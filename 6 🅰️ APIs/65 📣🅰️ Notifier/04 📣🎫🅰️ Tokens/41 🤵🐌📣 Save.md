# 🤵🐌📣 Save @ Notifier

> Calls [🧑‍🦰🚀🎴 Issued @ Issuer](<../../55 🎴🅰️ Issuer/01 🧑‍🦰🚀🎴 Issued.md>) and saves the response  into a local file. 

> Part of the [🧑‍🦰👉🎴 Offer Token @ Issuer](<../../../5 ⏩ Flows/60 🎴⏩ Issuers/01 🎴⏩🧑‍🦰 Offer token.md>) flow.


<br/>


## 🐌 Async Message

```yaml
Header:
    From: any-broker.com
    To: any-notifier.com
    Subject: Save@Notifier

Body:
    WalletID: <wallet-id>
    ChatID: <chat-uuid>
    Issuer: any-issuer.com
    TokenID: <token-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
||`To`|string| [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) name
||`Subject`|string|`Save@Notifier`
|Body  |`WalletID`| uuid | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) ID from [`Onboard@Notifier`](<../01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
|| `ChatID` | string | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ID
| | `Issuer`| string | [Issuer 🎴 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) name
| | `Token`| string | [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) ID from [`Offer@Broker`](<../../15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/51 🎴🐌🤵 Offer.md>)
| 