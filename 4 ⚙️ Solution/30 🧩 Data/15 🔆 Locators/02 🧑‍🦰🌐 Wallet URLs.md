🧑‍🦰 Wallet URL navigation 🌐
===

1. **How can app developers handle NLWeb URLs?**

    An NLWeb [Locator 🔆](<$ 🔆 Locator.md>) link is an Uniform Resource Locator (URL) starting with the custom protocol `nlweb://` (e.g., a locator `ABC` can be handled with the URL `nlweb://ABC`). 
    
    * When installing, [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) register themselves to handle the `nlweb` protocol - if more than one app is able to handle the protocol, then the Operating System (OS) asks the user to select one of the apps. 
    
    * When the Wallet app opens, it reads the link passed by the OS and then opens a chat with the Host domain in the URL's Locator.

    ---
    <br/>

1. **What if an NLWeb Wallet is not installed in the device?**

    NLWeb advocates for developers to use the redirect script at `https://nlweb.org/go/` so that users without an installed [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) can fallback to a page with instructions on how to install one. 
    
    * If a user with an NLWeb [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) installed navigates to a redirect link (e.g., `https://nlweb.org/go/ABC`), the browser redirects to a `nlweb` URL, signaling the OS to open the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) - the [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) then opens with a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) to the link's host. 

    ---
    <br/>

1. **How can website developers add NLWeb links?**

    Website developers can use NLWeb's proxy at `nlweb.org/go` (e.g., a [Locator 🔆](<$ 🔆 Locator.md>) `XPTO` is defined as an HTML anchor to `https://nlweb.org/go/XPTO`). 
    
    * When a user clicks on the link on a web browser, the proxy redirects the browser to a `nlweb://` protocol, then uses JavaScript to monitor the success of the redirection.

    * If no mobile app opens the `nlweb://` URL, then the proxy redirects to a fallback webpage explaining to the user how to find and install an app that supports the NLWeb protocol. 

    * Website developers can also opt to link the JavaScript library `https://nlweb.org/sdk/nlweb.js` - this allows [Wallets 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) to achieve the same behavior without browser redirects.
    
    * See [here](<https://gist.github.com/diachedelic/0d60233dab3dcae3215da8a4dfdcd434>) for details.

    ---
    <br/>

1. **What happens to NFC/QR Locators if `nlweb.org` goes down?**

    * Users using their [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) as the default NFC/QR reader won't notice any difference, because the [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) will parse the destination [Host 🤗](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) from the URL.

    * Conversely, users without a Wallet will see an HTTP 404 error on their web browsers when interacting with an NLWeb NFC/QR, because the OS will navigate to the fallback URL which points to `nlweb.org`.

    ---
    <br/>