# 💼⏩🧑‍🦰 Query a Vault @ Consumer

> In a [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>), a [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>)  can query user data.

> Implements the [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>).

<br/>

## Flow diagram

![alt text](<../../.📎 Assets/Binds 📎/⚙️ Share Bind.png>)

|#|Step|Purpose
|-|-|-
|1|[💼🐌🤵 `Query@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [Consumers 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) ask for [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|2|[👥🚀🕸 `Queryable@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Queryable.md>) | [Brokers 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) match [Trusted 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) [Vaults 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) 
|3|[👥🚀🕸 `Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | [Brokers 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) translate [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|4|[🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Brokers 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) ask which [Vault 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) if many
|5|[🤵🐌🗄️ `Disclose@Broker`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>) | [Brokers 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) ask the [Vault 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) to disclose
|6|[🗄️🚀💼 `Context@Consumer`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Context 🗄️🚀💼/💼 Context 🚀 request.md>) | [Vaults 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) ask for the request's context
|7|[🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Vaults 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) ask users for additional info
|8|[🗄️⏩💼 Consume 🧩](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️⏩ Vault flows/Consume 🗄️⏩💼/🗄️ Consume ⏩ flow.md>) | [Vaults 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) share the user's data
|

<br/>
