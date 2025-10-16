# 🤵🐌📣 Converse @ Notifier

> [Broker 🤵 domains](<../../../03 🤵 Brokers/🤵🤲 Broker helper.md>) tell [Wallet 🧑‍🦰 apps](<../../../01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) about a new [Chat 💬](<../../../../35 Chats/💬 Chats/💬 Chat.md>).

> Used in [🤵⏩🧑‍🦰 Converse @ Broker](<../../../03 🤵 Brokers/🤵⏩ Broker flows/🤵⏩🧑‍🦰 Converse 💬.md>) 

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
|Header|`From`|string | [Broker 🤵](<../../../03 🤵 Brokers/🤵🤲 Broker helper.md>) from [`Assess@Broker`](<../../../03 🤵 Brokers/🤵🅰️ Broker methods/2 🤵🅰️ Locators/🧑‍🦰🐌🤵 Assess.md>)
||`To`|string| [Notifier 📣](<../../📣 Notifier domain.md>) from [`Onboard@Broker`](<../../../03 🤵 Brokers/🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/📣🚀🤵 Onboard.md>)
||`Subject`|string|`Converse@Notifier`
|Body  |`WalletID` |uuid  | [Wallet 🧑‍🦰](<../../../01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) ID from [`Assess@Broker`](<../../../03 🤵 Brokers/🤵🅰️ Broker methods/2 🤵🅰️ Locators/🧑‍🦰🐌🤵 Assess.md>)
|      |`ChatID`   |uuid  | New [Chat 💬](<../../../../35 Chats/💬 Chats/💬 Chat.md>) ID on the [Broker 🤵](<../../../03 🤵 Brokers/🤵🤲 Broker helper.md>)
|      |`Host`     |string| [Host 🤗 domain](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) name
|      |`Name`     |string| Name from [`Translate@Graph`](<../../../../45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|      |`SmallIcon`|string   | Small icon from [`Identity@Graph`](<../../../../45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)
|      |`BigIcon`  |string   | Big icon from [`Identity@Graph`](<../../../../45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)
|      |`PrivateKey`|string  | For [`Prompted@`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>) [`Reply@`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>) [`Download@`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Download.md>)
|