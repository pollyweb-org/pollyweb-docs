import objc

from Cocoa import (
    NSApplication,
    NSWindow,
    NSMakeRect,
    NSBackingStoreBuffered,
    NSWindowStyleMaskTitled,
    NSWindowStyleMaskClosable,
    NSWindowStyleMaskMiniaturizable,
    NSWindowStyleMaskResizable,
    NSObject
)
from WebKit import (
    WKWebView,
    WKWebViewConfiguration,
    WKUserContentController,
    NSURL,
    NSURLRequest
)
from PyObjCTools import AppHelper


class _WindowDelegate(NSObject):
    def initWithController_(self, controller):
        self = objc.super(_WindowDelegate, self).init()
        if self is None:
            return None
        self.controller = controller
        return self

    def windowWillClose_(self, notification):
        self.controller._handle_window_will_close()


class PythonMessageHandler(NSObject):
    def initWithCallback_(self, callback):
        self = objc.super(PythonMessageHandler, self).init()
        if self is None:
            return None
        self.callback = callback
        return self

    def userContentController_didReceiveScriptMessage_(self, controller, message):
        if hasattr(self, "callback") and self.callback is not None:
            self.callback(message.body())


class WebViewController:
    def __init__(self, url: str, on_message=None):
        self.url = url
        self.on_message = on_message
        self.app = NSApplication.sharedApplication()
        self.window = None
        self.webview = None
        self._closing = False
        self._delegate = None
        self._user_content_controller = None
        self._message_handler = None

    def _create_window(self):
        rect = NSMakeRect(200, 200, 900, 700)

        config = WKWebViewConfiguration.alloc().init()
        user_controller = WKUserContentController.alloc().init()

        self._message_handler = PythonMessageHandler.alloc().initWithCallback_(self._dispatch_js_message)
        user_controller.addScriptMessageHandler_name_(self._message_handler, "python")
        config.setUserContentController_(user_controller)
        self._user_content_controller = user_controller

        self.window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            rect,
            NSWindowStyleMaskTitled
            | NSWindowStyleMaskClosable
            | NSWindowStyleMaskMiniaturizable
            | NSWindowStyleMaskResizable,
            NSBackingStoreBuffered,
            False
        )
        self.window.setTitle_("Python WebView")

        self.webview = WKWebView.alloc().initWithFrame_configuration_(rect, config)

        self._delegate = _WindowDelegate.alloc().initWithController_(self)
        self.window.setDelegate_(self._delegate)

        if isinstance(self.url, str) and (self.url.startswith("http://") or self.url.startswith("https://")):
            nsurl = NSURL.URLWithString_(self.url)
        else:
            nsurl = NSURL.fileURLWithPath_(self.url)
        req = NSURLRequest.requestWithURL_(nsurl)
        self.webview.loadRequest_(req)

        self.window.setContentView_(self.webview)
        self.window.makeKeyAndOrderFront_(None)
        self.app.activateIgnoringOtherApps_(True)

    def open(self):
        self._create_window()

    def run(self):
        AppHelper.runEventLoop()

    def close(self):
        if not self._closing:
            self._closing = True

            def _close():
                if self.window is not None and self.window.isVisible():
                    self.window.close()
                if self._user_content_controller is not None and self._message_handler is not None:
                    self._user_content_controller.removeScriptMessageHandlerForName_("python")
                    self._message_handler = None
                self._stop_event_loop()

            AppHelper.callAfter(_close)
        else:
            self._stop_event_loop()

    def eval_js(self, script: str):
        self.webview.evaluateJavaScript_completionHandler_(script, None)

    @property
    def is_closing(self) -> bool:
        return self._closing

    def _handle_window_will_close(self):
        if not self._closing:
            self._closing = True
        self._stop_event_loop()

    def set_on_message(self, callback):
        self.on_message = callback

    def _dispatch_js_message(self, body):
        if self.on_message is not None:
            self.on_message(body)

    def _stop_event_loop(self):
        self.app.stop_(None)
        AppHelper.stopEventLoop()
