# 🤵🐌🎴 Accepted @ Issuer

> Flow
* Part of the [🧑‍🦰👉🎴 Save Token @ Issuer](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>) flow.

> Implementation
* Implemented by the [`Accepted` 📃 script](<🎴 Accepted 📃 handler.md>)

> Purpose
* Tells an [Issuer 🎴 domain](<../../🎴 Issuer/🎴🎭 Issuer role.md>) 
    * if a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) was accepted or declined.

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-issuer.dom
    Subject: Accepted@Issuer

Body:
    Token: <token-uuid>
    Answer: true
```


|Object |Property |Type|Description|Origin
|-|-|-|-|-
|Header |`From`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Offer@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
|       |`To`|string  | [Issuer 🎴](<../../🎴 Issuer/🎴🎭 Issuer role.md>) | [`Offer@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
||`Subject`|text|`Accepted@Issuer` 
| Body  | `Token`| uuid | [Issuer 🎴](<../../🎴 Issuer/🎴🎭 Issuer role.md>) Hook | [`Offer@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) |  
|       | `Answer`| boolean | Accepted or not | 
|


