
# 🤵🐌📣 Remove @ [Notifier](<../../📣👥 Notifier domain.md>)

> Implements the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>)

> Used in [🧑‍🦰👉🤵 Remove token](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/💬🤵 Remove 🎫 chat ⏩ flow.md>).

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
    Path: /storage/nlweb/tokens/<token-uuid>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) from [`Onboard@Broker`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`To`|string| [Notifier 📣](<../../📣👥 Notifier domain.md>) from [`Onboard@Broker`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`Subject`|string|`Remove@Broker`
|Body  |`Wallet`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Broker`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`Path`    |string| Path from [`Save@Notifier`](<../Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)
|