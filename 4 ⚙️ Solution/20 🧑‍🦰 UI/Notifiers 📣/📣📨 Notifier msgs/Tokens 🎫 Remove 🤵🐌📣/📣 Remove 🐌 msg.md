
# 🤵🐌📣 Remove @ [Notifier](<../../📣/📣 Notifier 👥 domain.md>)

> Implements the [Notifier 📣 domain](<../../📣/📣 Notifier 👥 domain.md>)

> Used in [🧑‍🦰👉🤵 Remove token](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/Remove 💬🎫🤵 /🧑‍🦰 Remove Token ⏩ flow.md>)


## Async Message 🐌
```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Remove@Notifier

Body:
    Wallet: <wallet-id>
    Path: <token-path>
```


|Object|Property|Type|Description|Origin
|-|-|-|-|-
|Header|`From`|text| [Broker 🤵](<../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
||`To`|text| [Notifier 📣](<../../📣/📣 Notifier 👥 domain.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
||`Subject`|text|`Remove@Broker`
|Body  |`Wallet`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
||`Path`    |text| Path to [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) | [`Saved@Broker`](<../../../Brokers 🤵/🤵📨 Broker msgs/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>)
|
