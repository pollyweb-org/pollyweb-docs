<!-- https://quip.com/UbokAEferibV#temp:C:Yfbbd64684ba1df4ea683cf4e49b -->
# 🗄️🐌💼 Consume @ Consumer

> Implementation
* Implemented by the [`Consume` 📃 handler](<💼 Consume 📃 handler.md>)

> Used by
* [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Bind 👉🔗💼/🧑‍🦰 Share Bind ⏩ flow.md>)

> Purpose
* Asks the [Consumer 💼 domain](<../../💼🎭 Consumer role.md>) to consume a given [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>).
* Tells them to collect data shared by a user in a [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>).

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-vault.dom
    To: any-consumer.dom
    Subject: Consume@Consumer

Body:
    Hook: <hook-uuid>
    Collect: <collect-uuid>
    Schema: any-authority.dom/ANY-SCHEMA:1.0
    TTL: 2023-04-01T05:00:30.001000Z
```


Object |Property|Type|Description
|-|-|-|-
|Header| `From`| string | [Vault 🗄️ domain](<../../../Vaults 🗄️/🗄️🎭 Vault role.md>) name
|| `To`| string | [Consumer 💼 domain](<../../💼🎭 Consumer role.md>) name
|| `Subject` | string | `Consume@Consumer`
|Body| `Hook` | uuid | From [`Query@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) and [`Invite@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)
|| `Collect` | uuid | Hook for [`Collect@Vault`](<../../../Vaults 🗄️/🗄️🅰️ Vault methods/Collect 💼🚀🗄️/🗄️ Collect 🚀 request.md>)
|| `Schema`| string |  [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) of the data
|| `TTL` | timestamp| Callback deadline
|


<br/>

## FAQ

1. **Why a cache?**

    `Async` A caching strategy avoids synchronous collection timeouts.
    * When [Consumer 💼 domains](<../../💼🎭 Consumer role.md>)  call [`Collect@Vault`](<../../../Vaults 🗄️/🗄️🅰️ Vault methods/Collect 💼🚀🗄️/🗄️ Collect 🚀 request.md>), [Vault 🗄️ domains](<../../../Vaults 🗄️/🗄️🎭 Vault role.md>) are expected to gather and cache the data and only send the [`Consume@Consumer`](<💼 Consume 🐌 msg.md>) message when the data is cached and ready to be collected.
    * The Vault's cache duration is expressed in the `TTL` field.

    ---
    <br/>
