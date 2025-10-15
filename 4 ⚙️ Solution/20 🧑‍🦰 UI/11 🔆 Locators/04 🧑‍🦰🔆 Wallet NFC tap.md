🧑‍🦰 Wallet NFC tap 🔆
===

1. **How do Wallets tap an NFC Locator?**

    NLWeb NFC tags are standard NDEF Records of type URI starting with `https://nlweb.org/go/`. 
    
    * On install, NLW [Wallet apps 🧑‍🦰](<../01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) register on the OS as the default NFC reader - this differs from NFC payments, and does not interfere with the default NFC payment mechanisms of Google and Apple Wallets. 
    
    * When users read an NFC tag, Wallets discard any URL tag that doesn't start with `https://nlweb.org/go/`, and open a chat to the [Locator 🔆](<$ 🔆 Locator.md>)'s [Host 🤗](<../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>).

    ---

1. **What if users use the default NFC reader instead?**

    Users will have an experience similar to users not using the [Wallet 🧑‍🦰](<../01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) to [scan NLWeb QR codes](<03 🧑‍🦰✨ Wallet QR scan.md>). Also in this case, Wallets should educate users to set the Wallet as the default NFC reader.

    ---

1. **What if users without a Wallet tap an NFC?**

    If a user doesn't have an NLWeb [Wallet app 🧑‍🦰](<../01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) installed and taps an NFC with the mobile device's default NFC reader scanner then a web browser opens with an experience similar to [scanning a QR](<03 🧑‍🦰✨ Wallet QR scan.md>) without a Wallet. 

    ---