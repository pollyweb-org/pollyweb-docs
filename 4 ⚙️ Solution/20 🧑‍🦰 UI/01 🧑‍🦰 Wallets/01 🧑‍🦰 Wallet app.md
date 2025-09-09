🧑‍🦰 Wallet app FAQ
===

![](<.📎 Assets/🧑‍🦰 Wallet App.png>)

1. **What is an NLWeb Wallet app?**

    Wallets 🧑‍🦰 are apps for mobile devices (e.g. Android-based phones, iPhones) that implement the NLWeb protocol.

    ---

1. **What can a user do with a Wallet?**

    - 💬 [Chats](<../23 💬 Chats/01 💬 Chat.md>): list, filter, search, view, and interact.
    - 🔗 [Binds](<../24 🗄️ Vaults/01 🔗 Bind.md>): list, view, unbind, and chat with the bound [Vault 🗄️](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>). 
    - 🎫 [Tokens](<../25 🎫 Tokens/01 🎫 Token.md>): view, and chat with the [Issuer 🎴](<../25 🎫 Tokens/02 🎴🎭 Issuer role.md>).
    - ✨ [Scan](<../22 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>) a QR [Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>) to open a [Chat 💬](<../23 💬 Chats/01 💬 Chat.md>).
    - 🔆 [Tap](<../22 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>) an NFC [Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>) to open a [Chat 💬](<../23 💬 Chats/01 💬 Chat.md>).
    - 🌐 [Click](<../22 🔆 Locators/02 🧑‍🦰🌐 Wallet URLs.md>) on [Locator 🔆](<../22 🔆 Locators/01 🔆 Locator.md>) links in the device's web browser to open chats.
    - 🛜 [Wi-Fiers](<../../60 🧰 Edge/61 🔌 Pluggables/03 🛜🔀 Wi-Fier router.md>): tap/scan an NFC/QR of a Wi-Fier to enable Wi-Fi on a [Robot 🤖](<../../70 🌳 Ambient/72 🤖 Brand Robots/01 🤖💠 Robot thing.md>).
    - 🔒 [Padlocks](<../../70 🌳 Ambient/75 🔒 Brand Padlocks/01 🔒 Padlock device.md>): tap/scan an NFC/QR of a Padlock to open it.
    
    ---

1. **What are examples of bound Vaults?**

    The following are examples of user [Vaults 🗄️](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) that be available by default:
    - 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>), to change settings, migrate to another device, or recover from a lost device;
    - 📦 [Storage](<../../30 🫥 Agents/01 📦 Storage/01 📦🫥 Storage agent.md>), for data residency compliance;
    - 🧢 [Persona](<../../30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>), for managing user preferences;
    - 🆔 [Identity](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>), for identity authentication;
    - 💳 [Payer](<../../30 🫥 Agents/04 💳 Payers/02 💳🫥 Payer role.md>), for general payments;
    - ⭐ [Reviewer](<../../30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>), to provide feedback on [Hosts 🤗](<../23 💬 Chats/04 🤗💬 Host chats.md>);
    - 🔎 [Finder](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>), to search for [Locators 🔆](<../22 🔆 Locators/01 🔆 Locator.md>) according to the user's preferences;
    - 🛎️ [Concierge](<../../30 🫥 Agents/06 🛎️ Concierges/01 🛎️🫥 Concierge agent.md>), to perform tasks on behalf of the user;
    - 🎩 [Custodian](<../../70 🌳 Ambient/71 💠 Brand Things/05 🎩🗄️ Custodian vault.md>), to manage the user's [Things 💠](<../../70 🌳 Ambient/71 💠 Brand Things/01 💠 Thing.md>), [Robots 🤖](<../../70 🌳 Ambient/72 🤖 Brand Robots/01 🤖💠 Robot thing.md>), and [Userables 💍](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>).
    ---

1. **What permissions are required on the device?**

    - Localization settings (for translations)
    - Country location (for fraud prevention)
    - Geographical coordinates (for real-time workflows)    
    - Rear camera (for scanning)
    - Front camera (for identity verification)

    ---

1. **What happens when users install an NLWeb Wallet?**

    On its first use, Wallet 🧑‍🦰 apps:
    1. create a key-pair for user and store it in the secure area of the device;
        - e.g., in Android, this is the high-level behavior of [passkeys](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/03 📺 Google passkeys.md>);
    1. register the user's public half of the key-pair in the Wallet's [Notifier 📣](<../02 📣 Notifiers/02 📣 Notifier domain.md>);
    1. store locally the wallet ID returned by the [Notifier 📣](<../02 📣 Notifiers/02 📣 Notifier domain.md>).

    ---

1. **What data exists in the device at any given time?**

    The only data that [Wallets 🧑‍🦰](<01 🧑‍🦰 Wallet app.md>) store locally is:
    - 🔏 The private half of the key pair;
    - 📣 The Wallet ID provided by the [Notifier 📣](<../02 📣 Notifiers/02 📣 Notifier domain.md>);
    - 🎫 Downloaded [Tokens 🎫](<../25 🎫 Tokens/01 🎫 Token.md>) from [Issuers 🎴](<../25 🎫 Tokens/02 🎴🎭 Issuer role.md>).

    ---

1. **Do wallets work after backing up and restoring a phone?**

    Yes. 
    - If the OS of the old phone is backed up and restored on another Android or iOS phone, then nothing else is required given that the [Wallet's 🧑‍🦰](<01 🧑‍🦰 Wallet app.md>) key-pair isn't dependent on any hardware key, and is stored on the OS Vault.

    ---
