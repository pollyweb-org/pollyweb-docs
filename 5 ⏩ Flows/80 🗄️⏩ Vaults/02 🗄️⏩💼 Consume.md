# 🗄️⏩💼 Consume @ Vault

> Used in [💼⏩🧑‍🦰 Query Vault @ Consumer](<../90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind.md>) flow.
 
<br/>

## Flow diagram

![alt text](<.📎 Assets/⚙️ Consume.png>)


|#|Step|Purpose
|-|-|-
|1|[👥🚀🕸 Trusts @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/03 👥🚀🕸 Trusts.md>) | [Vaults 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) see if [Consumers 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) are [Trusted 👍](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>)  
|2|[🗄️🐌💼 Consume @ Consumer](<../../6 🅰️ APIs/30 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>) | [Vaults 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) tell [Consumers 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) they're ready
|3|[👥🚀🕸 Trusts @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/03 👥🚀🕸 Trusts.md>) | [Consumers 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) see if [Vaults 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) are [Trusted 👍](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>)
|4|[💼🚀🗄️ Collect @ Vault](<../../6 🅰️ APIs/95 🗄️🅰️ Vault/01 💼🚀🗄️ Collect.md>) | [Consumers 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) collect the data shared
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

1. **Why Consume+Collect instead of a single call?**

    `Time` [Vault 🗄️ domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) may need time to gather the data, from seconds to days.
    * Thus, [Consumer 💼 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) need to wait for [Vault 🗄️ domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) to notify them when the data is ready.
    * This is the [Consume @ Consumer](<../../6 🅰️ APIs/30 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>) call.

    `Size` Pushing a payload has size limits, while downloading it doesn't.
    * Thus, to allow [Consumer 💼 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) to download data sets from [Vault 🗄️ domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) via with no theoretical size limit, the request needs to come from the [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) (and not from the [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)).
    * This is the [Collect @ Vault](<../../6 🅰️ APIs/95 🗄️🅰️ Vault/01 💼🚀🗄️ Collect.md>) call.

    ---