# 🤗⏩🧑‍🦰 Inform 📝

* Shows user instructions and allow inputs.
    * [Brokers 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) may ask for [user confirmation  👍](<../../../35 💬 Chats/🤔 Prompts/🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>) the first time,
    * then switch to a [non-blocking info ℹ️](<../../../35 💬 Chats/🤔 Prompts/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>).

* Related to:
    * [📝 Talker `INFORM` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...methods 🤵/INFORM 📝/INFORM 📝 msg.md>)

* Examples:
    * [Buy hot dog 🌭](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/21 🎪 Stall: Buy hot dog 🌭.md>)
    * [Book restaurant table 🗓️](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)

<br/>

## 💬 Chat


| [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| 🤵 [Broker](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 Ready to order? [Yes, No] <br/> - your curator orders 🧚<br/>  - your payer pays the bill 💳  | > Yes
|

<br/>

Here's the [Talker 😃](<../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>).

```yaml
# Talker
- INFORM|TableOrder
```

| [Command ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | Purpose
|-|-
| 📝 [`INFORM`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...methods 🤵/INFORM 📝/INFORM 📝 msg.md>) | Show user instructions and allow inputs.
|

<br/>

Here's the [Manifest 📜](<../../../30 🧩 Data/Manifests 📜/📜 Manifest.md>).
```yaml
Forms:
  TableOrder:
    Verb: order
    Steps:
      - Schema: .CURATOR/FILTER
        Purpose: your curator orders 🧚
      - Schema: .PAYER/CHARGE
        Purpose: your payer pays the bill 💳  
```

<br/>

## ⏩ Flow diagram

![alt text](<../.📎 Assets/⚙️📝 Inform.png>)


| # | Call | Description
|-|-|-
|1|[💼🐌🤵 `Query@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/🤵 Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [Consumers 💼](<../💼🎭 Consumer role.md>) ask for [Schema Codes 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|2|[🤗⏩🧑‍🦰 Prompt 🤔](<../../Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) reject non-announced asks
|3|[💼🐌🤵 `Inform@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/🤵 Share 💼 Inform 💼🐌🤵/🤵 Inform 🐌 msg.md>) | [Consumers 💼](<../💼🎭 Consumer role.md>) inform the upcoming form 
|4|[👥🚀🕸 `Form@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Form.md>) | [Brokers 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) get the form [Schema Codes 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|5|[🤗⏩🧑‍🦰 Prompt 🤔](<../../Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) inform the user on the steps
|6|[💼🐌🤵 `Query@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/🤵 Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [Consumers 💼](<../💼🎭 Consumer role.md>) ask for [Schema Codes 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|7|[🤵🐌🗄️ `Disclose@Broker`](<../../Vaults 🗄️/🗄️🅰️ Vault methods/Disclose/🤵🐌🗄️ Disclose.md>) | [Brokers 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) ask [Vaults 🗄️](<../../Vaults 🗄️/🗄️🎭 Vault role.md>) to disclose
|