# 👥🚀🛢 Read @ Itemizer

> Flow
* Part of [Itemizer 🛢 helper](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>)

> Implements
* Implements the [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) command

> Purpose

* Retrieves an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
    * as requested by a [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)


## Synchronous Call 🚀

```yaml
Header:
    From: any-talker.dom
    To: any-itemizer.dom
    Subject: Read@Itemizer

Body:
    Set: MySet
    Key: [ MyKey1, Key2 ]
```

|Object|Property|Type|Description
|-|-|-|-
| Header    |`From`|text| [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>) from [`Build@Itemizer`](<../Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           |`To`|text| [Itemizer 🛢](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>) from [`Build@Itemizer`](<../Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           | `Subject`     | string    | `Read@Itemizer`
| Body      | `Set`     | string    | Set from [`Build@Itemizer`](<../Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           | `Key`        | string    | Key from [`Save@Itemizer`](<../Item Save 👥🚀🛢/🛢 Save 🚀 call.md>)
|


<br/>

## Synchronous Response

```yaml
:{Item}:
.Table: MyTable
.Version: <version-uuid>
```

||Property|Type|Description
|-|-|-|-
|| `Item`        | object    | [Item 🛢](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) saved on the [`Save@Itemizer` 📨 msg](<../Item Save 👥🚀🛢/🛢 Save 🚀 call.md>)
|| `.Table`   |text| Table name for the [`SAVE` 📃 script](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE 📃 script.md>)
|| `.Version` | uuid   | Version for the [`Save@Itemizer` 📨 msg](<../Item Save 👥🚀🛢/🛢 Save 🚀 call.md>)
|