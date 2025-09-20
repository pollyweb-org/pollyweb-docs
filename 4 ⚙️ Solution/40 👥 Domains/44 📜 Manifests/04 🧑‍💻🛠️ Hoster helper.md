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
    | [Payer 💳](<../../30 🫥 Agents/04 💳 Payers/04 💳🫥 Payer agent.md>) | To pay for usage and subscription plans.
    | [Folder 🗂️](<../../20 🧑‍🦰 UI/26 🗂️ Folders/01 🗂️ Folder editor.md>) | To manage the settings of the hosted [domain 👥](<00 👥 Domain.md>).
    | [Identity 🆔](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) | To authenticate the domain user.
    


    ---
    <br/>

4. **How can an admin user leverage a [🧑‍💻 Hoster](<04 🧑‍💻🛠️ Hoster helper.md>)?**

    |#| Category | Step
    |-|-|-
    |1| `Find` | Using their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), the user [finds 🔎](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) a [Hoster 🧑‍💻 domain](<04 🧑‍💻🛠️ Hoster helper.md>) and starts a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) with the [Hoster's Host 🤗 role](<../../20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>).
    |2| `Bind`| On the [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>), the user [Binds 🔗](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) to the [Hoster's Vault 🗄️ role](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>).
    |3| `Create` | The user creates a new [domain 👥](<00 👥 Domain.md>), and the [Hoster 🧑‍💻 domain](<04 🧑‍💻🛠️ Hoster helper.md>) returns a random domain name - e.g., `<any-uuid>.domains.any-host.com`
    |4| `Config`| The user uses their [Folder 🗂️ editor](<../../20 🧑‍🦰 UI/26 🗂️ Folders/01 🗂️ Folder editor.md>) to configure the [domain 📜 Manifest](<01 📜 Domain Manifest.md>) of the newly created [domain 👥](<00 👥 Domain.md>).

    ---
    <br/>