# 🤗🐌🤵 Freeze @ Broker

* The [Host 🤗 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) 
    * freezes changes to any pre.

* Used in:
    * [❄️ Talker `FREEZE` command](<../../../9 😃 Talkers/60 ⏩ Msg flows/42 ❄️ FREEZE msg.md>)
    * [❄️ Host Freeze ⏩ flow](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/06 🤗⏩🧑‍🦰 Freeze ❄️.md>)

<br/> 

## Async Message 🐌

```yaml
Header:
    From: any-host.com
    To: any-broker.com
    Subject: Freeze@Broker
    
Body:
    ChatID: <chat-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | [Host 🤗 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>)
||`To`       | string  | [Broker 🤵 domain](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>)
||`Subject` | string | `Freeze@Broker`
|Body|`ChatID`   | uuid    | ID of the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) 
|