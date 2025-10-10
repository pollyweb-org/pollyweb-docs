
<!-- Docs: https://quip.com/PCunAKUqSObO/-Notifier -->
<!-- Code: -->
<!-- Test: -->


# 🤵🐌📣 Updated @ Notifier

> The Broker domain tells the [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) that there was an update and they need to refresh the user experience.

> Used in:
> <br/>• [🤵⏩🧑‍🦰 Update Binds 🔗](<../../../5 ⏩ Flows/10 🤵⏩ Brokers/03 🤵⏩🧑‍🦰 Update binds.md>)
> <br/>• [🤵⏩🧑‍🦰 Update tokens](<../../../5 ⏩ Flows/10 🤵⏩ Brokers/04 🤵⏩🧑‍🦰 Update tokens.md>)
> <br/>• [🤵⏩🧑‍🦰 Update chats 💬](<../../../5 ⏩ Flows/10 🤵⏩ Brokers/05 🤵⏩🧑‍🦰 Update chats.md>)

<br/>

## 🐌 Async Message

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
|Header|`From`|string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
||`To`|string| [Notifier 📣](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) from [`Onboard@Broker`](<../../15 🤵🅰️ Broker/10 🤵🅰️ Wallets 🧑‍🦰/11 📣🚀🤵 Onboard.md>)
||`Subject`|string|`Updated@Notifier`
|Body  |`WalletID` |uuid  | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) ID from [`Onboard@Broker`](<../../15 🤵🅰️ Broker/10 🤵🅰️ Wallets 🧑‍🦰/11 📣🚀🤵 Onboard.md>)
|      |`Updates`   |enum  | `CHATS` `BINDS` `TOKENS`
|