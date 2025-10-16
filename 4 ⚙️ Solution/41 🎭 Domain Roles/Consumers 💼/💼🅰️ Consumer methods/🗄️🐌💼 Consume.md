<!-- https://quip.com/UbokAEferibV#temp:C:Yfbbd64684ba1df4ea683cf4e49b -->
# 🗄️🐌💼 Consume @ Consumer


> Used by [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰👉 Wallet flows/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind 🔗.md>)

* Asks the [Consumer 💼 domain](<../💼🎭 Consumer role.md>) to consume a given [Bind 🔗](<../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>).
* Tells them to collect data shared by a user in a [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>).

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-vault.com
    To: any-consumer.com
    Subject: Consume@Consumer

Body:
    Broker: any-broker.com
    ChatID: <chat-uuid>
    Code: airlines.any-igo.org/SSR/WCH:1
    ConsumerKey: <consumer-key>
    VaultKey: <vault-key>
    TTL: 2023-04-01T05:00:30.001000Z
```


|Property|Type|Description
|-|-|-
| `From`| string | [Vault 🗄️ domain](<../../Vaults 🗄️/🗄️🎭 Vault role.md>) name
| `To`| string | [Consumer 💼 domain](<../💼🎭 Consumer role.md>) name
| `Subject` | string | `Consume@Consumer`
| `Broker`| string | [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) name
| `ChatID` | uuid | [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID
| `Code`| string |  [Schema Code 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)
| `ConsumerKey` | uuid | From [`Query@`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Query.md>) and [`Invite@`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Invite.md>)
| `VaultKey` | uuid | Callback to [`Collect@Vault`](<../../Vaults 🗄️/🗄️🅰️ Vault methods/💼🚀🗄️ Collect.md>)
| `TTL` | timestamp| Callback deadline
|


<br/>

## FAQ

1. **Why a cache?**

    `Async` A caching strategy avoids synchronous collection timeouts.
    * When [Consumer 💼 domains](<../💼🎭 Consumer role.md>)  call [`Collect@Vault`](<../../Vaults 🗄️/🗄️🅰️ Vault methods/💼🚀🗄️ Collect.md>), [Vault 🗄️ domains](<../../Vaults 🗄️/🗄️🎭 Vault role.md>) are expected to gather and cache the data and only send the [`Consume@Consumer`](<🗄️🐌💼 Consume.md>) message when the data is cached and ready to be collected.
    * The Vault's cache duration is expressed in the `TTL` field.

    ---
    <br/>
