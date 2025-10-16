# 🤗⏩🧑‍🦰 Form 📝

* Shows user instructions and allow inputs.
    * [Brokers 🤵](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) may ask for [user confirmation  👍](<../../../35 Chats/20 🤔 Prompts/7 ✏️ Input prompts/31 👍 CONFIRM prompt.md>) the first time,
    * then switch to a [non-blocking info ℹ️](<../../../35 Chats/20 🤔 Prompts/4 ⚠️ Status prompts/21 ℹ️ INFO prompt.md>).

* Related to:
    * [📝 Talker `INFORM` command](<../../../../9 😃 Talkers/😃📨 Talker msgs/41 📝 INFORM msg.md>)

* Examples:
    * [Buy hot dog 🌭](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/21 🎪 Stall: Buy hot dog 🌭.md>)
    * [Book restaurant table 🗓️](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)

<br/>

## 💬 Chat


| [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 Chats/20 🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🤵 [Broker](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Ready to order? [Yes, No] <br/> - your curator orders 🧚<br/>  - your payer pays the bill 💳  | > Yes
|

<br/>

Here's the [Talker 😃](<../../../../9 😃 Talkers/10 😃 Talker.md>).

```yaml
# Talker
- INFORM|TableOrder
```

| [Command ⌘](<../../../../9 😃 Talkers/😃🌊 Talker flow/10 ⌘ Command.md>) | Purpose
|-|-
| 📝 [`INFORM`](<../../../../9 😃 Talkers/😃📨 Talker msgs/41 📝 INFORM msg.md>) | Show user instructions and allow inputs.
|

<br/>

Here's the [Manifest 📜](<../../../40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>).
```yaml
Forms:
  TableOrder:
    Verb: order
    Steps:
      - Code: .CURATOR/FILTER
        Purpose: your curator orders 🧚
      - Code: .PAYER/CHARGE
        Purpose: your payer pays the bill 💳  
```

<br/>

## ⏩ Flow diagram

![alt text](<../.📎 Assets/⚙️📝 Inform.png>)


| # | Call | Description
|-|-|-
|1|[💼🐌🤵 `Query@Broker`](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/60 🤵🅰️ Share/💼🐌🤵 Query.md>) | [Consumers 💼](<../💼🎭 Consumer role.md>) ask for [Schema Codes 🧩](<../../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)
|2|[🤗⏩🧑‍🦰 Prompt 🤔](<../../30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) reject non-announced asks
|3|[💼🐌🤵 `Inform@Broker`](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/60 🤵🅰️ Share/💼🐌🤵 Inform.md>) | [Consumers 💼](<../💼🎭 Consumer role.md>) inform the upcoming form 
|4|[👥🚀🕸 `Form@Graph`](<../../../45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Form.md>) | [Brokers 🤵](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) get the form [Schema Codes 🧩](<../../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)
|5|[🤗⏩🧑‍🦰 Prompt 🤔](<../../30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) inform the user on the steps
|6|[💼🐌🤵 `Query@Broker`](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/60 🤵🅰️ Share/💼🐌🤵 Query.md>) | [Consumers 💼](<../💼🎭 Consumer role.md>) ask for [Schema Codes 🧩](<../../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)
|7|[🤵🐌🗄️ `Disclose@Broker`](<../../80 🗄️ Vaults/🗄️🅰️ Vault methods/🤵🐌🗄️ Disclose.md>) | [Brokers 🤵](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) ask [Vaults 🗄️](<../../80 🗄️ Vaults/🗄️🎭 Vault role.md>) to disclose
|