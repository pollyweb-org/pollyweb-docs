# 👉 Share vault

> In a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>), a [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>)  can query user data.

> Implements [Consumer 💼 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>)

<br/>

## Flow diagram

![alt text](<.📎 Assets/⚙️ Query Vault.png>)

|#|Step|Purpose
|-|-|-
|1|[💼🐌🤵 Query @ Broker](<../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>) | [Consumers 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) ask for [Schema Codes 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
|2|[👥🚀🕸 Queryable @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/05 👥🚀🕸 Queryable.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) match [Trusted 👍](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>) [Vaults 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) 
|3|[👥🚀🕸 Translate @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/06 👥🚀🕸 Translate.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) translate [Schema Codes 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
|4|[🤗⏩🧑‍🦰 Prompt @ Host](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) ask wish [Vault 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) if many
|5|[🤵🐌🗄️ Disclose @ Broker](<../../6 🅰️ APIs/95 🗄️🅰️ Vault/03 🤵🐌🗄️ Disclose.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) ask the [Vault 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) to disclose
|6|[👥🚀🕸 Trusts @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/03 👥🚀🕸 Trusts.md>) | [Vaults 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) see if [Consumer 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) is [Trusted 👍](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>)
|7|[🤗⏩🧑‍🦰 Prompt @ Host](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | [Vaults 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) ask users for additional info
|8|[🗄️🐌💼 Consume @ Consumer](<../../6 🅰️ APIs/30 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>) | [Vaults 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) tell [Consumers 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) they're ready
|9|[👥🚀🕸 Trusts @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/03 👥🚀🕸 Trusts.md>) | [Consumers 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) see if [Vault 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) is [Trusted 👍](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>)
|10|[💼🚀🗄️ Collect @ Vault](<../../6 🅰️ APIs/95 🗄️🅰️ Vault/01 💼🚀🗄️ Collect.md>) | [Consumers 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) collect the data shared
|

<br/>

## FAQ

1. **Why do Consumers and Vaults check Trusts again?**

    `Liability` [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) do not assume legal responsibility for orchestration faults.
    * [Broker 🤵 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) can be compromised or make mistakes.
    * [Vault 🗄️ domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) are ultimately responsible for data breaches.
    * [Consumer 💼 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) are ultimately responsible for interacting with banned entities (e.g., entities listed as terrorist groups).
    * [Consumer 💼 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) and [Vault 🗄️ domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) should revalidate the [Trust 👍](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>) path for their own protection whenever feasible.

    

    ---
    <br/>

2. **Why Consume+Collect instead of a single call?**

    `Time` [Vault 🗄️ domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) may need time to gather the data, from seconds to days.
    * Thus, [Consumer 💼 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) need to wait for [Vault 🗄️ domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) to notify them when the data is ready.
    * This is the [Consume @ Consumer](<../../6 🅰️ APIs/30 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>) call.

    `Size` Pushing a payload has size limits, while downloading it doesn't.
    * Thus, to allow [Consumer 💼 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) to download data sets from [Vault 🗄️ domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) via with no theoretical size limit, the request needs to come from the [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) (and not from the [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)).
    * This is the [Collect @ Vault](<../../6 🅰️ APIs/95 🗄️🅰️ Vault/01 💼🚀🗄️ Collect.md>) call.

    ---