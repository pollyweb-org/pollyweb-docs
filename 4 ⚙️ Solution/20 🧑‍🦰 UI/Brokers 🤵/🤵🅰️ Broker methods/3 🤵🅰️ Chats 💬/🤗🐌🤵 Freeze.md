# 🤗🐌🤵 Freeze @ Broker

* The [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
    * freezes changes to any pre.

* Used in:
    * [❄️ Talker `FREEZE` command](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...methods/FREEZE ❄️ msg.md>)
    * [❄️ Host Freeze ⏩ flow](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Freeze ❄️.md>)

<br/> 

## Async Message 🐌

```yaml
Header:
    From: any-host.dom
    To: any-broker.dom
    Subject: Freeze@Broker
    
Body:
    Chat: <chat-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)
||`To`       | string  | [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>)
||`Subject` | string | `Freeze@Broker`
|Body|`Chat`   | uuid    | ID of the [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) 
|