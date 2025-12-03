# 🧑‍🦰🐌💼 Receive @ Consumer

> About
* Implemented by the [`Receive` 📃 script](<💼 Receive 📃 handler.md>)
* Part of the [`Share Token` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>) 
* Succeeds the [`Share@Notifier` 📨 msg](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>)
* [Wallet 🧑‍🦰 apps](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) send [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) to a [Consumer 💼 domain](<../../💼 Consumer/💼🎭 Consumer role.md>).



<br/>

## Async Message 🐌

```yaml
Header:
    From: Anonymous
    To: any-consumer.dom
    Subject: Receive@Consumer

Body: 
    Query: <query-uuid>
    Shared: 
        Token: <token-uuid>
        Issuer: any-issuer.dom

        # Properties from Save@Notifier
        Schema: .TOKEN
        Properties:
            Property1: Value1
            Property2: Value2
        Issued: 2024-09-21T12:34:00Z
        Starts: 2024-01-10T13:45:00.000Z
        Expires: 2028-12-10T13:45:00.000Z
        Signature: ABCMIQDALK2Fd...
        DKIM: pk1
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
| Header|`From`|text| `Anonymous`
| |`To`|text| [Consumer 💼](<../../💼 Consumer/💼🎭 Consumer role.md>) | [`Share@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>)
| | `Subject`|text| `Receive@Consumer`
| Body | `Query` | uuid | [Issuer 🎴](<../../../Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) Query | [`Share@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>)
|   | `Token` | uuid | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) ID | [`Share@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>) | [`Status@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Status 💼🚀🤵/🤵 Status 🚀 call.md>)
|| `Issuer` | text | [Issuer 🎴](<../../../Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) name | [`Issue@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Status@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Status 💼🚀🤵/🤵 Status 🚀 call.md>)
||...| ... | Properties | [`Save@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)
|


