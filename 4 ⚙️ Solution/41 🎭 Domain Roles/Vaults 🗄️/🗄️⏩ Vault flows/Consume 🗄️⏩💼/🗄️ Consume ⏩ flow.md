# 🗄️⏩💼 Consume @ Vault

> Used in [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Bind 👉🔗💼/🧑‍🦰 Share Bind ⏩ flow.md>) flow.
 
<br/>

## Flow diagram

![alt text](<🗄️ Consume ⚙️ uml.png>)


|#|Step|Purpose
|-|-|-
|1|[👥🚀🕸 `Trusts@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>) | [Vaults 🗄️](<../../🗄️ Vault/🗄️🎭 Vault role.md>) see if [Consumers 💼](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) are [Trusted 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>)  
|2|[🗄️🐌💼 `Consume@Consumer`](<../../../Consumers 💼/💼📨 Consumer msgs/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>) | [Vaults 🗄️](<../../🗄️ Vault/🗄️🎭 Vault role.md>) tell [Consumers 💼](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) they're ready
|3|[👥🚀🕸 `Trusts@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>) | [Consumers 💼](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) see if [Vaults 🗄️](<../../🗄️ Vault/🗄️🎭 Vault role.md>) are [Trusted 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>)
|4|[💼🚀🗄️ `Collect@Vault`](<../../🗄️📨 Vault msgs/Collect 💼🚀🗄️/🗄️ Collect 🚀 call.md>) | [Consumers 💼](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) collect the data shared
|

<br/> 


## FAQ

1. **Why do Consumers and Vaults check Trusts again?**

    `Liability` [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) do not assume legal responsibility for orchestration faults.
    * [Broker 🤵 domains](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) can be compromised or make mistakes.
    * [Vault 🗄️ domains](<../../🗄️ Vault/🗄️🎭 Vault role.md>) are ultimately responsible for data breaches.
    * [Consumer 💼 domains](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) are ultimately responsible for interacting with banned entities (e.g., entities listed as terrorist groups).
    * [Consumer 💼 domains](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) and [Vault 🗄️ domains](<../../🗄️ Vault/🗄️🎭 Vault role.md>) should revalidate the [Trust 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) path for their own protection whenever feasible.

    

    ---
    <br/>

1. **Why Consume+Collect instead of a single call?**

    `Time` [Vault 🗄️ domains](<../../🗄️ Vault/🗄️🎭 Vault role.md>) may need time to gather the data, from seconds to days.
    * Thus, [Consumer 💼 domains](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) need to wait for [Vault 🗄️ domains](<../../🗄️ Vault/🗄️🎭 Vault role.md>) to notify them when the data is ready.
    * This is the [`Consume@Consumer`](<../../../Consumers 💼/💼📨 Consumer msgs/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>) call.

    `Size` Pushing a payload has size limits, while downloading it doesn't.
    * Thus, to allow [Consumer 💼 domains](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) to download data sets from [Vault 🗄️ domains](<../../🗄️ Vault/🗄️🎭 Vault role.md>) via with no theoretical size limit, the request needs to come from the [Consumer 💼 domain](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) (and not from the [Vault 🗄️ domain](<../../🗄️ Vault/🗄️🎭 Vault role.md>)).
    * This is the [`Collect@Vault`](<../../🗄️📨 Vault msgs/Collect 💼🚀🗄️/🗄️ Collect 🚀 call.md>) call.

    ---