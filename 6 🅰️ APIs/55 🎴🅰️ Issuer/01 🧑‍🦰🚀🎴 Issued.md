<!-- Docs: https://quip.com/a167Ak79FKlt#temp:C:TMB24db6408284b4de5a52bcdfec -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/issuer/ISSUER_TESTS.py#L16 -->


# 🧑‍🦰🚀🎴 Issued @ Issuer

> Allows for a [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) to be downloaded from the [Issuer 🎴 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) into the [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

> Part of the [🎴⏩🧑‍🦰 Offer Token @ Issuer](<../../5 ⏩ Flows/60 🎴⏩ Issuers/01 🎴⏩🧑‍🦰 Offer token.md>) flow.

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
|       | `To`    | string  | [Issuer 🎴 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) name
||`Subject`|string|`Token@Issuer` 
| Body | `ChatID` | string | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/05 💬 Chats/01 💬 Chat.md>) ID
| | `TokenID`| string | [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) ID from [`Offer@Broker`](<../15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/51 🎴🐌🤵 Offer.md>)
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
| `Issuer` | string | [Issuer 🎴 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) name
| `TokenID`| string | Resource key on the [Issuer 🎴](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) 
|  `Code`| string | [Schema Code 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
| ... | ... | Other [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) fields 
|