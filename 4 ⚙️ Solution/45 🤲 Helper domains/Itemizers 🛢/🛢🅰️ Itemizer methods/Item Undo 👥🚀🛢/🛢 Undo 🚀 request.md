# 👥🚀🛢 Undo @ Itemizer

> Part of [Itemizer 🛢 helper](<../../🛢🤲 Itemizer helper.md>)

> Implements the [`UNDO`](<../../../../35 💬 Chats/Scripts 📃/📃 for datasets 🪣/UNDO ↩️/↩️ UNDO ⌘ cmd.md>) command.


<br/>

## Synchronous Request

```yaml
Header:
    From: any-talker.dom
    To: any-itemizer.dom
    Subject: Undo@Itemizer

Body:
    Script: MyScript
    Set: MySet
    Key: [ MyKey1, MyKey2 ]
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃 Talker role.md>) from [`Delete@Itemizer`](<../Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>)
|           | `To`          | string    | [Itemizer 🛢](<../../🛢🤲 Itemizer helper.md>) from [`Delete@Itemizer`](<../Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>)
|           | `Subject`     | string    | `Undo@Itemizer`
| Body    | `Script`     | string    | [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 commands ⌘/Script 📃/📃 Script.md>) for traceability
|         | `Set`    | string  | `Set` from [`Delete@Itemizer`](<../Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>) 
|         | `Key`     | string[]  | `Key` from [`Delete@Itemizer`](<../Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>)
|