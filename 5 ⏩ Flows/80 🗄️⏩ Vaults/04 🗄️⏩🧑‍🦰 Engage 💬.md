# 🗄️⏩🧑‍🦰 Engage @ Vault

> Used by [🔃⏩🗃️ Chat @ Syncer](<../77 🔃⏩ Syncer/30 🔃⏩🗃️ Chat.md>)

* Allows for [Vault 🗄️ domains](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) 
    * to proactively start a new [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) 
    * with a [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) previously [bound 🔗](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/01 🔗 Bind.md>)
    * in the best interest of the user.

<br/>


## Chat

| [Domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🔎 [Finder](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Vault (4.4 ⭐) [+]
| 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Bind: Any Bind 🔗 [+]
| 🗄️ [Vault](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) | ℹ️ Context: Any Locator 🔆 [+]
| 🗄️ [Vault](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) | 😃 Need help with this? [Yes, No] | > Yes
||

<br/>

## Flow diagram

![alt text](<.📎 Assets/⚙️🧑‍🦰 Engage.png>)

|#|Step|Purpose
|-|-|-
|1| [🗄️🐌🤵 `Engage@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/30 🗄️🐌🤵 Engage.md>) | [Vaults 🗄️](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) present a [Bind 🔗](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/01 🔗 Bind.md>)
| 2 | [🤵⏩🧑‍🦰 Assess 🔆](<../10 🤵⏩ Brokers/01 🤵⏩🧑‍🦰 Assess 🔆.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) open a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)  on the [Wallet 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) 
|3|[🤵🐌🤗 `Hello@Host`](<../../6 🅰️ APIs/50 🤗🅰️ Host/01 🤵🐌🤗 Hello.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) hand it over to [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>)
|4|[🤗⏩🧑‍🦰 Prompt ℹ️](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) provide context
|4|[🤗⏩🧑‍🦰 Prompt 😃](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) ask users for an action
|