# 🗄️⏩🧑‍🦰 Engage @ Vault

> Used by [🔃⏩🗃️ Chat @ Syncer](<../../../90 👷 Build/2 🛠️ Syncers/🔃⏩ Syncer flows/30 🔃⏩🗃️ Chat.md>)

* Allows for [Vault 🗄️ domains](<../🗄️🎭 Vault role.md>) 
    * to proactively start a new [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>) 
    * with a [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) previously [bound 🔗](<../../../30 Data/2 🔗 Binds/🔗 Bind.md>)
    * in the best interest of the user.

<br/>


## Chat

| [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🔎 [Finder](<../../../50 🫥 Agent domains/40 🔎 Finders/🔎🫥 Finder agent.md>) | ⓘ Any Vault (4.4 ⭐) [+]
| 🤵 [Broker](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) | ⓘ Bind: Any Bind 🔗 [+]
| 🗄️ [Vault](<../🗄️🎭 Vault role.md>) | ℹ️ Context: Any Locator 🔆 [+]
| 🗄️ [Vault](<../🗄️🎭 Vault role.md>) | 😃 Need help with this? [Yes, No] | > Yes
||

<br/>

## Flow diagram

![alt text](<../.📎 Assets/⚙️🧑‍🦰 Engage.png>)

|#|Step|Purpose
|-|-|-
|1| [🗄️🐌🤵 `Engage@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Engage.md>) | [Vaults 🗄️](<../🗄️🎭 Vault role.md>) present a [Bind 🔗](<../../../30 Data/2 🔗 Binds/🔗 Bind.md>)
| 2 | [🤵⏩🧑‍🦰 Assess 🔆](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵⏩ Broker flows/🤵⏩🧑‍🦰 Assess 🔆.md>) | [Brokers 🤵](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) open a [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>)  on the [Wallet 🧑‍🦰](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) 
|3|[🤵🐌🤗 `Hello@Host`](<../../30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>) | [Brokers 🤵](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) hand it over to [Hosts 🤗](<../../30 🤗 Hosts/🤗🎭 Host role.md>)
|4|[🤗⏩🧑‍🦰 Prompt ℹ️](<../../30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Hosts 🤗](<../../30 🤗 Hosts/🤗🎭 Host role.md>) provide context
|4|[🤗⏩🧑‍🦰 Prompt 😃](<../../30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Hosts 🤗](<../../30 🤗 Hosts/🤗🎭 Host role.md>) ask users for an action
|