
<!-- Docs: https://quip.com/PCunAKUqSObO/-Notifier -->
<!-- Code: -->
<!-- Test: -->


# 🤵🐌📣 Updated @ Notifier

> The Broker domain tells the [Notifier 📣 domain](<../../📣 Notifier domain.md>) that there was an update and they need to refresh the user experience.

> Used in:
> <br/>• [🤵⏩🧑‍🦰 Update Binds 🔗](<../../../../../5 ⏩ Flows/10 🤵⏩ Brokers/06 🤵⏩🧑‍🦰 Update Binds 🔗.md>)
> <br/>• [🤵⏩🧑‍🦰 Update tokens](<../../../../../5 ⏩ Flows/10 🤵⏩ Brokers/08 🤵⏩🧑‍🦰 Update Tokens 🎫.md>)
> <br/>• [🤵⏩🧑‍🦰 Update chats 💬](<../../../../../5 ⏩ Flows/10 🤵⏩ Brokers/04 🤵⏩🧑‍🦰 Update Chats 💬.md>)

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
|Header|`From`|string | [Broker 🤵 domain](<../../../../45 🤲 Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) name
||`To`|string| [Notifier 📣](<../../📣 Notifier domain.md>) from [`Onboard@Broker`](<../../../../../6 🅰️ APIs/15 🤵🅰️ Broker/10 🤵🅰️ Wallets 🧑‍🦰/11 📣🚀🤵 Onboard.md>)
||`Subject`|string|`Updated@Notifier`
|Body  |`WalletID` |uuid  | [Wallet 🧑‍🦰](<../../../01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) ID from [`Onboard@Broker`](<../../../../../6 🅰️ APIs/15 🤵🅰️ Broker/10 🤵🅰️ Wallets 🧑‍🦰/11 📣🚀🤵 Onboard.md>)
|      |`Updates`   |enum  | `CHATS` `BINDS` `TOKENS`
|