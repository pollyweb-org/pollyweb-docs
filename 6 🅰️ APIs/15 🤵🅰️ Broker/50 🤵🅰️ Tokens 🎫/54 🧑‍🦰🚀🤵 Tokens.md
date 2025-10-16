<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfTa9a1f10023324c448a569fa05 -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS.py#L199 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L10 -->

# 🧑‍🦰🚀🤵 Tokens @ Broker

> List of [Tokens 🎫](<../../../4 ⚙️ Solution/30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) in a [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) for a human user, mapping to the local file.

> Used in:
> <br/> • [🧑‍🦰👉🤵 Translate @ Broker](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/10 👉🤵 Set-up/12 🧑‍🦰👉🤵 Translate.md>) flow
> <br/> • [🧑‍🦰👉🤵 List Tokens @ Broker](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/01 🧑‍🦰👉🤵 List tokens.md>) flow

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.com
    Subject: Tokens@Broker
Body: 
```

| Object | Property | Type  | Description
|-|-|-|-
| Header    | `From`| uuid  | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)  from [`Onboard@Notifier`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `To`  | string| [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `Subject`| string|  `Tokens@Broker`
|

<br/>

## Sync Response

```yaml
Tokens:
  - Issuer: any-issuer.com
    TokenID: <token-uuid>
    IssuerTitle: Any Issuer
    CodeTitle: Any Code
    Path: /storage/nlweb/tokens/any-issuer.com/<token-uuid>
    Status: REVOKED
    Locator: .TOKEN,any-issuer.com,any-key
```

|Object|Property|Type|Description|
|-|-|-|-
|Top   |`Tokens`   |Token[]|List of `Token` objects|
|Token | `Issuer` | string | [Issuer 🎴](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/40 🎴 Issuers/🎴🎭 Issuer role.md>) from [`Saved@Broker`](<53 🧑‍🦰🐌🤵 Saved.md>)
||`TokenID`  |uuid   |[Token 🎫](<../../../4 ⚙️ Solution/30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) ID from [`Saved@Broker`](<53 🧑‍🦰🐌🤵 Saved.md>)
|| `IssuerTitle` | string | [Issuer 🎴](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/40 🎴 Issuers/🎴🎭 Issuer role.md>) after [`Translate@Graph`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|| `CodeTitle` | string | [Code 🧩](<../../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) after [`Translate@Graph`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|| `Path`| string | Local path from [`Saved@Broker`](<53 🧑‍🦰🐌🤵 Saved.md>)
|| `Status`| enum | Status set in [`Status@Broker`](<../60 🤵🅰️ Share/62 💼🚀🤵 Status.md>)
| |`Locator`| string | [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) from [`Status@Broker`](<../60 🤵🅰️ Share/62 💼🚀🤵 Status.md>)
|