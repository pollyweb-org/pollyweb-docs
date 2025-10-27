<!-- Docs: https://quip.com/FNbzAVSVu9z6#temp:C:RCPf6c15c5e6e2d47c294917a750 -->

# 🤗🐌🤵 Prompt @ Broker

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
  Prompt: <prompt-uuid>
  Expires: 2023-04-01T05:00:30.001000Z
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)
||`To`       | string  | [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>)
||`Subject` | string | `Prompt@Broker`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Prompt` | uuid    | Callback to [`Prompted@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>)
||`Expires`| timestamp | Expiration of [`Prompted@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>) cache
|