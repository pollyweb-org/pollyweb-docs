# 🧑‍🦰🐌💼 Helped @ Consumer

> About
* Implemented by the [`Helped` 📃 script](<💼 Helped 📃 handler.md>)



<br/>

## Async Message 🐌

```yaml
Header:
    From: any-helper.dom
    To: any-consumer.dom
    Subject: Helped@Consumer

Body: 
    Invite: <invite-uuid>
    Help: {data}
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
| Header|`From`|text| `Anonymous`
| |`To`|text| [Consumer 💼](<../../💼 Consumer/💼🎭 Consumer role.md>) | [`Share@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>)
| | `Subject`|text| `Receive@Consumer`
| Body | `Invite` | uuid | [Issuer 🎴](<../../../Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) Query | [`Share@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>)
|   | `Token` | uuid | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) ID | [`Share@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>) | [`Status@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Status 💼🚀🤵/🤵 Status 🚀 call.md>)
|| `Issuer` | text | [Issuer 🎴](<../../../Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) name | [`Issue@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Status@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Status 💼🚀🤵/🤵 Status 🚀 call.md>)
||...| ... | Properties | [`Save@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)
|


