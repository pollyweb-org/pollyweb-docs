<!-- https://quip.com/rKzMApUS5QIi#temp:C:WTI8724d650e2ae45dabb56baea4 -->

# 💼🐌🤵  Query @ Broker

> Purpose
* In a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>), 
    * a [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) 
    * asks the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) 
    * for access to user data 
    * in one or more [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>).

> Used by

* [`Inform` ⏩ flow](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)
* [`Share Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>)
* [`Share Bind` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Bind 👉🔗💼/🧑‍🦰 Share Bind ⏩ flow.md>)

<br/> 

## Async Message 🐌

```yaml
Header:
    From: any-consumer.dom
    To: any-broker.dom
    Subject: Query@Broker

Body:
    Chat: <chat-uuid>
    Query: <query-uuid>
    Schemas:
      # either the driver's license,
      - usa.gov/DRIVER-LICENSE:1.0
      # or the passport.
      - icao.int/PASSPORT:1.0 # either the old passport,
      - icao.int/PASSPORT:2.0 # or the new version.
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
| Header |`From`| sting | [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
| |`To`|text| [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
| | `Subject` |text| `Query@Broker`
| Body | `Chat` |text| [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID
| | `Query`| uuid | [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) Query | |[`Consume@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>) 
| | `Schemas` | string[] | List of [Schemas 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|

<br/>

## FAQ

1. **Why a list of Schemas instead of a single one?**
   
    Although many [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) may be requested, 
    * only one of them will be returned; 
    * this allows for alternative documents;
    * e.g., passport or driver's license.

    ---
    <br/>

1. **Are suspended Tokens shared?**

    For [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>), 
    * only shows the ones that are active,
    * i.e., within the start and expiration date.

    ---
    <br/>

1. **How are SELF Tokens are shared?**

    For the [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) marked with SELF, 
    * only shows the [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) issued by the [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>),
    * e.g., [`.HOST/BOOKING/SELF 🧩`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST'BOOKING'SELF.md>).

    ---