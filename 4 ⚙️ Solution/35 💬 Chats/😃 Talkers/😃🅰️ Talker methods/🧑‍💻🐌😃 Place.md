# 🧑‍💻🐌☁️ Write @ Hoster

> Implements [Hoster ☁️ helper domain](<../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>)

> Part of [😃⏩🧑‍💻 Wait @ Talker](<../😃⏩ Talker flows/😃⏩🧑‍💻 Wait ⏸️.md>) flow

> Paired with [`Placed@Talker`](<🧑‍💻🚀😃 Placed.md>) message

* Writes a value to a [$Placeholder 💾](<../😃💾 Talker data/$Placeholder 💾.md>).
* [$Placeholder 💾](<../😃💾 Talker data/$Placeholder 💾.md>) names must to start with a letter.

<br/>

## Async Message 🐌


```yaml
Header:
    From: any-host.dom
    To: any-hoster.dom
    Subject: Place@Talker

Body:
    ChatID: <chat-uuid>
    Placeholder: $p
    Value: {A:1, B:2}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) name
|           | `To`          | string    | [Hoster ☁️ domain](<../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) name
|           | `Subject`     | string    | `Place@Talker`
| Body      | `ChatID`      | uuid      | [Chat 💬](<../../💬 Chats/💬 Chat.md>) ID
|           | `Placeholder` | string    | [$Placeholder 💾](<../😃💾 Talker data/$Placeholder 💾.md>) name
|           | `Value`       | any    | Any value to write
|