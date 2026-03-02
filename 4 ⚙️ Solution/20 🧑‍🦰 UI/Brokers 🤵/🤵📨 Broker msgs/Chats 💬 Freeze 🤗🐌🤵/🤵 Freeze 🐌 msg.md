# 🤗🐌🤵 Freeze @ Broker

> Implementation
* Implements a [Broker 🤵 domain](<../../🤵/🤵 Broker 🤲 helper.md>)
* Implemented by the [`Freeze` 📃 handler](<🤵 Freeze 📃 handler.md>)

> Purpose
* A [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) 
    * freezes changes to any previous inputs in the [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

> Used by
* [❄️ `FREEZE` command](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/FREEZE ❄️/❄️ FREEZE ⌘ cmd.md>)
* [❄️ `Freeze` ⏩ flow](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Freeze 🤗⏩❄️/🤗 Freeze ⏩ flow.md>)


## Async Message 🐌

```yaml
Header:
    From: any-host.dom
    To: any-broker.dom
    Subject: Freeze@Broker
    
Body:
    Chat: <chat-uuid>
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|text| [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`To`|string  | [Broker 🤵](<../../🤵/🤵 Broker 🤲 helper.md>) | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Subject` |text| `Freeze@Broker`
|Body|`Chat`   | uuid    | ID of the [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) | [`Frozen@Notifier`](<../../../Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Frozen 🤵🐌📣/📣 Frozen 🐌 msg.md>)
|