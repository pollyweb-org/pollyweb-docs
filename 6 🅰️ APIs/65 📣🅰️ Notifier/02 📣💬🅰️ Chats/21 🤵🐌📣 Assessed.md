<!-- #TODO -->

<!-- Docs: -->
<!-- Code: -->
<!-- Test: -->


# 🤵🐌📣 Assessed @ Notifier

> Brokers tell Wallets about a new chat.

> Used in [🤵⏩🧑‍🦰 Assessed @ Broker](<../../../5 ⏩ Flows/10 🤵⏩ Brokers/01 🤵⏩🧑‍🦰 Assessed.md>) 

<br/>

```yaml
Header:
    From: any-broker.com
    To: any-notifier.com
    Subject: Assessed@Notifier
Body:
    WalletID: <wallet-uuid>
    ChatID: <chat-uuid>
    Host: another-domain.com
    Name: Any Other Domain, Inc.
    SmallIcon: 
    BigIcon: https://another-domain.com/big-icon.png
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
||`To`|string| [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) name
||`Subject`|string|`Assessed@Notifier`
|Body  |`WalletID` |uuid  | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) ID from [Onboard@](<../01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
|      |`ChatID`   |uuid  | Chat ID on the Broker domain
|      |`Host`     |string| [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/05 💬 Chats/04 🤗🎭 Host role.md>) name
|      |`Name`     |string| Friendly translated name
|      |`SmallIcon`|URL   | Location of the small icon
|      |`BigIcon`  |URL   | Location of the big icon
|