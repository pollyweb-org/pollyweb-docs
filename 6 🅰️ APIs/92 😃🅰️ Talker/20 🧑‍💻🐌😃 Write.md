# 🧑‍💻🐌☁️ Write @ Hoster

> Implements [Hoster ☁️ helper domain](<../../9 😃 Talkers/90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>)

> Part of [😃⏩🧑‍💻 Wait @ Talker](<../../5 ⏩ Flows/79 😃⏩ Talkers/30 😃⏩🧑‍💻 Wait ⏸️.md>) flow

> Paired with [`Read@Talker`](<10 🧑‍💻🚀😃 Read.md>) method

> Writes to a [$Placeholder 💾](<../../9 😃 Talkers/30 🗃️ Talker data/10 💾 $Placeholder.md>)

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-host.com
    To: any-hoster.com
    Subject: Write@Talker

Body:
    ChatID: <chat-uuid>
    Placeholder: $p
    Value: {A:1, B:2}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) name
|           | `To`          | string    | [Hoster ☁️ domain](<../../9 😃 Talkers/90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>) name
|           | `Subject`     | string    | `Write@Talker`
| Body      | `ChatID`      | uuid      | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ID
|           | `Placeholder` | string    | [$Placeholder 💾](<../../9 😃 Talkers/30 🗃️ Talker data/10 💾 $Placeholder.md>) name
|           | `Value`       | any    | Any value to write
|