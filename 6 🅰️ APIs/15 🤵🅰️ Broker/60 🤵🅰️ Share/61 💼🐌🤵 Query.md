<!-- https://quip.com/rKzMApUS5QIi#temp:C:WTI8724d650e2ae45dabb56baea4 -->

# 💼🐌🤵  Query @ Broker

> In a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>), a [Consumer 💼 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) asks the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) for access to user data in one or more [Schema Codes 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>).

> Used by [💼⏩🧑‍🦰 Query token](<../../../5 ⏩ Flows/24 💼⏩ Consumers/03 💼⏩🧑‍🦰 Query token.md>).

<br/> 

## Async Message 🐌

```yaml
Header:
    From: any-consumer.com
    To: any-broker.com
    Subject: Query@Broker

Body:
    ChatID: <chat-uuid>
    Codes:
      # either the driver's license,
      - usa.gov/DRIVER-LICENSE:1.0
      # or the passport.
      - icao.int/PASSPORT:1.0 # either the old passport,
      - icao.int/PASSPORT:2.0 # or the new version.
```

|Object|Property|Type|Description
|-|-|-|-
| Header | `From`| sting | [Consumer 💼 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) name
| | `To` | string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
| | `Subject` | string | `Query@Broker`
| Body | `ChatID` | string | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) ID
| | `Codes` | string[] | List of [Schema Codes 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
|

<br/>

> Although many [Schema Codes 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) may be requested,
> <br/>• only one of them will be returned; 
> <br/>• this allows for alternative documents;
> <br/>• e.g., passport or driver's license.

> For [Tokens 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>), 
> <br/>• only shows the ones that are active,
> <br/>• i.e., within the start and expiration date.

> For the [Schema Codes 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) marked with SELF, 
> <br/>• only shows the [Tokens 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) issued by the [Consumer 💼 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>),
> <br/>• e.g., [`nlweb.org/BOOKING/SELF 🧩`](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/HOST/🧩 HostBookingSelf.md>)
