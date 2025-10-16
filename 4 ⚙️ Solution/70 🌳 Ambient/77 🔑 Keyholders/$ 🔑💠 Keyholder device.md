🔑 Keyholder device
===

![](<../75 🔒 Padlocks/. 📎 Assets/🔒 Keyholder.png>)

1. **What is a Keyholder?**

    In NLWeb, a Keyholder is a device that can scan and unlock [Padlock 🔒](<../75 🔒 Padlocks/$ 🔒 Padlock device.md>) devices.

    Examples of Keyholders include:
    * 🧑‍🦰 [Wallet apps](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) - Wallets support the Keyholder protocol natively.
    * ⌚ [Tapbands](<../../25 Locators/5 ⌚ Tapbands/⌚💠 Tapband thing.md>) - these are smart bands with the ability to connect to the internet (e.g., Bluetooth, eSim);

    ---

1. **What does a Keyholder store?**

    Keyholders store a list of Padlock keys, each containing:
    - the domain of the [🔐 KeyMaker](<../../45 🤲 Helper domains/58 🔐 Keymakers/05  🔐🏭 Keymaker supplier.md>) (e.g., `any-keymaker.com`) 
    - the resource key of the [Padlock 🔒](<../75 🔒 Padlocks/$ 🔒 Padlock device.md>) in the KeyMaker (e.g., `padlock-12345678`)
    - the encrypted sequence number for the key last rotation (e.g., `1234567890`)
    - the encrypted passkey for the last sequence number (e.g. `ABCDEF`)

    ---

1. **Why doesn't the Keyholder fetch the Keys online?**

    Keyholders store keys locally to allow users to quickly unlock Padlocks even with low-or-no internet connectivity - e.g., inside an underground gym.

    ---
