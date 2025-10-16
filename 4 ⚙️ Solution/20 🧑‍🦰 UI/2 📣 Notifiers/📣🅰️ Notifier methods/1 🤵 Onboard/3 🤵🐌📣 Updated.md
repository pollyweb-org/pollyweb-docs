
<!-- Docs: https://quip.com/PCunAKUqSObO/-Notifier -->
<!-- Code: -->
<!-- Test: -->


# 🤵🐌📣 Updated @ Notifier

> The Broker domain tells the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>) that there was an update and they need to refresh the user experience.

> Used in:
> <br/>• [🤵⏩🧑‍🦰 Update Binds 🔗](<../../../3 🤵 Brokers/🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Binds 🔗.md>)
> <br/>• [🤵⏩🧑‍🦰 Update tokens](<../../../3 🤵 Brokers/🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Tokens 🎫.md>)
> <br/>• [🤵⏩🧑‍🦰 Update chats 💬](<../../../3 🤵 Brokers/🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Chats 💬.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.com
    To: any-notifier.com
    Subject: Updated@Notifier
Body:
    WalletID: <wallet-uuid>
    Updates: [ CHATS, BINDS ]
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵 domain](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) name
||`To`|string| [Notifier 📣](<../../📣👥 Notifier domain.md>) from [`Onboard@Broker`](<../../../3 🤵 Brokers/🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/📣🚀🤵 Onboard.md>)
||`Subject`|string|`Updated@Notifier`
|Body  |`WalletID` |uuid  | [Wallet 🧑‍🦰](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>) ID from [`Onboard@Broker`](<../../../3 🤵 Brokers/🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/📣🚀🤵 Onboard.md>)
|      |`Updates`   |enum  | `CHATS` `BINDS` `TOKENS`
|