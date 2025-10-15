# 🤵🐌📣 Save @ Notifier

> Calls [🧑‍🦰🚀🎴 Issued @ Issuer](<../../../../41 🎭 Domain Roles/40 🎴 Issuers/🎴🅰️ Issuer methods/🧑‍🦰🚀🎴 Issued.md>) and saves the response  into a local file. 

> Part of the [🧑‍🦰👉🎴 Offer Token @ Issuer](<../../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) flow.


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
|Header|`From`|string | [Broker 🤵 domain](<../../../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) name
||`To`|string| [Notifier 📣 domain](<../../📣 Notifier domain.md>) name
||`Subject`|string|`Save@Notifier`
|Body  |`WalletID`| uuid | [Wallet 🧑‍🦰](<../../../01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) ID from [`Onboard@Notifier`](<../1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|| `ChatID` | string | [Chat 💬](<../../../12 💬 Chats/$ 💬 Chat.md>) ID from [`Offer@Broker`](<../../../../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/51 🎴🐌🤵 Offer.md>)
| | `Issuer`| string | [Issuer 🎴](<../../../../41 🎭 Domain Roles/40 🎴 Issuers/🎴🎭 Issuer role.md>) from [`Offer@Broker`](<../../../../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/51 🎴🐌🤵 Offer.md>)
| | `TokenID`| string | [Token 🎫](<../../../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) ID from [`Offer@Broker`](<../../../../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/51 🎴🐌🤵 Offer.md>)
| 