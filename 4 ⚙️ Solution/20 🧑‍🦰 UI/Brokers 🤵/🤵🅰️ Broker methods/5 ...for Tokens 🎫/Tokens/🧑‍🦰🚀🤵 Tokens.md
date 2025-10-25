<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfTa9a1f10023324c448a569fa05 -->
<!-- Source: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS.py#L199 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L10 -->

# 🧑‍🦰🚀🤵 Tokens @ Broker

> Implemented by the [`Tokens` 📃 handler](<.📎 Assets/Tokens 📃 handler.md>)

> Purpose

* List of [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) 
  * in a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) for a human user, 
  * mapping to the local file.

> Used in
  * [🧑‍🦰💬🤵 Translate @ Broker](<../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/💬🤵 Translate.md>) flow
  * [🧑‍🦰💬🤵 List Tokens @ Broker](<../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/💬🤵 List Tokens 🎫.md>) flow

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Tokens@Broker
```

| Object | Property | Type  | Description
|-|-|-|-
| Header    | `From`| uuid  | [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `To`  | string| [Broker 🤵](<../../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `Subject`| string|  `Tokens@Broker`
|

<br/>

## Sync Response

```yaml
Tokens:
  - Issuer: any-issuer.dom
    Issuer$: Any Issuer
    Key: <any-key>
    Path: /storage/nlweb/tokens/any-issuer.dom/<token-uuid>
    Schema: any-authority.dom/ANY-SCHEMA:1.0
    Schema$: Any Code
    Status: REVOKED
    Token: <token-uuid>
```

|Object|Property|Type|Description|
|-|-|-|-
|Top   |`Tokens`   |Token[]|List of `Token` objects|
|Token | `Issuer` | string | [Issuer 🎴](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) from [`Saved@Broker`](<../Saved 🐌/🧑‍🦰🐌🤵 Saved.md>)
|| `Issuer$` | string | [Issuer 🎴](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) after [`Translate@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|| `Path`| string | Local path from [`Saved@Broker`](<../Saved 🐌/🧑‍🦰🐌🤵 Saved.md>)
|| `Schema$` | string | [Schema 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) after [`Translate@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|| `Status`| enum | Status set in [`Status@Broker`](<../../6 ...for Share 💼/Status/💼🚀🤵 Status.md>)
||`Token`  |uuid   |[Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) ID from [`Saved@Broker`](<../Saved 🐌/🧑‍🦰🐌🤵 Saved.md>)
| |`Locator`| string | [Locator 🔆](<../../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) from [`Status@Broker`](<../../6 ...for Share 💼/Status/💼🚀🤵 Status.md>)
|

