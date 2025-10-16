# 🗄️⏩🧑‍🦰 Engage @ Vault

> Used by [🔃⏩🗃️ Chat @ Syncer](<../../../../5 ⏩ Flows/77 🔃⏩ Syncer/30 🔃⏩🗃️ Chat.md>)

* Allows for [Vault 🗄️ domains](<../🗄️🎭 Vault role.md>) 
    * to proactively start a new [Chat 💬](<../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) 
    * with a [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) previously [bound 🔗](<../../../30 🧩 Data/20 🔗 Binds/🔗 Bind.md>)
    * in the best interest of the user.

<br/>


## Chat

| [Domain](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🔎 [Finder](<../../../50 🫥 Agent domains/40 🔎 Finders/🔎🫥 Finder agent.md>) | ⓘ Any Vault (4.4 ⭐) [+]
| 🤵 [Broker](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | ⓘ Bind: Any Bind 🔗 [+]
| 🗄️ [Vault](<../🗄️🎭 Vault role.md>) | ℹ️ Context: Any Locator 🔆 [+]
| 🗄️ [Vault](<../🗄️🎭 Vault role.md>) | 😃 Need help with this? [Yes, No] | > Yes
||

<br/>

## Flow diagram

![alt text](<../.📎 Assets/⚙️🧑‍🦰 Engage.png>)

|#|Step|Purpose
|-|-|-
|1| [🗄️🐌🤵 `Engage@Broker`](<../../../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/30 🗄️🐌🤵 Engage.md>) | [Vaults 🗄️](<../🗄️🎭 Vault role.md>) present a [Bind 🔗](<../../../30 🧩 Data/20 🔗 Binds/🔗 Bind.md>)
| 2 | [🤵⏩🧑‍🦰 Assess 🔆](<../../../../5 ⏩ Flows/10 🤵⏩ Brokers/01 🤵⏩🧑‍🦰 Assess 🔆.md>) | [Brokers 🤵](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) open a [Chat 💬](<../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)  on the [Wallet 🧑‍🦰](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) 
|3|[🤵🐌🤗 `Hello@Host`](<../../30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>) | [Brokers 🤵](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) hand it over to [Hosts 🤗](<../../30 🤗 Hosts/🤗🎭 Host role.md>)
|4|[🤗⏩🧑‍🦰 Prompt ℹ️](<../../30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Hosts 🤗](<../../30 🤗 Hosts/🤗🎭 Host role.md>) provide context
|4|[🤗⏩🧑‍🦰 Prompt 😃](<../../30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Hosts 🤗](<../../30 🤗 Hosts/🤗🎭 Host role.md>) ask users for an action
|