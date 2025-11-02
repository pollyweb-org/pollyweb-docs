<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfTa9a1f10023324c448a569fa05 -->
<!-- Source: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS.py#L199 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L10 -->

# 🧑‍🦰🚀🤵 Tokens @ Broker

> Implemented by the [`Tokens` 📃 handler](<🤵 Tokens 📃 handler.md>)

> Purpose

* List of [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) 
  * in a [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) for a human user, 
  * mapping to the local file.

> Used in
  * [🧑‍🦰💬🤵 Translate @ Broker](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Set Language 💬🤵/🧑‍🦰 Set Language ⏩ flow.md>) flow
  * [🧑‍🦰💬🤵 List Tokens @ Broker](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/List Tokens 🎫💬🤵/🧑‍🦰 List Tokens ⏩ flow.md>) flow

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Tokens@Broker
```

| Object | Property | Type  | Description | Origin
|-|-|-|-|-
| Header    |`From`| uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  | [`Onboard@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|           |`To`|domain| [Broker 🤵](<../../🤵 Broker helper/🤵🤲 Broker helper.md>) | [`Onboard@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|           | `Subject`| string|  `Tokens@Broker`
|

<br/>

## Sync Response

```yaml
Tokens:
  - Issuer: any-issuer.dom
    Issuer$: Any Issuer
    Locator: any-domain.dom/ANY-RESOURCE
    Schema: any-authority.dom/ANY-CODE:1.0
    Schema$: Any Code
    Status: REVOKED
    Token: <token-uuid>
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
|Tokens | `Issuer` | string | [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) | [`Saved@`](<../Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>)
|| `Issuer$` | string | [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) | [`Translate@`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| |`Locator`| string | [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) | [`Status@`](<../Share 💼 Status 💼🚀🤵/🤵 Status 🚀 request.md>)
|| `Schema$` | string | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`Translate@`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|| `Status`| enum | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) Status | [`Status@`](<../Share 💼 Status 💼🚀🤵/🤵 Status 🚀 request.md>)
||`Token`  |uuid   | [Broker 🤵](<../../🤵 Broker helper/🤵🤲 Broker helper.md>) key | [`Saved@`](<../Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>)
|

## FAQ

1. **Why isn't the Token Key listed?**

    [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) keys are held by [Broker 🤵 domains](<../../🤵 Broker helper/🤵🤲 Broker helper.md>) until shared, to avoid replay attacks from [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) purposefully breaking the [`Save Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>) halfway to receive duplicate [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>).

    ---
    <br/>