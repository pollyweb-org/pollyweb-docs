# 💼⏩🧑‍🦰 Inform 📝

> Purpose 
* Shows user instructions and allow inputs.
    * [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) may ask for [user confirmation  👍](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>) the first time,
    * then switch to a [non-blocking info ℹ️](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>).

> Related to
* [📝 Talker `INFORM` command](<../../💼⌘ Consumer cmds/INFORM 📝/📝 INFORM ⌘ cmd.md>)

> Examples
  * [Buy hot dog 🌭](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/21 🎪 Stall: Buy hot dog 🌭.md>)
  * [Book restaurant table 🗓️](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)

<br/>

## 💬 Chat


| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 Ready to order? [Yes, No] <br/> - your curator orders 🧚<br/>  - your payer pays the bill 💳  | > Yes
|

<br/>

Here's the [`Script`](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

```yaml
# Talker
- INFORM: TableOrder
```

| [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
|-|-
| 📝 [`INFORM`](<../../💼⌘ Consumer cmds/INFORM 📝/📝 INFORM ⌘ cmd.md>) | Show user instructions and allow inputs.
|

<br/>

Here's the [Manifest 📜](<../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>).
```yaml
Forms:
  TableOrder:
    Title: Order a meal
    Steps:
      - Schema: .CURATOR/CURATE
        Purpose: your curator orders 🧚
      - Schema: .PAYER/CHARGE
        Purpose: your payer pays the bill 💳  
```

<br/>

## ⏩ Flow diagram

![alt text](<💼 Inform ⚙️ uml.png>)


| # | Call | Description
|-|-|-
|1|[💼🐌🤵 `Query@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [Consumers 💼](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) ask for [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|2|[🤗⏩🧑‍🦰 Prompt 🤔](<../../../Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) reject non-announced asks
|3|[💼🐌🤵 `Inform@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Inform 💼🐌🤵/🤵 Inform 🐌 msg.md>) | [Consumers 💼](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) inform the upcoming form 
|4|[👥🚀🕸 `Form@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Form/🕸 Form 🚀 call.md>) | [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) get the form [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|5|[🤗⏩🧑‍🦰 Prompt 🤔](<../../../Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) inform the user on the steps
|6|[🤵🐌💼 `Informed@Consumer`](<../../💼📨 Consumer msgs/Informed 🤵🐌💼/💼 Informed 🐌 msg.md>) | [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) tell [Consumers 💼](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) to continue
|7|[💼🐌🤵 `Query@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [Consumers 💼](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) ask for [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|8|[🤵🐌🗄️ `Disclose@Broker`](<../../../Vaults 🗄️/🗄️📨 Vault msgs/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>) | [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) ask [Vaults 🗄️](<../../../Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) to disclose
|