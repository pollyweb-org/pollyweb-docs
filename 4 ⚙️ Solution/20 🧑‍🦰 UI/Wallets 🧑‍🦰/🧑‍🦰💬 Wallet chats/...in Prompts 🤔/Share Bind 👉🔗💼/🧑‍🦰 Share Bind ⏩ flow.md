# 💼⏩🧑‍🦰 Share Bind

> In a [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>), a [Consumer 💼 domain](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>)  can query user data.

> Implements the [Consumer 💼 domain](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>).

<br/>

## 💬 Chat 

Consider the following [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

|Service|Prompt|User
| - | - | - |
| ☕ Café     | 😃 What's your name?
| 🤵 [Broker](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 Which vault to use? <br/> - [ 🧢 Any Persona ]<br/>- [ 🧢 Other Persona ] | > 🧢 Any Persona
| 🧢 [Persona](<../../../../../50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>) | 🫥 Share name? [Yes, No] | > Yes
| ☕ Café     | ✅ Hi, Alice!
|

<br/> 

## Flow diagram

![alt text](<🧑‍🦰 Share Bind ⚙️ uml.png>)

|#|Step|Purpose
|-|-|-
|1|[💼🐌🤵 `Query@Broker`](<../../../../Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [Consumers 💼](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) ask for [Schema Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|2|[👥🚀🕸 `Queryable@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Queryable/🕸 Queryable 🚀 call.md>) | [Brokers 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) match [Trusted 🫡](<../../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) [Vaults 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) 
|3|[👥🚀🕸 `Translate@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>) | [Brokers 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) translate [Schema Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|4|[🤗⏩🧑‍🦰 Prompt 🤔](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Brokers 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) ask which [Vault 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) if many
|5|[🤵🐌🗄️ `Disclose@Broker`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️📨 Vault msgs/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>) | [Brokers 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) ask the [Vault 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) to disclose
|6|[🗄️🚀💼 `Queried@Consumer`](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Queried 🗄️🚀💼/💼 Queried 🚀 call.md>) | [Vaults 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) ask for the request's context
|7|[🤗⏩🧑‍🦰 Prompt 🤔](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Vaults 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) ask users for additional info
|8|[🗄️⏩💼 Consume 🧩](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️⏩ Vault flows/Consume 🗄️⏩💼/🗄️ Consume ⏩ flow.md>) | [Vaults 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) share the user's data
|

<br/>
