🧑‍🦰 Wallet app
===

1. **What is a PollyWeb Wallet app?**

    [Wallets 🧑‍🦰](<🧑‍🦰 Wallet 🛠️ app.md>) are 
    * apps for mobile devices (e.g. Android-based phones, iPhones) 
    * that implement the PollyWeb protocol.

    ---
    <br/>

1. **What can a user do with a Wallet?**

    ![](<🧑‍🦰🏞️ Wallet img.png>)

    The following features are available in a [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet 🛠️ app.md>):
    - 💬 [Chats](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>): list, filter, search, view, and interact.
    - 🔗 [Binds](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>): list, view, unbind, and chat with the bound [Vault 🗄️ domain](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>). 
    - 🎫 [Tokens](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>): view, and chat with the [Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>).
    - ✨ [Scan](<../../../25 🔆 Locators/Locators 🔆/🔆⏩ Locator flows/🧑‍🦰✨ Wallet QR scan.md>) a QR [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) to open a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>).
    - 🔆 [Tap](<../../../25 🔆 Locators/Locators 🔆/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>) an NFC [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) to open a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>).
    - 🌐 [Click](<../../../25 🔆 Locators/Locators 🔆/🔆⏩ Locator flows/🧑‍🦰🌐 Wallet URLs.md>) on [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) links in the device's web browser to open chats.
    - 🛜 [Wi-Fiers](<../../../60 🧰 Edge/61 🔌 Pluggables/03 🛜🔀 Wi-Fier router.md>): tap/scan an NFC/QR of a Wi-Fier to enable Wi-Fi on a [Robot 🤖](<../../../25 🔆 Locators/Robots 🤖/🤖💠 Robot thing.md>).
    - 🔒 [Padlocks](<../../../70 🌳 Ambient/75 🔒 Padlocks/$ 🔒 Padlock device.md>): tap/scan an NFC/QR of a Padlock to open it.
    
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

1. **What happens when users install a PollyWeb Wallet?**

    On its first use, [Wallet 🧑‍🦰 apps](<🧑‍🦰 Wallet 🛠️ app.md>):
    1. create a key-pair for user and store it in the secure area of the device;
        - e.g., in Android, this is the high-level behavior of [passkeys 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/03 📺 Google passkeys.md>);
    2. register the user's public half of the key-pair in the [Wallet's Notifier 📣 domain](<../../Notifiers 📣/📣/📣 Notifier 👥 domain.md>);
    3. store locally the wallet ID returned by the [Notifier 📣 domain](<../../Notifiers 📣/📣/📣 Notifier 👥 domain.md>).

    ---
    <br/>

1. **What data exists in the device at any given time?**

    The only data that [Wallet 🧑‍🦰 apps](<🧑‍🦰 Wallet 🛠️ app.md>) store locally is:
    - 🔏 The private half of the key pair;
    - 📣 The Wallet ID provided by the [Broker 🤵 domain](<../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) via the [Notifier 📣 domain](<../../Notifiers 📣/📣/📣 Notifier 👥 domain.md>);
    - 🎫 Downloaded [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) from [Issuer 🎴 domains](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>).

    ---
    <br/>

1. **Do wallets work after backing up and restoring a phone?**

    Yes. 
    - If the OS of the old phone is backed up and restored on another Android or iOS phone, then nothing else is required given that the key-pair of the [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet 🛠️ app.md>) isn't dependent on any hardware key, and is stored on the OS Vault.

    ---
    <br/>


1. **How do users migrate a Wallet to another phone?**

    To migrate a [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet 🛠️ app.md>) to another phone, a user first needs to bind an [Identifier 🆔 agent domain](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) on the old phone, and then generate a migration QR [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>).
    
    * On the new phone, the user needs to install a [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet 🛠️ app.md>), then scan the migration QR of the old Wallet.
    * The [Broker 🤵 domain](<../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) will invoke the [Identifier 🆔 domain](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) on the new phone to perform an identity authentication (e.g., face scan), and then will automatically decommission the old Wallet.

    ---
    <br/>

1. **How do users change between Wallet providers?**

    If both the old and the new [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet 🛠️ app.md>) providers use the same [Broker 🤵 domain](<../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>), 
    * then changing between Wallet providers in the same phone is very similar to migrating a Wallet to another phone. 
    
    If they use different [Broker 🤵 domains](<../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>), 
    * then these Brokers will need to implement some sort of portability. 
     
    For simplicity, let's assume they use the same [Broker 🤵 domain](<../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>).
    
    * On the old [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet 🛠️ app.md>), the user generates a migration QR Token and downloads it or sends it to another person. 
    * Then, on the new [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet 🛠️ app.md>), the user uploads or scans the migration QR and performs an identity authentication (e.g., face scan).

    ---
    <br/>

1. **What if an attacker intercepts a user's recovery QR Token?**

    When a migration QR is used on a new [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet 🛠️ app.md>), the [Broker 🤵 domain](<../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) notifies the old Wallet, allowing legitimate owners to block the attack and destroy the QR. 
    
    * For situations where legitimate owners are not aware of notifications, migrations have a small grace period where [Broker 🤵 domains](<../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) inactivate both Wallets until the old Wallet accepts the transfer or the grace period expires.

    ---
    <br/>

1. **After destroying a migration QR, how can users migrate?**

    Just generate a new migration QR.

    ---
    <br/>

1. **After losing a phone, how do users recover a wallet on a new phone?**

    If the old phone is not available, then users need an offline migration QR previously printed or saved as an image - without it, it's not possible to recover the Wallet. 
    
    * On the new phone, users install a [Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet 🛠️ app.md>), scan or upload the QR, perform an identity authentication, and wait for the grace period.

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
    | 🤵 Set up | [👉 Onboard](<../🧑‍🦰✨ Wallet onboard 🤵/...in App/🧑‍🦰 Onboard 💬 flow.md>)  | Register the [Wallet 🧑‍🦰](<🧑‍🦰 Wallet 🛠️ app.md>) on a [Broker 🤵](<../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>)
    | | [👉 Translate](<../🧑‍🦰💬 Wallet chats/...in App 🏠/Set Language 💬🤵/🧑‍🦰 Set Language ⏩ flow.md>)  | Change the language of the [Wallet 🧑‍🦰](<🧑‍🦰 Wallet 🛠️ app.md>)
    | 🔆 Locators |[👉 Host QR](<../🧑‍🦰💬 Wallet chats/...in App 🏠/Tap host locator 🔆🤗 /🧑‍🦰 Tap host locator ⏩ flow.md>)  | Scan a [Host 🤗 NFC/QR](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>)   to open a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
    ||[👉 Printer QR](<../🧑‍🦰💬 Wallet chats/...in App 🏠/Tap alias locator 🔆🖨️ /🧑‍🦰 Tap alias locator ⏩ flow.md>)  | Scan a [Printer 🖨️ NFC/QR](<../../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>) to open a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
    |💬 Chats|[👉 Home](<../🧑‍🦰💬 Wallet chats/...in Chats 💬/Host home 💬🤵/🧑‍🦰 Host home ⏩ flow.md>) | Show the [Host's 🤗 ](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) menu in a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
    ||[👉 Abandon](<../🧑‍🦰💬 Wallet chats/...in Chats 💬/Abandon 💬🤵/🧑‍🦰 Abandon chat ⏩ flow.md>) | Unilaterally abandon a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
    | 🔗 Binds |  [👉 Bind](<../🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Bind 👉🗄️🔗/🧑‍🦰 Bind vault ⏩ flow.md>) | [Bind 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) the [Wallet 🧑‍🦰](<🧑‍🦰 Wallet 🛠️ app.md>) to a [Vault 🗄️](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>)
    || [👉 Unbind](<../🧑‍🦰💬 Wallet chats/...in Vaults 🗄️/Unbind 💬🗄️🤵 /🧑‍🦰 Unbind vault ⏩ flow.md>) | Remove a [Bind 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) from a [Vault 🗄️](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>)
    ||[👉 Share](<../🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Bind 👉🔗💼/🧑‍🦰 Share Bind ⏩ flow.md>) | Shares a [Bind 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) with a [Consumer 💼](<../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>)
    |🎫 Tokens| [👉 Save](<../🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>) | Save a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) in the [Wallet 🧑‍🦰](<🧑‍🦰 Wallet 🛠️ app.md>)
    || [👉 Remove](<../🧑‍🦰💬 Wallet chats/...in Tokens 🎫/Remove 💬🎫🤵 /🧑‍🦰 Remove Token ⏩ flow.md>) | Remove a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) from the [Wallet 🧑‍🦰](<🧑‍🦰 Wallet 🛠️ app.md>)
    || [👉 Share](<../🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>) | Share a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) with a [Consumer 💼](<../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>)
    || [👉 Verify ID](<../🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token+ID 👉🆔💼/🧑‍🦰 Share Token+ID ⏩ flow.md>) | Share and [verify the user Identifier 🆔](<../../../50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/3 Verify Tokens 🆔⏩🎫/🆔⏩ Verify Tokens.md>)

    ---
    <br/>