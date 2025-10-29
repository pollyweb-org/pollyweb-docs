# 🗄️🚀💼 Context @ Consumer

> Flow
* Part of the [`Share Bind` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Bind 👉🔗💼/🧑‍🦰 Share Bind ⏩ flow.md>)

> Implementation

* Implements the [Consumer 💼 domain](<../../💼🎭 Consumer role.md>)
* Implemented by the [`Context` 📃 handler](<💼 Context 📃 handler.md>)

> Purpose

* Asks the [Consumer 💼 domain](<../../💼🎭 Consumer role.md>) for the context of a [`Query@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>), if the requested [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) defines a context for requests.

> Example

* Consider a request to select the best date and time for a restaurant table reservation;
* it requires the context of the opening hours, working days, time slots still available, the building accessibility for the available slots, the menus available in each day of the week, and any other specificities related to the business.

<br>

## Synchronous Request 🚀

```yaml
Header:
    From: any-vault.dom
    To: any-consumer.dom
    Subject: Context@Consumer

Body:
    Hook: <hook-uuid>
    Schema: any-authority.dom/ANY-SCHEMA:1.0
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
| Header    | `From`        | string    | [Vault 🗄️ domain](<../../../Vaults 🗄️/🗄️🎭 Vault role.md>) | [`Bound@`](<../../../Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|           | `To`          | string    | [Consumer 💼](<../../💼🎭 Consumer role.md>) | [`Query@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
|           | `Subject`     | string    | `Context@Consumer`
| Body      | `Hook`        | uuid      | Hook | [`Query@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
|           | `Schema`      | string    | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) for [Trust 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) | [`Query@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [`Trusts@`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts.md>)
|

## Synchronous Response

```yaml
Context: {...}
```