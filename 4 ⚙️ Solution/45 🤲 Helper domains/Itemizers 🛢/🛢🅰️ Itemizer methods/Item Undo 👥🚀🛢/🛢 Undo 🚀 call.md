# 👥🚀🛢 Undo @ Itemizer

> Part of [Itemizer 🛢 helper](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>)

> Implements the [`UNDO`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/UNDO ↩️/↩️ UNDO ⌘ cmd.md>) command.


<br/>

## Synchronous Call 🚀

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
| Header    |`From`|text| [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>) from [`Delete@Itemizer`](<../Item Delete 👥🚀🛢/🛢 Delete 🚀 call.md>)
|           |`To`|text| [Itemizer 🛢](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>) from [`Delete@Itemizer`](<../Item Delete 👥🚀🛢/🛢 Delete 🚀 call.md>)
|           | `Subject`     | string    | `Undo@Itemizer`
| Body    | `Script`     | string    | [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) for traceability
|         | `Set`    | string  | `Set` from [`Delete@Itemizer`](<../Item Delete 👥🚀🛢/🛢 Delete 🚀 call.md>) 
|         | `Key`     | string[]  | `Key` from [`Delete@Itemizer`](<../Item Delete 👥🚀🛢/🛢 Delete 🚀 call.md>)
|