🧑‍🦰 Wallet NFC tap 🔆
===

> Part of [🔆 Locators](<../🔆 Locator.md>)

## FAQ

1. **How do Wallets tap an NFC Locator?**

    PollyWeb NFC tags are standard NDEF Records of type URI starting with `https://pollyweb.org/go/`. 
    
    * On install, NLW [Wallet apps 🧑‍🦰](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) register on the OS as the default NFC reader - this differs from NFC payments, and does not interfere with the default NFC payment mechanisms of Google and Apple Wallets. 
    
    * When users read an NFC tag, Wallets discard any URL tag that doesn't start with `https://pollyweb.org/go/`, and open a chat to the [Locator 🔆](<../🔆 Locator.md>)'s [Host 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).

    ---
    <br/>

1. **What if users use the default NFC reader instead?**

    Users will have an experience similar to users not using the [Wallet 🧑‍🦰](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to [scan PollyWeb QR codes](<🧑‍🦰✨ Wallet QR scan.md>). Also in this case, Wallets should educate users to set the Wallet as the default NFC reader.

    ---
    <br/>

1. **What if users without a Wallet tap an NFC?**

    If a user doesn't have an PollyWeb [Wallet app 🧑‍🦰](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) installed and taps an NFC with the mobile device's default NFC reader scanner then a web browser opens with an experience similar to [scanning a QR](<🧑‍🦰✨ Wallet QR scan.md>) without a Wallet. 

    ---
    <br/>