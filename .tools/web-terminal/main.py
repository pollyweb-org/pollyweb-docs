import signal
from pathlib import Path

from webview_controller import WebViewController


def main():
    page_path = Path(__file__).with_name("page.html").resolve()
    view = WebViewController(url=str(page_path))

    def handle_message(message):
        print(f"Message from WebView: {message}")
        view.close()

    view.set_on_message(handle_message)

    def handle_sigint(signum, frame):
        if view.is_closing:
            return
        print("\nCtrl+C detected. Closing window…")
        view.close()

    signal.signal(signal.SIGINT, handle_sigint)

    view.open()
    print("WebView opened.")
    print("Enter text in the page and press the Close button, or close the window / press Ctrl+C to exit.")

    try:
        view.run()
    finally:
        if not view.is_closing:
            view.close()

    print("Window closed. Exiting…")


if __name__ == "__main__":
    main()
