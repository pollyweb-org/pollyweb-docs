# 🤵🐌📣 Prompt @ Notifier

> Implements the [Notifier 📣 domain](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>)


> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) flow, succeeded by

*  [`Prompted@Host` 🅰️ method](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>)
*  [`Reply@Host` 🅰️ method](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>)
*  [`Download@Host` 🅰️ method](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Download 🧑‍🦰🚀🤗/🤗 Download 🚀 call.md>)

> Purpose
* [Broker 🤵 domains](<../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) 
    * forward   [Prompts 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) 
    * from [Host 🤗 domains](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) 
    * to [Notifier 📣 domains](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>).


## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Prompt@Notifier
    
Body:
    Wallet: <wallet-uuid>
    Chat: <chat-uuid>
    Sender: any-agent.dom
    Hook: <hook-uuid>
    Format: CONFIRM
    Emoji: 😃
```
<!-- TODO: Sender is not enough, we all so need a Sender$ and an icon, so we'll need to inform about new participants when they join -->

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|string| [Broker 🤵](<../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>)  | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
||`To`|string| [Notifier 📣](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
||`Subject`|string|`Prompt@` | 
|Body  |`Wallet` |uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) ID | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
|      |`Chat`  |uuid  | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Open@`](<../Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>)
|      |`Sender`  |string| [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) name | [`Prompt@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
|      |`Hook`|uuid  | [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) ID | [`Prompt@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>) | [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>) [`Reply@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>)
|| [`Format`](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>)  | string | [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) format | [`Prompt@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
|| [`Emoji`](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/😶⌘ EMOJI cmd.md>) | string | [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>)   emoji | [`Prompt@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
|

<br/>
