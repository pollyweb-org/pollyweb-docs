# 🗄️⏩🧑‍🦰 Engage @ Vault

> Used by [🔃⏩🗂️ Chat @ Syncer](<../../../../55 👷 Build domains/Syncers 🔃/🔃⏩ Syncer flows/30 🔃⏩🗂️ Chat.md>)

* Allows for [Vault 🗄️ domains](<../../🗄️ Vault/🗄️🎭 Vault role.md>) 
    * to proactively start a new [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) 
    * with a [Wallet 🧑‍🦰 app](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) previously [bound 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
    * in the best interest of the user.


## Chat

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🔎 [Finder](<../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Vault (4.4 ⭐) [+]
| 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ⓘ Bind: Any Bind 🔗 [+]
| 🗄️ [Vault](<../../🗄️ Vault/🗄️🎭 Vault role.md>) | ℹ️ Context: Any Locator 🔆 [+]
| 🗄️ [Vault](<../../🗄️ Vault/🗄️🎭 Vault role.md>) | 😃 Need help with this? [Yes, No] | > Yes
||

<br/>

## Flow diagram

![alt text](<🗄️ Engage ⚙️ uml.png>)

|#|Step|Purpose
|-|-|-
|1| [🗄️🐌🤵 `Engage@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Binds 🔗 Engage 🗄️🐌🤵/🤵 Engage 🐌 msg.md>) | [Vaults 🗄️](<../../🗄️ Vault/🗄️🎭 Vault role.md>) present a [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
| 2 | [🤵⏩🧑‍🦰 Locate 🔆](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵⏩ Broker flows/Locate 🔆⏩🤵/🤵 Locate ⏩ flow.md>) | [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) open a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)  on the [Wallet 🧑‍🦰](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) 
|3|[🤵🐌🤗 `Hello@Host`](<../../../Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) | [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) hand it over to [Hosts 🤗](<../../../Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>)
|4|[🤗⏩🧑‍🦰 Prompt ℹ️](<../../../Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Hosts 🤗](<../../../Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) provide context
|4|[🤗⏩🧑‍🦰 Prompt 😃](<../../../Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Hosts 🤗](<../../../Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) ask users for an action
|