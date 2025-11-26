# 🤵🐌🎴 Removed @ Issuer

> Purpose
* Tells an [Issuer 🎴 domain](<../../🎴 Issuer/🎴🎭 Issuer role.md>) 
    * that a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) was removed by the user.

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-issuer.dom
    Subject: Removed@Issuer

Body:
    Token: <token-uuid>
```


|Object |Property |Type|Description|Origin
|-|-|-|-|-
|Header |`From`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Issue@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>)
|       |`To`|text  | [Issuer 🎴](<../../🎴 Issuer/🎴🎭 Issuer role.md>) | [`Issue@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>)
||`Subject`|text|`Removed@Issuer` 
| Body  | `Token`| uuid | [Issuer 🎴](<../../🎴 Issuer/🎴🎭 Issuer role.md>) Hook | [`Issue@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) |  
|


