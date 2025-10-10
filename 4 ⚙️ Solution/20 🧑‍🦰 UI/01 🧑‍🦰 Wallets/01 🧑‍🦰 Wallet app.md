🧑‍🦰 Wallet app
===



1. **What is an NLWeb Wallet app?**

    [Wallets 🧑‍🦰](<01 🧑‍🦰 Wallet app.md>) are 
    * apps for mobile devices (e.g. Android-based phones, iPhones) 
    * that implement the NLWeb protocol.

    ---
    <br/>

1. **What can a user do with a Wallet?**

    ![](<.📎 Assets/🧑‍🦰 Wallet App.png>)

    The following features are available in a [Wallet 🧑‍🦰 app](<01 🧑‍🦰 Wallet app.md>):
    - 💬 [Chats](<../12 💬 Chats/01 💬 Chat.md>): list, filter, search, view, and interact.
    - 🔗 [Binds](<../24 🗄️ Vaults/01 🔗 Bind.md>): list, view, unbind, and chat with the bound [Vault 🗄️ domain](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>). 
    - 🎫 [Tokens](<../25 🎫 Tokens/01 🎫 Token.md>): view, and chat with the [Issuer 🎴 domain](<../25 🎫 Tokens/02 🎴🎭 Issuer role.md>).
    - ✨ [Scan](<../11 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>) a QR [Locator 🔆](<../11 🔆 Locators/01 🔆 Locator.md>) to open a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>).
    - 🔆 [Tap](<../11 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>) an NFC [Locator 🔆](<../11 🔆 Locators/01 🔆 Locator.md>) to open a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>).
    - 🌐 [Click](<../11 🔆 Locators/02 🧑‍🦰🌐 Wallet URLs.md>) on [Locator 🔆](<../11 🔆 Locators/01 🔆 Locator.md>) links in the device's web browser to open chats.
    - 🛜 [Wi-Fiers](<../../60 🧰 Edge/61 🔌 Pluggables/03 🛜🔀 Wi-Fier router.md>): tap/scan an NFC/QR of a Wi-Fier to enable Wi-Fi on a [Robot 🤖](<../../70 🌳 Ambient/72 🤖 Brand Robots/01 🤖💠 Robot thing.md>).
    - 🔒 [Padlocks](<../../70 🌳 Ambient/75 🔒 Brand Padlocks/01 🔒 Padlock device.md>): tap/scan an NFC/QR of a Padlock to open it.
    
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

    On its first use, [Wallet 🧑‍🦰 apps](<01 🧑‍🦰 Wallet app.md>):
    1. create a key-pair for user and store it in the secure area of the device;
        - e.g., in Android, this is the high-level behavior of [passkeys 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/03 📺 Google passkeys.md>);
    2. register the user's public half of the key-pair in the [Wallet's Notifier 📣 domain](<../02 📣 Notifiers/02 📣 Notifier domain.md>);
    3. store locally the wallet ID returned by the [Notifier 📣 domain](<../02 📣 Notifiers/02 📣 Notifier domain.md>).

    ---
    <br/>

1. **What data exists in the device at any given time?**

    The only data that [Wallet 🧑‍🦰 apps](<01 🧑‍🦰 Wallet app.md>) store locally is:
    - 🔏 The private half of the key pair;
    - 📣 The Wallet ID provided by the [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) via the [Notifier 📣 domain](<../02 📣 Notifiers/02 📣 Notifier domain.md>);
    - 🎫 Downloaded [Tokens 🎫](<../25 🎫 Tokens/01 🎫 Token.md>) from [Issuer 🎴 domains](<../25 🎫 Tokens/02 🎴🎭 Issuer role.md>).

    ---
    <br/>

1. **Do wallets work after backing up and restoring a phone?**

    Yes. 
    - If the OS of the old phone is backed up and restored on another Android or iOS phone, then nothing else is required given that the key-pair of the [Wallet 🧑‍🦰 app](<01 🧑‍🦰 Wallet app.md>) isn't dependent on any hardware key, and is stored on the OS Vault.

    ---
    <br/>


1. **How do users migrate a Wallet to another phone?**

    To migrate a [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to another phone, a user first needs to bind an [Identity 🆔 agent domain](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) on the old phone, and then generate a migration QR [Token 🎫](<../25 🎫 Tokens/01 🎫 Token.md>).
    
    * On the new phone, the user needs to install a [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), then scan the migration QR of the old Wallet.
    * The [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) will invoke the [Identity 🆔 domain](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) on the new phone to perform an identity authentication (e.g., face scan), and then will automatically decommission the old Wallet.

    ---
    <br/>

1. **How do users change between Wallet providers?**

    If both the old and the new [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) providers use the same [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>), 
    * then changing between Wallet providers in the same phone is very similar to migrating a Wallet to another phone. 
    
    If they use different [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>), 
    * then these Brokers will need to implement some sort of portability. 
     
    For simplicity, let's assume they use the same [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>).
    
    * On the old [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), the user generates a migration QR Token and downloads it or sends it to another person. 
    * Then, on the new [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), the user uploads or scans the migration QR and performs an identity authentication (e.g., face scan).

    ---
    <br/>

1. **What if an attacker intercepts a user's recovery QR Token?**

    When a migration QR is used on a new [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), the [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) notifies the old Wallet, allowing legitimate owners to block the attack and destroy the QR. 
    
    * For situations where legitimate owners are not aware of notifications, migrations have a small grace period where [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) inactivate both Wallets until the old Wallet accepts the transfer or the grace period expires.

    ---
    <br/>

1. **After destroying a migration QR, how can users migrate?**

    Just generate a new migration QR.

    ---
    <br/>

1. **After losing a phone, how do users recover a wallet on a new phone?**

    If the old phone is not available, then users need an offline migration QR previously printed or saved as an image - without it, it's not possible to recover the Wallet. 
    
    * On the new phone, users install a [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), scan or upload the QR, perform an identity authentication, and wait for the grace period.

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
    | 🤵 Set up | [👉 Onboard](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/10 👉🤵 Set-up/11 🧑‍🦰👉🤵 Onboard.md>)  | Register the [Wallet 🧑‍🦰](<01 🧑‍🦰 Wallet app.md>) on a [Broker 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>)
    | | [👉 Translate](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/10 👉🤵 Set-up/12 🧑‍🦰👉🤵 Translate.md>)  | Change the language of the [Wallet 🧑‍🦰](<01 🧑‍🦰 Wallet app.md>)
    | 🔆 Locators |[👉 Host QR](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/01 🧑‍🦰👉🤗 Scan host QR.md>)  | Scan a [Host 🤗 NFC/QR](<../12 💬 Chats/04 🤗🎭 Host role.md>)   to open a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)
    ||[👉 Printer QR](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/02 🧑‍🦰👉🤗 Scan printer QR.md>)  | Scan a [Printer 🖨️ NFC/QR](<../../70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>) to open a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)
    |💬 Chats|[👉 Chats](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/01 🧑‍🦰👉🤵 List chats.md>) | List the user's [Chats 💬](<../12 💬 Chats/01 💬 Chat.md>) 
    ||[👉 Home](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/02 🧑‍🦰👉🤵 Host home.md>) | Show the [Host's 🤗 ](<../12 💬 Chats/04 🤗🎭 Host role.md>) menu in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)
    ||[👉 Abandon](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>) | Unilaterally abandon a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)
    | 🔗 Binds | [👉 Binds ](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/01 🧑‍🦰👉🤵 List Binds.md>) | List the user's [Binds 🔗](<../24 🗄️ Vaults/01 🔗 Bind.md>)
    || [👉 Bind](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind.md>) | [Bind 🔗](<../24 🗄️ Vaults/01 🔗 Bind.md>) the [Wallet 🧑‍🦰](<01 🧑‍🦰 Wallet app.md>) to a [Vault 🗄️](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)
    || [👉 Unbind](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/03 🧑‍🦰👉🗄️ Unbind.md>) | Remove a [Bind 🔗](<../24 🗄️ Vaults/01 🔗 Bind.md>) from a [Vault 🗄️](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)
    ||[👉 Share](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind.md>) | Shares a [Bind 🔗](<../24 🗄️ Vaults/01 🔗 Bind.md>) with a [Consumer 💼](<../27 💼 Consumers/04 💼🎭 Consumer role.md>)
    |🎫 Tokens| [👉 Tokens](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/01 🧑‍🦰👉🤵 List Tokens.md>)| List the user's [Tokens 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
    || [👉 Save](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save Token.md>) | Save a [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) in the [Wallet 🧑‍🦰](<01 🧑‍🦰 Wallet app.md>)
    || [👉 Remove](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/03 🧑‍🦰👉🤵 Remove Token.md>) | Remove a [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) from the [Wallet 🧑‍🦰](<01 🧑‍🦰 Wallet app.md>)
    || [👉 Share](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token.md>) | Share a [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) with a [Consumer 💼](<../27 💼 Consumers/04 💼🎭 Consumer role.md>)
    || [👉 Verify ID](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/05 🧑‍🦰👉💼 Share Token+ID.md>) | Share and [verify the user Identity 🆔](<../../30 🫥 Agents/05 🆔 Identities/14 🆔🎫 Verify Tokens.md>)

    ---
    <br/>