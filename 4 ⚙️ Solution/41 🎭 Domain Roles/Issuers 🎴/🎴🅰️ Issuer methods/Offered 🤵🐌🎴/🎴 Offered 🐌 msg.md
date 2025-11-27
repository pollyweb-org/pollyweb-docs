# 🤵🐌🎴 Offered @ Issuer

> Implementation
* Part of an [Issuer 🎴 domain](<../../🎴 Issuer/🎴🎭 Issuer role.md>)
* Implemented by the [`Offered` 📃 script](<🎴 Offered 📃 handler.md>)

> Flow
* Part of the [🧑‍🦰👉🎴 Save Token @ Issuer](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>) flow.


> Purpose
* Tells an [Issuer 🎴 domain](<../../🎴 Issuer/🎴🎭 Issuer role.md>) 
    * if a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) was accepted or declined.

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-issuer.dom
    Subject: Offered@Issuer

Body:
    Token: <token-uuid>
    Answer: ACCEPTED
```


|Object |Property |Type|Description|Origin
|-|-|-|-|-
|Header |`From`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Issue@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>)
|       |`To`|text  | [Issuer 🎴](<../../🎴 Issuer/🎴🎭 Issuer role.md>) | [`Issue@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>)
||`Subject`|text|`Offered@Issuer` 
| Body  | `Token`| uuid | [Issuer 🎴](<../../🎴 Issuer/🎴🎭 Issuer role.md>) Hook | [`Issue@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) |  
|       | `Answer`| text | `ACCEPTED` `DECLINED` | 
|


