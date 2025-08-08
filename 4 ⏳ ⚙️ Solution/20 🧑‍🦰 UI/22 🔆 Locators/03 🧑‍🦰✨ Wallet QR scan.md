🧑‍🦰 Wallet QR scan ✨ FAQ
===

1. **How can website developers render an NLWeb QR?**

    Website developers can use NLWeb's proxy at `nlweb.org/go` (e.g., a Locator `XPTO` is defined as an HTML image with source `https://nlweb.org/go/XPTO`). 
    
    If in a mobile web browser, the proxy renders a button; otherwise, it renders a QR image. Buttons and QR images contain links to the `nlweb.org/go` proxy.

    ---

1. **How do Wallet apps scan an NLWeb QR?**

    An NLWeb QR contains a redirect URL starting with `https://nlweb.org/go/`. 
    
    * When a user scans the QR with an NLWeb Wallet app, the Wallet reads the [Locator 🔆](<01 ✅ 🔆 Locator.md>) from the URL and opens a chat with the Locator's [Host 🤗](<../23 ✅ 💬 Chats/03 ✅ 🤗🎭 Host role.md>).


    ---

1. **What if users use the default QR reader instead?**

    If a user with an NLWeb [Wallet app 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>) installed decides to use the mobile device's default QR scanner instead (e.g., Google Lens in Android) then a web browser opens the NLWeb HTTPS proxy (e.g., `https://nlweb.org/go/ABC`), which in turn redirect to a `nlweb` URL, signaling the OS to open the Wallet - the Wallet then opens with a chat to the QR's [Host 🤗](<../23 ✅ 💬 Chats/03 ✅ 🤗🎭 Host role.md>). Wallets should identify this redirect and educate users to prefer using the Wallet to perform the QR scan.


    ---

1. **What if users without a Wallet scan a QR?**

    If a user doesn't have an NLWeb [Wallet app 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>) installed and scans an NLWeb QR with the mobile device's default QR scanner (e.g., Google Lens in Android) then a web browser will open on `https://nlweb.org/install` educating the user to find and install a compatible NLWeb app. 

    ---