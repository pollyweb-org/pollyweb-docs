# 🧑‍💻🐌☁️ Write @ Hoster

> Paired with [Read@Hoster](<10 🧑‍💻🚀☁️ Read.md>)

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-host.com
    To: any-hoster.com
    Subject: Write@Hoster

Body:
    ChatID: <chat-uuid>
    Placeholder: $p
    Value: {A:1, B:2}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) name
|           | `To`          | string    | [Talker 😃 domain](<../../9 😃 Talkers/10 📘 Talker specs/02 😃🛠️ Talker helper.md>) name
|           | `Subject`     | string    | `Write@Talker`
| Body      | `ChatID`      | uuid      | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ID
|           | `Placeholder` | string    | [$Placeholder 💾](<../../9 😃 Talkers/30 🗃️ Talker data/10 💾 $Placeholder.md>) name
|           | `Value`       | any    | Any value to write
|