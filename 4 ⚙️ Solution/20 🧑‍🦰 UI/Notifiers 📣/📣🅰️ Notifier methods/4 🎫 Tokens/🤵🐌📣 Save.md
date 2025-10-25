# 🤵🐌📣 Save @ Notifier

> Implements the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>)

> Purpose
* Calls the [`Issued@Issuer` 🅰️ method](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/🧑‍🦰🚀🎴 Issued.md>) 
* and saves the response  into a local file. 

> Part of the [🧑‍🦰👉🎴 Offer Token @ Issuer](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉🎴 Save token.md>) flow.

* Followed by the [`Issued@Issuer` 🅰️ method](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/🧑‍🦰🚀🎴 Issued.md>)


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

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) from [`Offer@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/...for Tokens 🎫/Offer 🐌/🎴🐌🤵 Offer.md>)
||`To`|string| [Notifier 📣](<../../📣👥 Notifier domain.md>) from [`Onboard@Notifier`](<../1 🤵 Onboard/🧑‍🦰🚀📣 Onboard.md>)
||`Subject`|string|`Save@Notifier`
|Body  |`Wallet`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) from [`Onboard@Notifier`](<../1 🤵 Onboard/🧑‍🦰🚀📣 Onboard.md>)
||`Hook`|uuid|`Hook` from [`Offer@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/...for Tokens 🎫/Offer 🐌/🎴🐌🤵 Offer.md>)
|| `Token`| uuid | New [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) ID at the [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>)
| 