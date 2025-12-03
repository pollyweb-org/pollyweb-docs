# 🤵🐌📣 Save @ Notifier

> Implements the [Notifier 📣 domain](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>)

> Purpose
* Calls the [`Issued@Issuer` 🚀 call](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴📨 Issuer msgs/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 call.md>) 
* and saves the response  into a local file. 

> Flow
* Part of the [`Save Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>).
* Followed by the [`Issued@Issuer` 🚀 call](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴📨 Issuer msgs/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 call.md>)


<br/>


## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Save@Notifier

Body:
    Wallet: <wallet-id>
    Issuer: any-issuer.dom
    Offer: <offer-uuid>
```

|Object|Property|Type|Description | Origin | Purpose
|-|-|-|-|-|-
|Header|`From`|text| [Broker 🤵](<../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Issue@`](<../../../Brokers 🤵/🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>)
||`To`|text| [Notifier 📣](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
||`Subject`|text|`Save@Notifier`
|Body  |`Wallet`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
||`Issuer`|text| [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) domain  | [`Issue@`](<../../../Brokers 🤵/🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Issued@`](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴📨 Issuer msgs/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 call.md>)
||`Hook`|uuid| [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) Hook | [`Issue@`](<../../../Brokers 🤵/🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Issued@`](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴📨 Issuer msgs/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 call.md>)
| 

<br/>

## FAQ


1. **Why not send the Token ID at the Broker?**

    The objective is to avoid replay attacks from [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) purposefully breaking the [`Save Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>) halfway to collected repeated [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>).

    |||
    |-|-
    |`Offer`| This is a pointer to the [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) at the [Issuer 🎴 domain](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>), allowing [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to collect all [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) details except for the `Key`. It's only used in the [`Offer`](<../../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 OFFER.md>) flow.
    |`Key`| Contains the unique identifier of the [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) at the [Issuer 🎴 domain](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>). [Brokers 🤵](<../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) keep this `Key` hidden from [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) until there is a [`Query@Broker`](<../../../Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) message that triggers the [`Share@Notifier`](<../Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>) message. Even if there are multiple [`Issue@Broker`](<../../../Brokers 🤵/🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) calls, only the first `Key` will be sent to the [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) via [`Share@Notifier`](<../Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>).

    ---
    <br/>