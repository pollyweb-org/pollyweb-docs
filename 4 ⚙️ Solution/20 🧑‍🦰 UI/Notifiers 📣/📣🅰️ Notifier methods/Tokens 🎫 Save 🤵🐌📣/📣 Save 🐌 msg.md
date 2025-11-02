# 🤵🐌📣 Save @ Notifier

> Implements the [Notifier 📣 domain](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>)

> Purpose
* Calls the [`Issued@Issuer` 🅰️ method](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 request.md>) 
* and saves the response  into a local file. 

> Flow
* Part of the [`Save Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>).
* Followed by the [`Issued@Issuer` 🅰️ method](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 request.md>)


<br/>


## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Save@Notifier

Body:
    Wallet: <wallet-id>
    Hook: <hook-uuid>
    Token: <token-uuid>
```

|Object|Property|Type|Description | Origin | Purpose
|-|-|-|-|-|-
|Header|`From`|domain| [Broker 🤵](<../../../Brokers 🤵/🤵 Broker helper/🤵🤲 Broker helper.md>) | [`Offer@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
||`To`|domain| [Notifier 📣](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`Subject`|string|`Save@Notifier`
|Body  |`Wallet`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`Hook`|uuid| [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) Hook | [`Offer@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) | [`Issued@`](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 request.md>)
|| `Token`| uuid | New [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) | | [`Saved@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>)
| 