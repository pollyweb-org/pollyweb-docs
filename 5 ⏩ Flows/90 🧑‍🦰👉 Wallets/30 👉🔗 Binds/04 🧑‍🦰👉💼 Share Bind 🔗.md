# 💼⏩🧑‍🦰 Query a Vault @ Consumer

> In a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>), a [Consumer 💼 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>)  can query user data.

> Implements the [Consumer 💼 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>).

<br/>

## Flow diagram

![alt text](<.📎 Assets/⚙️ Share Bind.png>)

|#|Step|Purpose
|-|-|-
|1|[💼🐌🤵 `Query@Broker`](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>) | [Consumers 💼](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) ask for [Schema Codes 🧩](<../../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>)
|2|[👥🚀🕸 `Queryable@Graph`](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/05 👥🚀🕸 Queryable.md>) | [Brokers 🤵](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) match [Trusted 👍](<../../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) [Vaults 🗄️](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) 
|3|[👥🚀🕸 `Translate@Graph`](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/06 👥🚀🕸 Translate.md>) | [Brokers 🤵](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) translate [Schema Codes 🧩](<../../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>)
|4|[🤗⏩🧑‍🦰 Prompt 🤔](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔 flow.md>) | [Brokers 🤵](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) ask which [Vault 🗄️](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) if many
|5|[🤵🐌🗄️ `Disclose@Broker`](<../../../6 🅰️ APIs/95 🗄️🅰️ Vault/03 🤵🐌🗄️ Disclose.md>) | [Brokers 🤵](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) ask the [Vault 🗄️](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) to disclose
|6|[🗄️🚀💼 `Context@Consumer`](<../../../6 🅰️ APIs/30 💼🅰️ Consumer/01 🗄️🚀💼 Context.md>) | [Vaults 🗄️](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) ask for the request's context
|7|[🤗⏩🧑‍🦰 Prompt 🤔](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔 flow.md>) | [Vaults 🗄️](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) ask users for additional info
|8|[🗄️⏩💼 Consume 🧩](<../../80 🗄️⏩ Vaults/02 🗄️⏩💼 Consume 🔗.md>) | [Vaults 🗄️](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) share the user's data
|

<br/>
