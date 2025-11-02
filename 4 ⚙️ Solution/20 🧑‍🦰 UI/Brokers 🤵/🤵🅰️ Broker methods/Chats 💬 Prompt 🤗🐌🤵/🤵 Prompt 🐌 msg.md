<!-- Docs: https://quip.com/FNbzAVSVu9z6#temp:C:RCPf6c15c5e6e2d47c294917a750 -->

# 🤗🐌🤵 Prompt @ Broker

<!-- TODO: create the handler script -->
<!-- TODO: create the script diagram -->

> Implementation
* Implemented by the [`Prompt` 📃 handler](<🤵 Prompt 📃 handler.md>)
> Flow
* Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) flow.

> Purpose
* The [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) 
  * forwards the [Prompt 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) 
  * to the [Notifier 📣 domain](<../../../Notifiers 📣/📣👥 Notifier domain.md>).

<br/>

## Async Message 🐌

```yaml
Header:
  From: any-host.dom
  To: any-broker.dom
  Subject: Prompt@Broker
  
Body:
  Chat: <chat-uuid>
  Hook: <hook-uuid>
  Expires: 2023-04-01T05:00:30.001000Z
  Format: CONFIRM
  Emoji: 😃
```


|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|domain| [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) |[`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`To`|string  | [Broker 🤵](<../../🤵🤲 Broker helper.md>)|[`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Subject` | string | `Prompt@Broker`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Hook` | uuid    | [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) callback || [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>)
||`Expires`| time | Cache expiration || [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>) 
|| [`Format`](<../../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>)  | string | [Prompt 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) format || [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>) 
|| [`Emoji`](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt input features/😶⌘ EMOJI cmd.md>) | string | [Prompt 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>)   emoji || [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>) 
|

## FAQ

1. **Why are `Format` and `Emoji` the only Prompt properties provided?**

    For privacy reasons, [Broker 🤵 domains](<../../🤵🤲 Broker helper.md>) are not allowed to see the contents of [Prompts 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) sent from [Host 🤗 domains](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) to [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).
    * However, [Broker 🤵 domains](<../../🤵🤲 Broker helper.md>) are responsible for enforcing the standardization of [emojis](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt input features/😶⌘ EMOJI cmd.md>) for the benefit of users.  
    * Thus, only these two [Prompt 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) properties are provided directly via the [`Prompt@Broker` 🅰️ method](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>).
    * All other [Prompt 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) properties are provided via the [`Prompted@Host` 🅰️ method](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>).

    ---
    <br/>