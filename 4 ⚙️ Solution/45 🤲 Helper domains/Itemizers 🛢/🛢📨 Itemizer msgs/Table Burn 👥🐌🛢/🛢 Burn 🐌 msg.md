# 👥🐌🛢 Burn

> Part of [Itemizer 🛢 helper](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>)

> Purpose

* Destroys an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
    * as requested by a [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃 Talker/😃🤲 Talker helper.md>)

## Async Message
```yaml
Header:
    From: any-talker.dom
    To: any-itemizer.dom
    Subject: Burn@Itemizer

Body:
    Set: MyTable
```

|Object|Property|Type|Description
|-|-|-|-
| Header    |`From`|text| [Talker 😃 domain](<../../../../35 💬 Chats/Talkers 😃/😃 Talker/😃🤲 Talker helper.md>) name
|           |`To`|text| [Itemizer 🛢 domain](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>) name
|           | `Subject`     | string    | `Destroy@Itemizer`
| Body      | `Set`     | string    | Name of the table
|
