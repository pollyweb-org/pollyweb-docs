# 🤗⏩🧑‍🦰 Form 📝

* Shows user instructions and allow inputs.
    * [Brokers 🤵](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) may ask for [user confirmation  👍](<../../../9 😃 Talkers/20 🤔 Prompts/7 ✏️ Input prompts/31 👍 CONFIRM prompt.md>) the first time,
    * then switch to a [non-blocking info ℹ️](<../../../9 😃 Talkers/20 🤔 Prompts/4 ⚠️ Status prompts/21 ℹ️ INFO prompt.md>).

* Related to:
    * [📝 Talker `INFORM` command](<../../../9 😃 Talkers/60 ⏩ Msg flows/41 📝 INFORM msg.md>)

* Examples:
    * [Buy hot dog 🌭](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/21 🎪 Stall: Buy hot dog 🌭.md>)
    * [Book restaurant table 🗓️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)

<br/>

## 💬 Chat


| [Domain](<../../40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🤵 [Broker](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Ready to order? [Yes, No] <br/> - your curator orders 🧚<br/>  - your payer pays the bill 💳  | > Yes
|

<br/>

Here's the [Talker 😃](<../../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>).

```yaml
# Talker
- INFORM|TableOrder
```

| [Command ⌘](<../../../9 😃 Talkers/40 🌊 Talker flows/10 ⌘ Command.md>) | Purpose
|-|-
| 📝 [`INFORM`](<../../../9 😃 Talkers/60 ⏩ Msg flows/41 📝 INFORM msg.md>) | Show user instructions and allow inputs.
|

<br/>

Here's the [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>).
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

![alt text](<.📎 Assets/⚙️📝 Inform.png>)


| # | Call | Description
|-|-|-
|1|[💼🐌🤵 `Query@Broker`](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>) | [Consumers 💼](<$ 💼🎭 Consumer role.md>) ask for [Schema Codes 🧩](<../../25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>)
|2|[🤗⏩🧑‍🦰 Prompt 🤔](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) reject non-announced asks
|3|[💼🐌🤵 `Inform@Broker`](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/65 💼🐌🤵 Inform.md>) | [Consumers 💼](<$ 💼🎭 Consumer role.md>) inform the upcoming form 
|4|[👥🚀🕸 `Form@Graph`](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/01 👥🚀🕸 Form.md>) | [Brokers 🤵](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) get the form [Schema Codes 🧩](<../../25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>)
|5|[🤗⏩🧑‍🦰 Prompt 🤔](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) inform the user on the steps
|6|[💼🐌🤵 `Query@Broker`](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>) | [Consumers 💼](<$ 💼🎭 Consumer role.md>) ask for [Schema Codes 🧩](<../../25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>)
|7|[🤵🐌🗄️ `Disclose@Broker`](<../../../6 🅰️ APIs/95 🗄️🅰️ Vault/03 🤵🐌🗄️ Disclose.md>) | [Brokers 🤵](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) ask [Vaults 🗄️](<../80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) to disclose
|