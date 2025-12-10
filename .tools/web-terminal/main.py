from webview_controller import WebViewController

def on_message(msg):
    print("JS → Python:", msg)

    if msg == "close":
        print("Closing window...")
        view.close()

view = WebViewController(
    url="https://example.com",
    on_message=on_message
)

view.open()

print("WebView opened. Waiting for events...")
view.thread.join()
print("Window closed. Exiting…")
