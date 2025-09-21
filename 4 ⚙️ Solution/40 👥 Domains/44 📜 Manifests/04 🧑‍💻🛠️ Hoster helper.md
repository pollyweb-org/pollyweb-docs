# 🧑‍💻🛠️ Hoster helper FAQ

1. **What is a Hoster?**

    A [🧑‍💻 Hoster](<04 🧑‍💻🛠️ Hoster helper.md>) is 
    * any [Helper 🛠️ domain](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>).
    * that host the infrastructure of other [domains 👥](<00 👥 Domain.md>).
    * and allow their owners to manage them with a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    ---
    <br/>

1. **What roles do Hosters typically implement?**

    | [Role 🎭](<00 👥 Domain.md>) | Purpose
    |-|-
    | [🤗 Host](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) | To have [Chats 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) with users.
    | [🗄️ Vault](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) | To store the [domain 👥](<00 👥 Domain.md>) settings.
    | [🎴 Issuer](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) | To issue [domain 👥](<00 👥 Domain.md>) ownership [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>).
    | [🪢 Integrator](<../../20 🧑‍🦰 UI/23 💬 Chats/06 🪢🎭 Integrator role.md>) | To manifest the hosting service to  [Finder 🔎 domains](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>).
    | [💵 Seller](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) | To sell the usage plans via a [Biller 💳 helper domain](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>).
    

    ---
    <br/>

2. **What domain Helpers do Hosters typically leverage?**

    | [Helper 🛠️](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>)  | Purpose 
    |-|-
    | [💳 Biller](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>) | To manage usage and subscription plans.
    | [🏦 Collector](<../../30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) | To collect usage and subscription payments.
    
    ---
    <br/>

3. **What is required from domain owners?**

    | Requirement | Purpose
    |-|-
    | [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) | To authenticate and [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) with the [🧑‍💻 Hoster](<04 🧑‍💻🛠️ Hoster helper.md>).
    | [Payer 💳 agent](<../../30 🫥 Agents/04 💳 Payers/04 💳🫥 Payer agent.md>) | To pay for usage and subscription plans.
    | [Identity 🆔 agent](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) | To authenticate the domain user.
    | [Folder 🗂️ editor](<../../20 🧑‍🦰 UI/26 🗂️ Folders/01 🗂️ Folder editor.md>) | To manage the settings of the hosted [domain 👥](<00 👥 Domain.md>).

    ---
    <br/>

4. **How can a domain admin user leverage a [🧑‍💻 Hoster](<04 🧑‍💻🛠️ Hoster helper.md>)?**

    |#| Category | Step
    |-|-|-
    |1| `Find` | Using their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), <br/>the admin user [finds 🔎](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) a [Hoster 🧑‍💻 domain](<04 🧑‍💻🛠️ Hoster helper.md>) <br/>and starts a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) with the [Hoster's Host 🤗 role](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>).
    |2| `Bind`| On the [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>), <br/>the user [Binds 🔗](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) to the [Hoster's Vault 🗄️ role](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>), <br/>and creates a new [domain 👥](<00 👥 Domain.md>).
    |3| `Clone`| On a workstation terminal, <br/>the user [scans ✨](<../../20 🧑‍🦰 UI/22 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>) the terminal QR code <br/>to link the terminal to the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)<br/>and download the [domain 👥](<00 👥 Domain.md>) settings.
    |4| `Edit`| On a code editor (e.g., Visual Studio Code)<br/>the user configures the logic webhooks <br/>and the public [domain 📜 Manifest](<01 📜 Domain Manifest.md>).
    |5| `Sync`| On the workstation terminal, <br/>the user synchronizes the changes <br/>with the [Hoster 🧑‍💻 domain](<04 🧑‍💻🛠️ Hoster helper.md>).
    |6| `Test`| From the workstation terminal, <br/>the user runs automated tests <br/> and opens [Chats 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) for manual testing.

    ---
    <br/>


5. **What does the Wallet Chat looks like?**

    | Service | Prompt  | User 
    | - | - | - 
    | | | 🤵 [Broker](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
    | 🤵 [Broker](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 😃 Hi! What do you need? | `hoster`
    | 🤵 [Broker](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 💬 How can I help? <br/> - Open [ 🧭 Navigator ] <br/> - [ Something else ] | > 🧭 Navigator 
    | 🤵 [Broker](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | ✅ Over to 🧭 Navigator.
    | [ new chat ]
    | 🔎 [Finder](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Navigator (4.4 ⭐) [+]
    | 🧭 [Navigator](<../../30 🫥 Agents/07 🧭 Navigators/05 🧭🫥 Navigator agent.md>) | ℹ️ Request: return to hotel [+]
    | 🧭 [Navigator](<../../30 🫥 Agents/07 🧭 Navigators/05 🧭🫥 Navigator agent.md>) | 😃 Go to `Any Hotel`? [Yes, No]| > Yes
    | ...
    
    ---
    <br/>

6. **What commands are supported on the Terminal?**

    |🧑‍💻 Command | Description
    |-|-
    |`clone <name>` | Generates a [QR Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>)<br> for the user to scan with the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)<br/>to clone the [domain 👥](<00 👥 Domain.md>) to a local folder<br/>- e.g., `my-hoster clone my-domain`
    |`sync` | Sends the changes with the [Hoster 🧑‍💻 domain](<04 🧑‍💻🛠️ Hoster helper.md>) <br/>- e.g., `my-hoster sync`
    |`test <env>`| Runs test scripts on an environment<br/>- e.g., `my-hoster test local`
    |`chat <env>`| Opens a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) with an environment<br/>on the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)<br/>- e.g., `my-hoster chat local`

    ---
    <br/>

7. **What does a Terminal interaction looks like?**

    |🧑‍💻 Command | 🖥️ Display |  Workstation
    |-|-|-
    |`$ clone my-domain` | ⏳ Scan the QR code... | [✨ scan](<../../20 🧑‍🦰 UI/22 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>)
    || ✅ Domain cloned to folder
    |`code .` | &lt;opens visual studio code&gt;| 🧑‍💻 implement
    |`$ sync` | ✅ Changes synchronized.
    |`$ test dev` | ✅ Tested successfully. | 🥳 celebrate
    |`$ chat dev` | ⏳ Chat on your Wallet... | [💬 chat](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>)
    || ✅ Chat finished. | 
    |`$ chat prod` | ⏳ Chat on your Wallet... | [💬 chat](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>)
    || ✅ Chat finished. | 
    
    

    ---
    <br/>


