<!-- Docs: https://quip.com/a167Ak79FKlt#temp:C:TMB24db6408284b4de5a52bcdfec -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/issuer/ISSUER_TESTS.py#L16 -->


# 🧑‍🦰🚀🎴 Issued @ Issuer

> Allows for a [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) to be downloaded from the [Issuer 🎴 domain](<../🎴🎭 Issuer role.md>) into the [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>).

> Part of the [🎴⏩🧑‍🦰 Offer Token @ Issuer](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰⏩ Wallet flows/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) flow.

<br/>

## Sync Request 🚀


```yaml
Header:
    From: Anonymous
    To: any-issuer.com
    Subject: Token@Issuer
    
Body:
    ChatID: <chat-uuid>
    TokenID: <token-uuid>
```

|Object |Property |Type|Description
|-|-|-|-
|Header | `From`  | string  | `Anonymous`
|       | `To`    | string  | [Issuer 🎴 domain](<../🎴🎭 Issuer role.md>) name
||`Subject`|string|`Token@Issuer` 
| Body | `ChatID` | string | [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Offer@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🎴🐌🤵 Offer.md>)
| | `TokenID`| string | [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) ID from [`Offer@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🎴🐌🤵 Offer.md>)
|

<br/>

## Sync Response

```yaml
Issuer: any-issuer.com
TokenID: ANY-TOKEN-KEY
Code: airlines.any-igo.org/SSR/WCH:1 
...
```

|Property |Type|Description
|-|-|-
| `Issuer` | string | [Issuer 🎴 domain](<../🎴🎭 Issuer role.md>) name
| `TokenID`| string | Resource key on the [Issuer 🎴](<../🎴🎭 Issuer role.md>) 
|  `Code`| string | [Schema Code 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)
| ... | ... | Other [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) fields 
|