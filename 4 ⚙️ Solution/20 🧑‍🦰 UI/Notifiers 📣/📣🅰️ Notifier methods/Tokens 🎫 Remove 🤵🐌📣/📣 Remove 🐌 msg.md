
# 🤵🐌📣 Remove @ [Notifier](<../../📣👥 Notifier domain.md>)

> Implements the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>)

> Used in [🧑‍🦰👉🤵 Remove token](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/Remove 💬🎫🤵 /🧑‍🦰 Remove Token ⏩ flow.md>).

> Called by the [`TokenTimeout` 📃 script](<../../../Brokers 🤵/🤵🪣 Broker tables/Tokens 🎫 table/🤵 Tokens Timeout 📃 trigger.md>)


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
|Header|`From`|string | [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`To`|string| [Notifier 📣](<../../📣👥 Notifier domain.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`Subject`|string|`Remove@Broker`
|Body  |`Wallet`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`Token`    |uuid| [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) key | [`Save@`](<../Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)
|