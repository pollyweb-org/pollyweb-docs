<!-- https://quip.com/UbokAEferibV#temp:C:Yfbbd64684ba1df4ea683cf4e49b -->
# 🗄️🐌💼 Consume @ Consumer


> Used by [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉💼 Share Bind 🔗.md>)

* Asks the [Consumer 💼 domain](<../💼🎭 Consumer role.md>) to consume a given [Bind 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>).
* Tells them to collect data shared by a user in a [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>).

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-vault.dom
    To: any-consumer.dom
    Subject: Consume@Consumer

Body:
    Broker: any-broker.dom
    Chat: <chat-uuid>
    Schema: airlines.any-igo.dom/SSR/WCH:1
    Hook: <hook-uuid>
    Collect: <collect-uuid>
    TTL: 2023-04-01T05:00:30.001000Z
```


|Property|Type|Description
|-|-|-
| `From`| string | [Vault 🗄️ domain](<../../Vaults 🗄️/🗄️🎭 Vault role.md>) name
| `To`| string | [Consumer 💼 domain](<../💼🎭 Consumer role.md>) name
| `Subject` | string | `Consume@Consumer`
| `Broker`| string | [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) name
| `Chat` | uuid | [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID
| `Schema`| string |  [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
| `Hook` | uuid | From [`Query@`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/...for Share 💼/Query/💼🐌🤵 Query.md>) and [`Invite@`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/...for Share 💼/Invite/💼🐌🤵 Invite.md>)
| `Collect` | uuid | Hook for [`Collect@Vault`](<../../Vaults 🗄️/🗄️🅰️ Vault methods/Collect/💼🚀🗄️ Collect.md>)
| `TTL` | timestamp| Callback deadline
|


<br/>

## FAQ

1. **Why a cache?**

    `Async` A caching strategy avoids synchronous collection timeouts.
    * When [Consumer 💼 domains](<../💼🎭 Consumer role.md>)  call [`Collect@Vault`](<../../Vaults 🗄️/🗄️🅰️ Vault methods/Collect/💼🚀🗄️ Collect.md>), [Vault 🗄️ domains](<../../Vaults 🗄️/🗄️🎭 Vault role.md>) are expected to gather and cache the data and only send the [`Consume@Consumer`](<🗄️🐌💼 Consume.md>) message when the data is cached and ready to be collected.
    * The Vault's cache duration is expressed in the `TTL` field.

    ---
    <br/>
