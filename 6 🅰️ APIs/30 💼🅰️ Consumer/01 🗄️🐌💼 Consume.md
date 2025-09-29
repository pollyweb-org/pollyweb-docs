<!-- https://quip.com/UbokAEferibV#temp:C:Yfbbd64684ba1df4ea683cf4e49b -->
# 🗄️🐌💼 Consume @ Consumer

> Asks the [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) to consume a given [Bind 🔗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>).
> <br/>• Tells them to collect data shared by a user in a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>).

> Used by [💼⏩🧑‍🦰 Query vault @ Consumer](<../../5 ⏩ Flows/20 💼⏩ Consumers/02 💼⏩🧑‍🦰 Query Vault.md>)

<br/>

## Async Message 🐌


|Property|Type|Description
|-|-|-
| `From`| string | [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) name
| `To`| string | [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) name
| `Subject` | string | `Consume@Consumer`
| `Broker`| string | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
| `ChatID` | uuid | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) ID
| `Code`| string | [Bind 🔗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) [Schema Code 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
| `Collection` | string | [Collect 🚀](<../95 🗄️🅰️ Vault/01 💼🚀🗄️ Collect.md>) callback
| `TTL` | timestamp| Cache duration deadline

```yaml
Header:
    From: any-vault.com
    Subject: Consume@Consumer

Body:
    Chat: 
        Broker: any-broker.org
        ChatID: chat-uuid
    Bind: 
        Code: airlines.any-igo.org/SSR/WCH:1
        Collection: <collection-uuid>
        TTL: 2023-04-01T05:00:30.001000Z
```

<br/>

## FAQ

1. **Why a cache?**

    `Async` A caching strategy avoids synchronous collection timeouts.
    * When [Consumer 💼 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>)  call [Collect@Vault](<../95 🗄️🅰️ Vault/01 💼🚀🗄️ Collect.md>), [Vault 🗄️ domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) are expected to gather and cache the data and only send the [Consume@Consumer](<01 🗄️🐌💼 Consume.md>) message when the data is cached and ready to be collected.
    * The Vault's cache duration is expressed in the `TTL` field.

    ---
    <br/>

    