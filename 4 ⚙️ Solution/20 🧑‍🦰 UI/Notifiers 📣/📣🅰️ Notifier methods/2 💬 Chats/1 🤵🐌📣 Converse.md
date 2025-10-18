# 🤵🐌📣 Converse @ Notifier

> [Broker 🤵 domains](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) tell [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) about a new [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>).

> Used in [🤵⏩🧑‍🦰 Converse @ Broker](<../../../Brokers 🤵/🤵⏩ Broker flows/🤵⏩🧑‍🦰 Converse 💬.md>) 

<br/>

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Converse@Notifier
    
Body:
    Wallet: <wallet-uuid>
    Reference: <reference-uuid>
    Chat: <chat-uuid>
    PrivateKey: <private-key>
    Host: another-domain.com
    Name: Any Other Domain, Inc.
    SmallIcon: <base64>
    BigIcon: <base46>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) from [`Assess@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/2 🤵🅰️ Locators/🧑‍🦰🐌🤵 Assess.md>)
||`To`|string| [Notifier 📣](<../../📣👥 Notifier domain.md>) from [`Onboard@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/📣🚀🤵 Onboard.md>)
||`Subject`|string|`Converse@Notifier`
|Body  |`Wallet` |uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) ID from [`Assess@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/2 🤵🅰️ Locators/🧑‍🦰🐌🤵 Assess.md>)
|       | `Reference`| uuid | Reference from [`Assess@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/2 🤵🅰️ Locators/🧑‍🦰🐌🤵 Assess.md>)
|      |`Chat`   |uuid  | New [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID on the [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>)
|      |`Host`     |string| [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) name
|      |`Name`     |string| Name from [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|      |`SmallIcon`|string   | Small icon from [`Identity@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)
|      |`BigIcon`  |string   | Big icon from [`Identity@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)
|      |`PrivateKey`|string  | For [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>) [`Reply@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>) [`Download@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Download.md>)
|