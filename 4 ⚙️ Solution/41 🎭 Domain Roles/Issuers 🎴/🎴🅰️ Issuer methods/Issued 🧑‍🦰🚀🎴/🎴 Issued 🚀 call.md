# 🧑‍🦰🚀🎴 Issued @ Issuer


> Implementation
* Part of an [Issuer 🎴 domain](<../../🎴 Issuer/🎴🎭 Issuer role.md>)
* Implemented by the [`Issued` 📃 script](<🎴 Issued 📃 handler.md>)

> Flow
* Part of the [🎴⏩🧑‍🦰 Offer Token @ Issuer](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>) flow.

> Purpose
* Allows for a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) to be downloaded 
    * from the [Issuer 🎴 domain](<../../🎴 Issuer/🎴🎭 Issuer role.md>) 
    * into the [Wallet 🧑‍🦰 app](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).

<br/>

## Synchronous Call 🚀


```yaml
Header:
    From: Anonymous
    To: any-issuer.dom
    Subject: Issued@Issuer
    
Body:
    Token: <token-uuid>
```

|Object |Property |Type|Description | Origin 
|-|-|-|-|-
|Header |`From`|text| `Anonymous`
|       |`To`|string  | [Issuer 🎴](<../../🎴 Issuer/🎴🎭 Issuer role.md>) | [`Save@Notifier`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)
||`Subject`|text|`Issued@Issuer` 
| Body | `Token`|text| [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) key | [`Save@Notifier`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)
|

<br/>


## Sync Response

```yaml
Schema: airlines.any-igo.dom/SSR/WCH:1 
...
```

|Property |Type|Description
|-|-|-
|  `Schema`|text| [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
| ... | ... | Other [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) fields 
|

<br/>


