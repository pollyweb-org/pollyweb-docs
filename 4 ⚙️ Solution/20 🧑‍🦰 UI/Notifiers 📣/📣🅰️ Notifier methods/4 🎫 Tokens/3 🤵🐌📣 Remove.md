
# 🤵🐌📣 Remove @ [Notifier](<../../📣👥 Notifier domain.md>)

> Implements the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>)

> Used in [🧑‍🦰👉🤵 Remove token](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/💬🤵 Remove 🎫 chat.md>).

> Called by the [`TokenTimeout` 📃 script](<../../../Brokers 🤵/🤵📃 Broker scripts/...triggers/🤵📃 Token 🎫 timeout.md>)


<br/>

## Async Message 🐌
```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Remove@Notifier

Body:
    Wallet: <wallet-id>
    Path: /storage/nlweb/tokens/<issuer>/<token-uuid>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) from [`Onboard@Broker`](<../1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
||`To`|string| [Notifier 📣](<../../📣👥 Notifier domain.md>) from [`Onboard@Broker`](<../1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
||`Subject`|string|`Remove@Broker`
|Body  |`Wallet`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Broker`](<../1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
||`Path`    |string| Path from [`Save@Notifier`](<1 🤵🐌📣 Save.md>)
|