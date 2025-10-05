# 🧑‍💻🛠️ Hoster helper FAQ

1. **What is a Hoster?**

    A [🧑‍💻 Hoster](<05 ☁️🛠️ Hoster helper.md>) is 
    * any [Helper 🛠️ domain](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>)
    * that hosts the infrastructure of a [Hosted 🧑‍💻 domain](<10 🧑‍💻☁️ Hosted domain.md>)
    * and allow their owners to manage them with a [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    ---
    <br/>

1. **What roles do Hosters typically implement?**

    | [Role 🎭](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | Purpose
    |-|-
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | To have [Chats 💬](<../12 💬 Chats/01 💬 Chat.md>) with users.
    | [🗄️ Vault](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) | To store the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) settings.
    | [🎴 Issuer](<../25 🎫 Tokens/02 🎴🎭 Issuer role.md>) | To issue [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) ownership [Tokens 🎫](<../25 🎫 Tokens/01 🎫 Token.md>).
    | [🪢 Integrator](<../12 💬 Chats/06 🪢🎭 Integrator role.md>) | To manifest the hosting service to  [Finder 🔎 domains](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>).
    | [💵 Seller](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) | To sell the usage plans via a [Biller 💳 helper domain](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>).
    

    ---
    <br/>

1. **What domain Helpers do Hosters typically leverage?**

    | [Helper 🛠️](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>)  | Purpose 
    |-|-
    | [💳 Biller](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>) | To manage usage and subscription plans.
    | [🏦 Collector](<../../30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) | To collect usage and subscription payments.
    
    ---
    <br/>


1. **How can a domain admin user leverage a [🧑‍💻 Hoster](<05 ☁️🛠️ Hoster helper.md>)?**

    |#| Category | Step
    |-|-|-
    |1| `Find` | Using their [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), <br/>the admin user [finds 🔎](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) a [Hoster ☁️ domain](<../12 💬 Chats/01 💬 Chat.md>) with the [Hoster's Host 🤗 role](<../12 💬 Chats/04 🤗🎭 Host role.md>).
    |2| `Bind`| On the [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>), <br/>the user [Binds 🔗](<../24 🗄️ Vaults/01 🔗 Bind.md>) to the [Hoster's Vault 🗄️ role](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>), <br/>and creates a new [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).
    |3| `Clone`| On a workstation terminal, <br/>the user [scans ✨](<../11 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>) the terminal QR code <br/>to link the terminal to the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)<br/>and download the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) settings.
    |4| `Edit`| On a code editor (e.g., Visual Studio Code)<br/>the user configures the logic webhooks <br/>and the public [domain 📜 Manifest](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>).
    |5| `Sync`| On the workstation terminal, <br/>the user synchronizes the changes <br/>with the [Hoster ☁️ domain](<05 ☁️🛠️ Hoster helper.md>).
    |6| `Test`| From the workstation terminal, <br/>the user opens [Chats 💬](<../12 💬 Chats/01 💬 Chat.md>) for manual testing.

    ---
    <br/>


1. **What does the Wallet Chat looks like?**

    | Service | Prompt  | User 
    | - | - | - 
    | [🧑‍💻 Hoster](<05 ☁️🛠️ Hoster helper.md>) | 😃 Hi! What do you need? <br/>- [ Create ] a domain <br/>- [ Something else ] | > Create
    | [🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Bind [Yes, No]<br/>- domain admin 🧩 | > Yes 
    | [🧑‍💻 Hoster](<05 ☁️🛠️ Hoster helper.md>) | 😃 Name for the domain? | `my-domain`
    | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save token? [Yes, No] <br/>- domain owner 🎫 <br/>- of my-domain
    | [🧑‍💻 Hoster](<05 ☁️🛠️ Hoster helper.md>) | ✅ Done!
    
    ---
    <br/>

1. **What commands are supported on the terminal CLI?**

    The terminal Command Line Interface (CLI) supports the following commands.

    |🧑‍💻 Command | Description
    |-|-
    |`clone <name>` | Generates a [QR Locator 🔆](<../11 🔆 Locators/01 🔆 Locator.md>)<br> for the user to scan with the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)<br/>to clone the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) to a local folder<br/>- e.g., `my-hoster clone my-domain`
    |`sync` | Syncs the changes with the [Hoster ☁️ domain](<05 ☁️🛠️ Hoster helper.md>) <br/>- e.g., `my-hoster sync`
    |`chat <env>`| Opens a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) with an environment<br/>on the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)<br/>- e.g., `my-hoster chat local`
    <!--|`test <env>`| Runs test scripts on an environment<br/>- e.g., `my-hoster test local`-->

    ---
    <br/>

1. **What does a terminal CLI interaction looks like?**

    |🧑‍💻 Command | 🖥️ Display |  Workstation
    |-|-|-
    |`$ clone my-domain` | ⏳ Scan the QR code... | [✨ scan](<../11 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>)
    || ✅ Domain cloned to folder
    |`code .` | &lt;opens visual studio code&gt;| 🧑‍💻 implement
    |`$ sync` | ✅ Changes synchronized.
    |`$ chat dev` | ⏳ Chat on your Wallet... | [💬 chat](<../12 💬 Chats/01 💬 Chat.md>)
    || ✅ Chat finished. | 
    |`$ chat prod` | ⏳ Chat on your Wallet... | [💬 chat](<../12 💬 Chats/01 💬 Chat.md>)
    || ✅ Chat finished. | 
    <!--|`$ test dev` | ✅ Tested successfully. | 🥳 celebrate-->
    
    

    ---
    <br/>



1. **What happens when the Wallet scans the QR?**

    | Service | Prompt  | User 
    | - | - | - 
    | [🧑‍💻 Hoster](<05 ☁️🛠️ Hoster helper.md>) | ℹ️ Cloning request:<br/>- domain: my-domain<br/>- from: London, UK
    | [🧑‍💻 Hoster](<05 ☁️🛠️ Hoster helper.md>) | 😃 Authorize? [Yes, No]<br/>- [ I don't recognize it ] | > Yes
    | [🧑‍💻 Hoster](<05 ☁️🛠️ Hoster helper.md>) | ✅ Authorized!
    
    ---
    <br/>
