# 👥🐌🛢 Destroy

> Part of [Itemizer 🛢 helper](<../../🛢🤲 Itemizer helper.md>)

> Purpose

* Destroys an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
    * as requested by a [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)

## Async Message
```yaml
Header:
    From: any-talker.dom
    To: any-itemizer.dom
    Subject: Burn@Itemizer

Body:
    Table: MyTable
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Talker 😃 domain](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>) name
|           | `To`          | string    | [Itemizer 🛢 domain](<../../🛢🤲 Itemizer helper.md>) name
|           | `Subject`     | string    | `Destroy@Itemizer`
| Body      | `Table`     | string    | Name of the table
|