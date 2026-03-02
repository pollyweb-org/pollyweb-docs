<!-- TODO: add a script diagram -->

# 💼🚀🤵  Status @ Broker

> About

* Implements the [Broker 🤵 domain](<../../🤵/🤵 Broker 🤲 helper.md>)
* Implemented by the [`Status` 📃 handler](<🤵 Status 📃 handler.md>)
* Part of the [🧑‍🦰 `Share Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>)

<br/> 

## Synchronous Call 🚀

```yaml
Header:
    From: any-consumer.dom
    To: any-broker.dom
    Subject: Status@Broker

Body:
    Token: <token-uuid>  
    Issuer: any-issuer.dom
```


|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header|`From`|text| [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
| |`To`|text| [Broker 🤵 domain](<../../🤵/🤵 Broker 🤲 helper.md>) | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
| | `Subject`|text| `Status@Broker`
| Body | `Token`| uuid | [Broker 🤵](<../../🤵/🤵 Broker 🤲 helper.md>) key | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
|   | `Issuer` | text | [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) name | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
|
    
<br/>


## Synchronous Response

```yaml
Status: SUSPENDED
Starting: 2025-10-10T13:45:00.000Z
Ending: 2025-12-31T00:00:00.000Z
```

|Property|Type|Description
|-|-|-
| `Status`  |text| `ACTIVE` `SUSPENDED` `REVOKED` `EXPIRED`
| `Starting`|text| Optional date of start of status
| `Ending`  |text| Optional date of ending of status
|
