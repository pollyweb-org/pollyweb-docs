<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfTa9a1f10023324c448a569fa05 -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS.py#L199 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L10 -->

# 🧑‍🦰🚀🤵 Tokens @ Broker

> List of [Tokens 🎫](<../../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) in a [Wallet 🧑‍🦰 app](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>) for a human user, mapping to the local file.

> Used in:
> <br/> • [🧑‍🦰👉🤵 Translate @ Broker](<../../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in App 🏠/💬🤵 Translate.md>) flow
> <br/> • [🧑‍🦰👉🤵 List Tokens @ Broker](<../../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in App 🏠/💬🤵 List Tokens 🎫.md>) flow

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Tokens@Broker
Body: 
```

| Object | Property | Type  | Description
|-|-|-|-
| Header    | `From`| uuid  | [Wallet 🧑‍🦰](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `To`  | string| [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `Subject`| string|  `Tokens@Broker`
|

<br/>

## Sync Response

```yaml
Tokens:
  - Issuer: any-issuer.dom
    TokenID: <token-uuid>
    IssuerTitle: Any Issuer
    CodeTitle: Any Code
    Path: /storage/nlweb/tokens/any-issuer.dom/<token-uuid>
    Status: REVOKED
    Locator: .TOKEN,any-issuer.dom,any-key
```

|Object|Property|Type|Description|
|-|-|-|-
|Top   |`Tokens`   |Token[]|List of `Token` objects|
|Token | `Issuer` | string | [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) from [`Saved@Broker`](<🧑‍🦰🐌🤵 Saved.md>)
||`TokenID`  |uuid   |[Token 🎫](<../../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) ID from [`Saved@Broker`](<🧑‍🦰🐌🤵 Saved.md>)
|| `IssuerTitle` | string | [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) after [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|| `CodeTitle` | string | [Code 🧩](<../../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) after [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|| `Path`| string | Local path from [`Saved@Broker`](<🧑‍🦰🐌🤵 Saved.md>)
|| `Status`| enum | Status set in [`Status@Broker`](<../6 🤵🅰️ Share/💼🚀🤵 Status.md>)
| |`Locator`| string | [Locator 🔆](<../../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) from [`Status@Broker`](<../6 🤵🅰️ Share/💼🚀🤵 Status.md>)
|