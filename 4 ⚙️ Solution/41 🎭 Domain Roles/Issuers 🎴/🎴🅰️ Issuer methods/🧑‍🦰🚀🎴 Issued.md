<!-- Docs: https://quip.com/a167Ak79FKlt#temp:C:TMB24db6408284b4de5a52bcdfec -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/issuer/ISSUER_TESTS.py#L16 -->


# 🧑‍🦰🚀🎴 Issued @ Issuer

> Implemented by the [`Issued` 📃 script](<../🎴📃 Issuer scripts/🎴📃 Issued.md>)

> Part of the [🎴⏩🧑‍🦰 Offer Token @ Issuer](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉🎴 Save token.md>) flow.

> Purpose:
* Allows for a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) to be downloaded 
    * from the [Issuer 🎴 domain](<../🎴🎭 Issuer role.md>) 
    * into the [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).



<br/>

## Sync Request 🚀


```yaml
Header:
    From: Anonymous
    To: any-issuer.dom
    Subject: Token@Issuer
    
Body:
    Hook: <hook-uuid>
```

|Object |Property |Type|Description
|-|-|-|-
|Header | `From`  | string  | `Anonymous`
|       | `To`    | string  | [Issuer 🎴](<../🎴🎭 Issuer role.md>) from [`Save@Notifier`](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/📣 Tokens 🎫 Save 🤵🐌📣/Save 🐌 msg.md>)
||`Subject`|string|`Token@Issuer` 
| Body | `Hook`| string | `Hook` from [`Save@Notifier`](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/📣 Tokens 🎫 Save 🤵🐌📣/Save 🐌 msg.md>)
|

<br/>

## Sync Response

```yaml
Schema: airlines.any-igo.dom/SSR/WCH:1 
...
```

|Property |Type|Description
|-|-|-
|  `Schema`| string | [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
| ... | ... | Other [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) fields 
|

<br/>


## FAQ

1. **Why isn't the `Token` ID property in the response?**

    At this point, the [Issuer 🎴](<../🎴🎭 Issuer role.md>) doesn't know the `Token` yet.
    * That information will be given later in [`Accepted@Issuer`](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/🤵🐌🎴 Accepted.md>).

    ---
    <br/>