# 🤵🐌📣 Save @ Notifier

> Calls [🧑‍🦰🚀🎴 Issued @ Issuer](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/40 🎴 Issuers/55 🎴🅰️ Issuer/01 🧑‍🦰🚀🎴 Issued.md>) and saves the response  into a local file. 

> Part of the [🧑‍🦰👉🎴 Offer Token @ Issuer](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) flow.


<br/>


## Async Message 🐌

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
|Header|`From`|string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) name
||`To`|string| [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/$ 📣 Notifier domain.md>) name
||`Subject`|string|`Save@Notifier`
|Body  |`WalletID`| uuid | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) ID from [`Onboard@Notifier`](<../01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
|| `ChatID` | string | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID from [`Offer@Broker`](<../../15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/51 🎴🐌🤵 Offer.md>)
| | `Issuer`| string | [Issuer 🎴](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/40 🎴 Issuers/$ 🎴🎭 Issuer role.md>) from [`Offer@Broker`](<../../15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/51 🎴🐌🤵 Offer.md>)
| | `TokenID`| string | [Token 🎫](<../../../4 ⚙️ Solution/30 🧩 Data/30 🎫 Tokens/$ 🎫 Token.md>) ID from [`Offer@Broker`](<../../15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/51 🎴🐌🤵 Offer.md>)
| 