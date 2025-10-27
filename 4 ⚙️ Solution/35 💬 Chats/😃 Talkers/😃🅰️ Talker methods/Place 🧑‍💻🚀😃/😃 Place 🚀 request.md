# 🧑‍💻🚀😃 Write @ Hoster

> Implementation 
* Implements [Hoster ☁️ helper domain](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>)
* Implemented by the [`Place` 📃 handler](<😃 Place 📃 handler.md>)

> Flow
* Part of [`Async` ⏩ flow](<../../😃⏩ Talker flows/Async Tasks 😃⏩📦/😃 Async ⏩ flow.md>) flow
* Paired with the [`Placed@Talker` 🅰️ method](<../Placed 🧑‍💻🚀😃/😃 Placed 🚀 request.md>)

> Purpose 
* Writes a value to a [Placeholder 🧠](<../../😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>).


<br/>

## Async Message 🐌


```yaml
Header:
    From: any-host.dom
    To: any-hoster.dom
    Subject: Place@Talker

Body:
    Chat: <chat-uuid>
    Placeholder: $p
    Value: {A:1, B:2}
    Reason: Any reason...
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) name
|           | `To`          | string    | [Hoster ☁️ domain](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) name
|           | `Subject`     | string    | `Place@Talker`
| Body      | `Chat`      | uuid      | [Chat 💬](<../../../💬 Chats/💬 Chat.md>) ID
|           | `Placeholder` | string    | [Placeholder 🧠](<../../😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) name
|           | `Value`       | any    | Any value to write
|           | `Reason`      | string | For traceability
|