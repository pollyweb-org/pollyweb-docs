# 🤵🐌📣 Converse @ Notifier

> Implements the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>)


> [Broker 🤵 domains](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) tell [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) about a new [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>).

> Used in [🤵⏩🧑‍🦰 Converse @ Broker](<../../../Brokers 🤵/🤵⏩ Broker flows/Converse 💬/🤵⏩🧑‍🦰 Converse 💬.md>) 

<br/>

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Converse@Notifier
    
Body:
    Wallet: <wallet-uuid>
    Hook: <hook-uuid>
    Chat: <chat-uuid>
    PrivateKey: <private-key>
    Host: another-domain.com
    Host$: Any Other Domain, Inc.
    SmallIcon: <base64>
    BigIcon: <base46>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) from [`Assess@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/2 ...for Locators 🔆/Assess/🧑‍🦰🐌🤵 Assess.md>)
||`To`|string| [Notifier 📣](<../../📣👥 Notifier domain.md>) from [`Onboard@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/1 ...for Wallets 🧑‍🦰/Onboard/📣🚀🤵 Onboard.md>)
||`Subject`|string|`Converse@Notifier`
|Body  |`Wallet` |uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) from [`Assess@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/2 ...for Locators 🔆/Assess/🧑‍🦰🐌🤵 Assess.md>) [`Pop@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/3 ...for Chats 💬/Pop 🐌/.📎 Assets/🤵📃 Pop 💬 handler.md>)
|       | `Hook`| uuid | `Hook` from [`Assess@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/2 ...for Locators 🔆/Assess/🧑‍🦰🐌🤵 Assess.md>) [`Pop@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/3 ...for Chats 💬/Pop 🐌/.📎 Assets/🤵📃 Pop 💬 handler.md>)
|      |`Chat`   |uuid  | New [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID on the [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>)
|      |`Host`     |string| [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) name
|      |`Host$`     |string| `Domain` from [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|      |`SmallIcon`|string   | `SmallIcon` from [`Identity@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)
|      |`BigIcon`  |string   | `BigIcon` from [`Identity@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)
|      |`PrivateKey`|string  | For [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>) [`Reply@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>) [`Download@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Download.md>)
|