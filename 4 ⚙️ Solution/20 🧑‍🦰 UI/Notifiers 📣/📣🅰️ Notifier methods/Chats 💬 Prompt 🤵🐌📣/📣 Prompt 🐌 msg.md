# 🤵🐌📣 Prompt @ Notifier

> Implements the [Notifier 📣 domain](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>)


> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) flow, succeeded by

*  [`Prompted@Host` 🅰️ method](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>)
*  [`Reply@Host` 🅰️ method](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>)
*  [`Download@Host` 🅰️ method](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Download 🧑‍🦰🚀🤗/🤗 Download 🚀 request.md>)

> Purpose
* [Broker 🤵 domains](<../../../Brokers 🤵/🤵 Broker helper/Broker 🤵 helper 🤲.md>) 
    * forward   [Prompts 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) 
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
    Sender: any-agent.com
    Hook: <hook-uuid>
    Format: CONFIRM
    Emoji: 😃
```
<!-- TODO: Sender is not enough, we all so need a Sender$ and an icon, so we'll need to inform about new participants when they join -->

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|domain| [Broker 🤵](<../../../Brokers 🤵/🤵 Broker helper/Broker 🤵 helper 🤲.md>)  | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`To`|domain| [Notifier 📣](<../../📣 Notifier domain/📣 Notifier 👥 domain.md>) | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`Subject`|string|`Prompt@` | 
|Body  |`Wallet` |uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) ID | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|      |`Chat`  |uuid  | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Converse@`](<../Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>)
|      |`Sender`  |domain| [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) name | [`Prompt@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
|      |`Hook`|uuid  | [Prompt 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) ID | [`Prompt@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>) | [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>) [`Reply@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>)
|| [`Format`](<../../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>)  | string | [Prompt 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) format | [`Prompt@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
|| [`Emoji`](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt input features/😶⌘ EMOJI cmd.md>) | string | [Prompt 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>)   emoji | [`Prompt@`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
|

<br/>
