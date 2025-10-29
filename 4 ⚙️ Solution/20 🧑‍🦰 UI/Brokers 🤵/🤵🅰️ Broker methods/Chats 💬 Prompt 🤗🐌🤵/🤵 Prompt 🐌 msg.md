<!-- Docs: https://quip.com/FNbzAVSVu9z6#temp:C:RCPf6c15c5e6e2d47c294917a750 -->

# 🤗🐌🤵 Prompt @ Broker

<!-- TODO: create the handler script -->
<!-- TODO: create the script diagram -->

> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) flow.

> Purpose
* The [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) 
  * forwards the [Prompt 🤔](<../../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) 
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
```


|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`     | string  | [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) |[`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`To`       | string  | [Broker 🤵](<../../🤵🤲 Broker helper.md>)|[`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Subject` | string | `Prompt@Broker`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Hook` | uuid    | [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) callback || [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>)
||`Expires`| timestamp | Cache expiration || [`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>) 
|