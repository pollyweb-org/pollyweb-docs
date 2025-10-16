<!-- https://quip.com/rKzMApUS5QIi#temp:C:WTI8724d650e2ae45dabb56baea4 -->

# 💼🐌🤵  Query @ Broker

* In a [Chat 💬](<../../../../35 Chats/💬 Chats/💬 Chat.md>), 
    * a [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>) 
    * asks the [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) 
    * for access to user data 
    * in one or more [Schema Codes 🧩](<../../../../30 Data/1 🧩 Schema Codes/🧩 Schema Code.md>).

* Used by: 
    * [💼⏩🧑‍🦰 Inform ⏩ flow](<../../../../41 🎭 Domain Roles/27 💼 Consumers/💼⏩ Consumer flows/💼⏩🧑‍🦰 Inform 📝.md>)
    * [🧑‍🦰👉💼 Share Token ⏩ flow](<../../../1 🧑‍🦰 Wallets/🧑‍🦰👉 Wallet flows/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token 🎫.md>)
    * [🧑‍🦰👉💼 Share Bind ⏩ flow](<../../../1 🧑‍🦰 Wallets/🧑‍🦰👉 Wallet flows/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind 🔗.md>)

<br/> 

## Async Message 🐌

```yaml
Header:
    From: any-consumer.com
    To: any-broker.com
    Subject: Query@Broker

Body:
    ChatID: <chat-uuid>
    ConsumerKey: <consumer-key>
    Codes:
      # either the driver's license,
      - usa.gov/DRIVER-LICENSE:1.0
      # or the passport.
      - icao.int/PASSPORT:1.0 # either the old passport,
      - icao.int/PASSPORT:2.0 # or the new version.
```

|Object|Property|Type|Description
|-|-|-|-
| Header | `From`| sting | [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>) name
| | `To` | string | [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) name
| | `Subject` | string | `Query@Broker`
| Body | `ChatID` | string | [Chat 💬](<../../../../35 Chats/💬 Chats/💬 Chat.md>) ID
| | `ConsumerKey`| uuid | [`Consume@Consumer`](<../../../../41 🎭 Domain Roles/27 💼 Consumers/💼🅰️ Consumer methods/🗄️🐌💼 Consume.md>) callback
| | `Codes` | string[] | List of [Schema Codes 🧩](<../../../../30 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)
|

<br/>

## FAQ

1. **Why a list of Codes instead of a single one?**
   
    Although many [Schema Codes 🧩](<../../../../30 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) may be requested, 
    * only one of them will be returned; 
    * this allows for alternative documents;
    * e.g., passport or driver's license.

    ---
    <br/>

1. **Are suspended Tokens shared?**

    For [Tokens 🎫](<../../../../30 Data/3 🎫 Tokens/🎫 Token.md>), 
    * only shows the ones that are active,
    * i.e., within the start and expiration date.

    ---
    <br/>

1. **How are SELF Tokens are shared?**

    For the [Schema Codes 🧩](<../../../../30 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) marked with SELF, 
    * only shows the [Tokens 🎫](<../../../../30 Data/3 🎫 Tokens/🎫 Token.md>) issued by the [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>),
    * e.g., [`.BOOKING/SELF 🧩`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🧩 Host schemas/🧩 HOST'BOOKING'SELF.md>).

    ---