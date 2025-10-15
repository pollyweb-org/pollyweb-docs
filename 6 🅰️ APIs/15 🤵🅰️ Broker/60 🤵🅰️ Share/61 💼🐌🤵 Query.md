<!-- https://quip.com/rKzMApUS5QIi#temp:C:WTI8724d650e2ae45dabb56baea4 -->

# 💼🐌🤵  Query @ Broker

* In a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>), 
    * a [Consumer 💼 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) 
    * asks the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) 
    * for access to user data 
    * in one or more [Schema Codes 🧩](<../../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>).

* Used by: 
    * [💼⏩🧑‍🦰 Inform ⏩ flow](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/02 💼⏩🧑‍🦰 Inform 📝.md>)
    * [🧑‍🦰👉💼 Share Token ⏩ flow](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token 🎫.md>)
    * [🧑‍🦰👉💼 Share Bind ⏩ flow](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind 🔗.md>)

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
| Header | `From`| sting | [Consumer 💼 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) name
| | `To` | string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) name
| | `Subject` | string | `Query@Broker`
| Body | `ChatID` | string | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID
| | `ConsumerKey`| uuid | [`Consume@Consumer`](<../../30 💼🅰️ Consumer/02 🗄️🐌💼 Consume.md>) callback
| | `Codes` | string[] | List of [Schema Codes 🧩](<../../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>)
|

<br/>

## FAQ

1. **Why a list of Codes instead of a single one?**
   
    Although many [Schema Codes 🧩](<../../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>) may be requested, 
    * only one of them will be returned; 
    * this allows for alternative documents;
    * e.g., passport or driver's license.

    ---
    <br/>

1. **Are suspended Tokens shared?**

    For [Tokens 🎫](<../../../4 ⚙️ Solution/25 Data/30 🎫 Tokens/$ 🎫 Token.md>), 
    * only shows the ones that are active,
    * i.e., within the start and expiration date.

    ---
    <br/>

1. **How are SELF Tokens are shared?**

    For the [Schema Codes 🧩](<../../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>) marked with SELF, 
    * only shows the [Tokens 🎫](<../../../4 ⚙️ Solution/25 Data/30 🎫 Tokens/$ 🎫 Token.md>) issued by the [Consumer 💼 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>),
    * e.g., [`.BOOKING/SELF 🧩`](<../../../7 🧩 Codes/HOST/🧩 HostBookingSelf.md>).

    ---