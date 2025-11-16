<!-- TODO: add a script diagram -->

# 💼🚀🤵  Status @ Broker

> Implementation

* Implements the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* Implemented by the [`Status` 📃 handler](<🤵 Status 📃 handler.md>)

> Used in
* [💼⏩🧑‍🦰 Share Token @ Consumer](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>)

<br/> 

## Synchronous Call 🚀

```yaml
Header:
    From: any-consumer.dom
    To: any-broker.dom
    Subject: Status@Broker

Body:
    Token: <token-uuid>  
```


|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header|`From`|text| [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
| |`To`|text| [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
| | `Subject`|text| `Status@Broker`
| Body | `Token`| uuid | [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) key | [`Receive@`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
|
    
<br/>


## Synchronous Response

```yaml
Status: SUSPENDED
Starting: 2025-10-10T13:45:00.000Z
Ending: 2025-12-31T00:00:00.000Z
Locator: .HOST,any-host.dom,any-key
```

|Property|Type|Description
|-|-|-
| `Status`  |text| `ACTIVE` `SUSPENDED` `REVOKED` `EXPIRED`
| `Starting`|text| Optional date of start of status
| `Ending`  |text| Optional date of ending of status
| `Locator`|text| Optional [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) for a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) about it
|
