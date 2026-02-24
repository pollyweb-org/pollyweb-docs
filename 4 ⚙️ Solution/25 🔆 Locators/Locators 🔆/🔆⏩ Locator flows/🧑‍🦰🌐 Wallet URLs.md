🧑‍🦰 Wallet URL navigation 🌐
===

> Part of [🔆 Locators](<../🔆 Locator.md>)

## FAQ

1. **How can app developers handle PollyWeb URLs?**

    An PollyWeb [Locator 🔆](<../🔆 Locator.md>) link is an Uniform Resource Locator (URL) starting with the custom protocol `pollyweb://` (e.g., a locator `ABC` can be handled with the URL `pollyweb://ABC`). 
    
    * When installing, [Wallet 🧑‍🦰 apps](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) register themselves to handle the `pollyweb` protocol - if more than one app is able to handle the protocol, then the Operating System (OS) asks the user to select one of the apps. 
    
    * When the Wallet app opens, it reads the link passed by the OS and then opens a chat with the Host domain in the URL's Locator.

    ---
    <br/>

1. **What if an PollyWeb Wallet is not installed in the device?**

    PollyWeb advocates for developers to use the redirect script at `https://pollyweb.org/go/` so that users without an installed [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) can fallback to a page with instructions on how to install one. 
    
    * If a user with an PollyWeb [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) installed navigates to a redirect link (e.g., `https://pollyweb.org/go/ABC`), the browser redirects to a `pollyweb` URL, signaling the OS to open the [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) - the [Wallet 🧑‍🦰](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) then opens with a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) to the link's host. 

    ---
    <br/>

1. **How can website developers add PollyWeb links?**

    Website developers can use PollyWeb's proxy at `pollyweb.org/go` (e.g., a [Locator 🔆](<../🔆 Locator.md>) `XPTO` is defined as an HTML anchor to `https://pollyweb.org/go/XPTO`). 
    
    * When a user clicks on the link on a web browser, the proxy redirects the browser to a `pollyweb://` protocol, then uses JavaScript to monitor the success of the redirection.

    * If no mobile app opens the `pollyweb://` URL, then the proxy redirects to a fallback webpage explaining to the user how to find and install an app that supports the PollyWeb protocol. 

    * Website developers can also opt to link the JavaScript library `https://pollyweb.org/sdk/pollyweb.js` - this allows [Wallets 🧑‍🦰](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to achieve the same behavior without browser redirects.
    
    * See [here](<https://gist.github.com/diachedelic/0d60233dab3dcae3215da8a4dfdcd434>) for details.

    ---
    <br/>

1. **What happens to NFC/QR Locators if `pollyweb.org` goes down?**

    * Users using their [Wallet 🧑‍🦰 apps](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) as the default NFC/QR reader won't notice any difference, because the [Wallet 🧑‍🦰](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) will parse the destination [Host 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) from the URL.

    * Conversely, users without a Wallet will see an HTTP 404 error on their web browsers when interacting with an PollyWeb NFC/QR, because the OS will navigate to the fallback URL which points to `pollyweb.org`.

    ---
    <br/>