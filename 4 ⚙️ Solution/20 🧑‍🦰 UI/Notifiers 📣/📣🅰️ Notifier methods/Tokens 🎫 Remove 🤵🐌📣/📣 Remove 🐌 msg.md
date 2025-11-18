
# 🤵🐌📣 Remove @ [Notifier](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>)

> Implements the [Notifier 📣 domain](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>)

> Used in [🧑‍🦰👉🤵 Remove token](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/Remove 💬🎫🤵 /🧑‍🦰 Remove Token ⏩ flow.md>)

> Called by the [`OnTokenPurged` 📃 script](<../../../Brokers 🤵/🤵🪣 Broker tables/Tokens 🎫 table/🪣🔔 6 Purged/🤵 OnTokenPurged 📃 handler.md>)


<br/>

## Async Message 🐌
```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Remove@Notifier

Body:
    Wallet: <wallet-id>
    Token: <token-uuid>
```


|Object|Property|Type|Description|Origin
|-|-|-|-|-
|Header|`From`|text| [Broker 🤵](<../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
||`To`|text| [Notifier 📣](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
||`Subject`|text|`Remove@Broker`
|Body  |`Wallet`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
||`Token`    |uuid| [Broker 🤵](<../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) key | [`Save@`](<../Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)
|