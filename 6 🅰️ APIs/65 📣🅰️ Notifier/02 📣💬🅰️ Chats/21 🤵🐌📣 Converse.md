# 🤵🐌📣 Converse @ Notifier

> [Broker 🤵 domains](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) tell [Wallet 🧑‍🦰 apps](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) about a new [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).

> Used in [🤵⏩🧑‍🦰 Converse @ Broker](<../../../5 ⏩ Flows/10 🤵⏩ Brokers/03 🤵⏩🧑‍🦰 Converse 💬.md>) 

<br/>

```yaml
Header:
    From: any-broker.com
    To: any-notifier.com
    Subject: Converse@Notifier
    
Body:
    WalletID: <wallet-uuid>
    ChatID: <chat-uuid>
    PrivateKey: <private-key>
    Host: another-domain.com
    Name: Any Other Domain, Inc.
    SmallIcon: <base64>
    BigIcon: <base46>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) from [`Assess@Broker`](<../../15 🤵🅰️ Broker/20 🤵🅰️ Locators/01 🧑‍🦰🐌🤵 Assess.md>)
||`To`|string| [Notifier 📣](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) from [`Onboard@Broker`](<../../15 🤵🅰️ Broker/10 🤵🅰️ Wallets 🧑‍🦰/11 📣🚀🤵 Onboard.md>)
||`Subject`|string|`Converse@Notifier`
|Body  |`WalletID` |uuid  | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) ID from [`Assess@Broker`](<../../15 🤵🅰️ Broker/20 🤵🅰️ Locators/01 🧑‍🦰🐌🤵 Assess.md>)
|      |`ChatID`   |uuid  | New [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ID on the [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
|      |`Host`     |string| [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) name
|      |`Name`     |string| Name from [`Translate@Graph`](<../../45 🕸🅰️ Graph/06 👥🚀🕸 Translate.md>)
|      |`SmallIcon`|string   | Small icon from [`Identity@Graph`](<../../45 🕸🅰️ Graph/04 👥🚀🕸 Identity.md>)
|      |`BigIcon`  |string   | Big icon from [`Identity@Graph`](<../../45 🕸🅰️ Graph/04 👥🚀🕸 Identity.md>)
|      |`PrivateKey`|string  | For [`Prompted@`](<../../50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) [`Reply@`](<../../50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) [`Download@`](<../../50 🤗🅰️ Host/06 🧑‍🦰🚀🤗 Download.md>)
|