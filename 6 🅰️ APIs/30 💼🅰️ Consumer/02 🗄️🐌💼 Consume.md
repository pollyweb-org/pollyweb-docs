<!-- https://quip.com/UbokAEferibV#temp:C:Yfbbd64684ba1df4ea683cf4e49b -->
# 🗄️🐌💼 Consume @ Consumer


> Used by [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind 🔗.md>)

* Asks the [Consumer 💼 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) to consume a given [Bind 🔗](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/01 🔗 Bind.md>).
* Tells them to collect data shared by a user in a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).

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
| `From`| string | [Vault 🗄️ domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) name
| `To`| string | [Consumer 💼 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) name
| `Subject` | string | `Consume@Consumer`
| `Broker`| string | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
| `ChatID` | uuid | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ID
| `Code`| string |  [Schema Code 🧩](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>)
| `ConsumerKey` | uuid | From [`Query@`](<../15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>) and [`Invite@`](<../15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>)
| `VaultKey` | uuid | Callback to [`Collect@Vault`](<../95 🗄️🅰️ Vault/01 💼🚀🗄️ Collect.md>)
| `TTL` | timestamp| Callback deadline
|


<br/>

## FAQ

1. **Why a cache?**

    `Async` A caching strategy avoids synchronous collection timeouts.
    * When [Consumer 💼 domains](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>)  call [`Collect@Vault`](<../95 🗄️🅰️ Vault/01 💼🚀🗄️ Collect.md>), [Vault 🗄️ domains](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) are expected to gather and cache the data and only send the [`Consume@Consumer`](<02 🗄️🐌💼 Consume.md>) message when the data is cached and ready to be collected.
    * The Vault's cache duration is expressed in the `TTL` field.

    ---
    <br/>
