🧑‍🦰 Wallet app
===



1. **What is an NLWeb Wallet app?**

    [Wallets 🧑‍🦰](<🧑‍🦰 Wallet app.md>) are 
    * apps for mobile devices (e.g. Android-based phones, iPhones) 
    * that implement the NLWeb protocol.

    ---
    <br/>

1. **What can a user do with a Wallet?**

    ![](<.📎 Assets/🧑‍🦰 Wallet App.png>)

    The following features are available in a [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet app.md>):
    - 💬 [Chats](<../../35 💬 Chats/💬 Chats/💬 Chat.md>): list, filter, search, view, and interact.
    - 🔗 [Binds](<../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>): list, view, unbind, and chat with the bound [Vault 🗄️ domain](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>). 
    - 🎫 [Tokens](<../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>): view, and chat with the [Issuer 🎴 domain](<../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>).
    - ✨ [Scan](<../../25 🔆 Locators/1 🔆 Locators/🔆⏩ Locator flows/🧑‍🦰✨ Wallet QR scan.md>) a QR [Locator 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) to open a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>).
    - 🔆 [Tap](<../../25 🔆 Locators/1 🔆 Locators/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>) an NFC [Locator 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) to open a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>).
    - 🌐 [Click](<../../25 🔆 Locators/1 🔆 Locators/🔆⏩ Locator flows/🧑‍🦰🌐 Wallet URLs.md>) on [Locator 🔆](<../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) links in the device's web browser to open chats.
    - 🛜 [Wi-Fiers](<../../60 🧰 Edge/61 🔌 Pluggables/03 🛜🔀 Wi-Fier router.md>): tap/scan an NFC/QR of a Wi-Fier to enable Wi-Fi on a [Robot 🤖](<../../25 🔆 Locators/3 🤖 Robots/🤖💠 Robot thing.md>).
    - 🔒 [Padlocks](<../../70 🌳 Ambient/75 🔒 Padlocks/$ 🔒 Padlock device.md>): tap/scan an NFC/QR of a Padlock to open it.
    
    ---
    <br/>


1. **What permissions are required on the device?**

    - Localization settings (for translations)
    - Country location (for fraud prevention)
    - Geographical coordinates (for real-time workflows)    
    - Rear camera (for scanning)
    - Front camera (for identity verification)

    ---
    <br/>

1. **What happens when users install an NLWeb Wallet?**

    On its first use, [Wallet 🧑‍🦰 apps](<🧑‍🦰 Wallet app.md>):
    1. create a key-pair for user and store it in the secure area of the device;
        - e.g., in Android, this is the high-level behavior of [passkeys 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/03 📺 Google passkeys.md>);
    2. register the user's public half of the key-pair in the [Wallet's Notifier 📣 domain](<../2 📣 Notifiers/📣👥 Notifier domain.md>);
    3. store locally the wallet ID returned by the [Notifier 📣 domain](<../2 📣 Notifiers/📣👥 Notifier domain.md>).

    ---
    <br/>

1. **What data exists in the device at any given time?**

    The only data that [Wallet 🧑‍🦰 apps](<🧑‍🦰 Wallet app.md>) store locally is:
    - 🔏 The private half of the key pair;
    - 📣 The Wallet ID provided by the [Broker 🤵 domain](<../3 🤵 Brokers/🤵🤲 Broker helper.md>) via the [Notifier 📣 domain](<../2 📣 Notifiers/📣👥 Notifier domain.md>);
    - 🎫 Downloaded [Tokens 🎫](<../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) from [Issuer 🎴 domains](<../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>).

    ---
    <br/>

1. **Do wallets work after backing up and restoring a phone?**

    Yes. 
    - If the OS of the old phone is backed up and restored on another Android or iOS phone, then nothing else is required given that the key-pair of the [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet app.md>) isn't dependent on any hardware key, and is stored on the OS Vault.

    ---
    <br/>


1. **How do users migrate a Wallet to another phone?**

    To migrate a [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet app.md>) to another phone, a user first needs to bind an [Identity 🆔 agent domain](<../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) on the old phone, and then generate a migration QR [Token 🎫](<../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>).
    
    * On the new phone, the user needs to install a [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet app.md>), then scan the migration QR of the old Wallet.
    * The [Broker 🤵 domain](<../3 🤵 Brokers/🤵🤲 Broker helper.md>) will invoke the [Identity 🆔 domain](<../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) on the new phone to perform an identity authentication (e.g., face scan), and then will automatically decommission the old Wallet.

    ---
    <br/>

1. **How do users change between Wallet providers?**

    If both the old and the new [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet app.md>) providers use the same [Broker 🤵 domain](<../3 🤵 Brokers/🤵🤲 Broker helper.md>), 
    * then changing between Wallet providers in the same phone is very similar to migrating a Wallet to another phone. 
    
    If they use different [Broker 🤵 domains](<../3 🤵 Brokers/🤵🤲 Broker helper.md>), 
    * then these Brokers will need to implement some sort of portability. 
     
    For simplicity, let's assume they use the same [Broker 🤵 domain](<../3 🤵 Brokers/🤵🤲 Broker helper.md>).
    
    * On the old [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet app.md>), the user generates a migration QR Token and downloads it or sends it to another person. 
    * Then, on the new [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet app.md>), the user uploads or scans the migration QR and performs an identity authentication (e.g., face scan).

    ---
    <br/>

1. **What if an attacker intercepts a user's recovery QR Token?**

    When a migration QR is used on a new [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet app.md>), the [Broker 🤵 domain](<../3 🤵 Brokers/🤵🤲 Broker helper.md>) notifies the old Wallet, allowing legitimate owners to block the attack and destroy the QR. 
    
    * For situations where legitimate owners are not aware of notifications, migrations have a small grace period where [Broker 🤵 domains](<../3 🤵 Brokers/🤵🤲 Broker helper.md>) inactivate both Wallets until the old Wallet accepts the transfer or the grace period expires.

    ---
    <br/>

1. **After destroying a migration QR, how can users migrate?**

    Just generate a new migration QR.

    ---
    <br/>

1. **After losing a phone, how do users recover a wallet on a new phone?**

    If the old phone is not available, then users need an offline migration QR previously printed or saved as an image - without it, it's not possible to recover the Wallet. 
    
    * On the new phone, users install a [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet app.md>), scan or upload the QR, perform an identity authentication, and wait for the grace period.

    ---
    <br/>

1. **What if an attacker has the user's old phone and rejects the transfer?**

    After a successful identity authentication on the new phone, blocking the migration from the old phone will also require a successful identity authentication. 

    * This way, an attacker in the possession of the old phone will not be able to stop the migration to the legitimate user.

    ---
    <br/>


1. **What workflows can users execute in a Wallet app?**

    | Category | Workflow |  Description
    |-|-|-
    | 🤵 Set up | [👉 Onboard](<🧑‍🦰👉 Wallet flows/10 👉🤵 Set-up/11 🧑‍🦰👉🤵 Onboard.md>)  | Register the [Wallet 🧑‍🦰](<🧑‍🦰 Wallet app.md>) on a [Broker 🤵](<../3 🤵 Brokers/🤵🤲 Broker helper.md>)
    | | [👉 Translate](<🧑‍🦰👉 Wallet flows/10 👉🤵 Set-up/12 🧑‍🦰👉🤵 Translate.md>)  | Change the language of the [Wallet 🧑‍🦰](<🧑‍🦰 Wallet app.md>)
    | 🔆 Locators |[👉 Host QR](<🧑‍🦰👉 Wallet flows/15 👉🔆 Locators/01 🧑‍🦰👉🤗 Scan host QR.md>)  | Scan a [Host 🤗 NFC/QR](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)   to open a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>)
    ||[👉 Printer QR](<🧑‍🦰👉 Wallet flows/15 👉🔆 Locators/02 🧑‍🦰👉🤗 Scan printer QR.md>)  | Scan a [Printer 🖨️ NFC/QR](<../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>) to open a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>)
    |💬 Chats|[👉 Chats](<🧑‍🦰👉 Wallet flows/20 👉💬 Chats/01 🧑‍🦰👉🤵 List chats.md>) | List the user's [Chats 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) 
    ||[👉 Home](<🧑‍🦰👉 Wallet flows/20 👉💬 Chats/02 🧑‍🦰👉🤵 Host home.md>) | Show the [Host's 🤗 ](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) menu in a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>)
    ||[👉 Abandon](<🧑‍🦰👉 Wallet flows/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>) | Unilaterally abandon a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>)
    | 🔗 Binds | [👉 Binds ](<🧑‍🦰👉 Wallet flows/30 👉🔗 Binds/01 🧑‍🦰👉🤵 List binds.md>) | List the user's [Binds 🔗](<../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>)
    || [👉 Bind](<🧑‍🦰👉 Wallet flows/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind 🔗.md>) | [Bind 🔗](<../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>) the [Wallet 🧑‍🦰](<🧑‍🦰 Wallet app.md>) to a [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)
    || [👉 Unbind](<🧑‍🦰👉 Wallet flows/30 👉🔗 Binds/03 🧑‍🦰👉🗄️ Unbind.md>) | Remove a [Bind 🔗](<../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>) from a [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)
    ||[👉 Share](<🧑‍🦰👉 Wallet flows/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind 🔗.md>) | Shares a [Bind 🔗](<../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>) with a [Consumer 💼](<../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>)
    |🎫 Tokens| [👉 Tokens](<🧑‍🦰👉 Wallet flows/40 👉🎫 Tokens/01 🧑‍🦰👉🤵 List tokens.md>)| List the user's [Tokens 🎫](<../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>)
    || [👉 Save](<🧑‍🦰👉 Wallet flows/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) | Save a [Token 🎫](<../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) in the [Wallet 🧑‍🦰](<🧑‍🦰 Wallet app.md>)
    || [👉 Remove](<🧑‍🦰👉 Wallet flows/40 👉🎫 Tokens/03 🧑‍🦰👉🤵 Remove token.md>) | Remove a [Token 🎫](<../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) from the [Wallet 🧑‍🦰](<🧑‍🦰 Wallet app.md>)
    || [👉 Share](<🧑‍🦰👉 Wallet flows/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token 🎫.md>) | Share a [Token 🎫](<../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) with a [Consumer 💼](<../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>)
    || [👉 Verify ID](<🧑‍🦰👉 Wallet flows/40 👉🎫 Tokens/05 🧑‍🦰👉💼 Share Token+ID.md>) | Share and [verify the user Identity 🆔](<../../50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/3 🆔🎫 Verify Tokens.md>)

    ---
    <br/>