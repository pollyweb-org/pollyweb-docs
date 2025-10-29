# 🤵🐌📣 Converse @ Notifier

> Implements the [Notifier 📣 domain](<../../📣👥 Notifier domain.md>)


> [Broker 🤵 domains](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) tell [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) about a new [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>).

> Used in [🤵⏩🧑‍🦰 Converse @ Broker](<../../../Brokers 🤵/🤵⏩ Broker flows/Converse 🤵⏩💬/🤵 Converse ⏩ flow.md>) 

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

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|string | [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) | [`Assess@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)
||`To`|string| [Notifier 📣](<../../📣👥 Notifier domain.md>) | [`Onboard@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 request.md>)
||`Subject`|string|`Converse@*`
|Body  |`Wallet` |uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) | [`Assess@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>) [`Pop@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Pop 🧑‍🦰🐌🤵/🤵 Pop 📃 handler.md>)
|       | `Hook`| uuid | `Hook` | [`Assess@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>) [`Pop@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Pop 🧑‍🦰🐌🤵/🤵 Pop 📃 handler.md>)
|      |`Chat`   |uuid  | New [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>)  || [`Prompt@`](<../Chats 💬 Prompt 🤵🐌📣/📣 Prompt 🐌 msg.md>)
|      |`Host`     |string| [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
|      |`Host$`     |string| `Domain` | [`Translate@`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|      |`SmallIcon`|string   | `SmallIcon` | [`Identity@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)
|      |`BigIcon`  |string   | `BigIcon` | [`Identity@`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)
|      |`PrivateKey`|string  | For signing || [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>) [`Reply@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>) [`Download@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Download 🧑‍🦰🚀🤗/🤗 Download 🚀 request.md>)
|