import threading
import time

from Cocoa import (
    NSApplication,
    NSWindow,
    NSRect,
    NSBackingStoreBuffered,
    NSWindowStyleMaskTitled
)
from WebKit import (
    WKWebView,
    WKUserContentController,
    WKWebViewConfiguration,
    WKScriptMessageHandler,
    NSURL,
    NSURLRequest
)


class PythonMessageHandler(WKScriptMessageHandler):
    """Receives JS -> Python messages via window.webkit.messageHandlers.python.postMessage(...)"""

    def initWithCallback_(self, callback):
        self = super().init()
        self.callback = callback
        return self

    def userContentController_didReceiveScriptMessage_(self, controller, message):
        if self.callback:
            self.callback(message.body())


class WebViewController:
    def __init__(self, url: str, on_message=None):
        self.url = url
        self.on_message = on_message
        self.app = NSApplication.sharedApplication()
        self.window = None
        self.webview = None

    def _create_window(self):
        rect = NSRect(200, 200, 900, 700)

        config = WKWebViewConfiguration.alloc().init()
        user_controller = WKUserContentController.alloc().init()

        handler = PythonMessageHandler.alloc().initWithCallback_(self.on_message)
        user_controller.addScriptMessageHandler_name_(handler, "python")

        config.setUserContentController_(user_controller)

        self.window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            rect,
            NSWindowStyleMaskTitled,
            NSBackingStoreBuffered,
            False
        )
        self.window.setTitle_("Python WebView")

        self.webview = WKWebView.alloc().initWithFrame_configuration_(rect, config)

        nsurl = NSURL.URLWithString_(self.url)
        req = NSURLRequest.requestWithURL_(nsurl)
        self.webview.loadRequest_(req)

        self.window.setContentView_(self.webview)
        self.window.makeKeyAndOrderFront_(None)

    def _run_loop(self):
        self._create_window()
        self.app.run()

    def open(self):
        self.thread = threading.Thread(target=self._run_loop)
        self.thread.start()
        time.sleep(0.3)

    def close(self):
        if self.window:
            self.window.close()
        self.app.stop_(None)
        if hasattr(self, "thread"):
            self.thread.join()

    def eval_js(self, script: str):
        self.webview.evaluateJavaScript_completionHandler_(script, None)
