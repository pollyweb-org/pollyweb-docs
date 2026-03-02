# 🤗🐌🤵 Prompt @ Broker

<!-- TODO: create the handler script -->
<!-- TODO: create the script diagram -->

> Implementation
* Implemented by the [`Prompt` 📃 handler](<🤵 Prompt 📃 handler.md>)
> Flow
* Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) flow.

> Purpose
* The [Broker 🤵 domain](<../../🤵/🤵 Broker 🤲 helper.md>) 
  * forwards the [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) 
  * to the [Notifier 📣 domain](<../../../Notifiers 📣/📣/📣 Notifier 👥 domain.md>).

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-host.dom
    To: any-broker.dom
    Subject: Prompt@Broker
  
Body:
    Prompt: <prompt-uuid>
    Chat: <chat-uuid>
    Expires: 2023-04-01T05:00:30.001000Z
    Format: CONFIRM
    Emoji: 😃
```


|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|text| [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) |[`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`To`|string  | [Broker 🤵](<../../🤵/🤵 Broker 🤲 helper.md>)|[`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Subject` |text| `Prompt@Broker`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Prompt` | uuid    | [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) callback || [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>)
||`Expires`| time | Cache expiration || [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>) 
|| [`Format`](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>)  |text| [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) format || [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>) 
|| [`Emoji`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/EMOJI 😶/😶 EMOJI ⌘ cmd.md>) |text| [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>)   emoji || [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>) 
|

## FAQ

1. **Why are `Format` and `Emoji` the only Prompt properties provided?**

    For privacy reasons, [Broker 🤵 domains](<../../🤵/🤵 Broker 🤲 helper.md>) are not allowed to see the contents of [Prompts 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) sent from [Host 🤗 domains](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) to [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
    * However, [Broker 🤵 domains](<../../🤵/🤵 Broker 🤲 helper.md>) are responsible for enforcing the standardization of [emojis](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/EMOJI 😶/😶 EMOJI ⌘ cmd.md>) for the benefit of users.  
    * Thus, only these two [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) properties are provided directly via the [`Prompt@Broker` 🐌 msg](<🤵 Prompt 🐌 msg.md>).
    * All other [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) properties are provided via the [`Prompted@Host` 🚀 call](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>).

    ---
    <br/>