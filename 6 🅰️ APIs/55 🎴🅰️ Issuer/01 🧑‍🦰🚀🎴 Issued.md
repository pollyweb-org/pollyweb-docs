<!-- #TODO -->

<!-- Docs: https://quip.com/a167Ak79FKlt#temp:C:TMB24db6408284b4de5a52bcdfec -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/issuer/ISSUER_TESTS.py#L16 -->


# 🧑‍🦰🚀🎴 Issued @ Issuer

> Allows for a [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) to be downloaded from the [Issuer 🎴 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) into the [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

> Part of the [🎴⏩🧑‍🦰 Offer Token @ Issuer](<../../5 ⏩ Flows/60 🎴⏩ Issuers/01 🎴⏩🧑‍🦰 Offer token.md>) flow.

<br/>

## Sync Request 🚀


```yaml
Header:
    From: any-broker.com
    To: any-issuer.com
    Subject: Token@Issuer
    
Body:
    TokenID: <token-uuid>
```

|Object |Property |Type|Description
|-|-|-|-
|Header | `From`  | string  | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
|       | `To`    | string  | [Issuer 🎴 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) name
||`Subject`|string|`Token@Issuer` 
| Body  | `TokenID`| string | [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) ID sent on [Offer@Broker](<../15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/51 🎴🐌🤵 Offer.md>)
|

<br/>

## Sync Response

```yaml
QR: `<qr>`
```

|Property |Type|Description
|-|-|-
|`QR`     |string| [QR Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>)
|`Issued` |timestamp| When it was issued
|`Starts` |timestamp| Valid from
|`Expires`|timestamp| Valid until
|