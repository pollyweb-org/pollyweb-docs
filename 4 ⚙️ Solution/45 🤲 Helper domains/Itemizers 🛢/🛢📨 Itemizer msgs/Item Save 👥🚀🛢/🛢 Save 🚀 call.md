# 👥🚀🛢 Save @ Itemizer

> Part of [Itemizer 🛢 helper](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>)

> Implements the [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) commands from [Talker 😃 domains](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>).

> Purpose

* Saves an item
  * on an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
  * as requested by a [Talker 😃 domain](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>).

<br/>

## Synchronous Call 🚀

```yaml
Header:
    From: any-talker.dom
    To: any-itemizer.dom
    Subject: Save@Itemizer

Body:
    Set: MySet
    Item: {...}
    Script: SaveToken
    Delete: 30 days         # Optional
```

|Object|Property|Type|Description
|-|-|-|-
| Header    |`From`|text| [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>) from [`Build@Itemizer`](<../Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           |`To`|text| [Itemizer 🛢](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>) from [`Build@Itemizer`](<../Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           | `Subject`     | string    | `Save@Itemizer`
| Body    | `Set`    | string  | `Set` from [`Build@Itemizer`](<../Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|         | `Item`    | object  | Object to save
|        | `Script` | string    | Optional [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) for traceability
|         | `Delete` | string  | Optional scheduled delete
|

## Synchronous Response

```yaml
Status: OK
Item: 
    :{Item properties}:
    .Table: MyTable
    .Version: <version-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Top| `Status`  | string    | `OK` `BLOCKED` `OUTDATED`
|Item| `Item`    | object    | Saved item with updated properties
|| `.Table`   |text| Table name for the [`SAVE` 📃 script](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE 📃 script.md>)
|| `.Version` | uuid   | Version for [`Save@Itemizer`](<🛢 Save 🚀 call.md>)
|


<br/>

## FAQ

1. **What's the format of `Delete`?**

    The `Delete` parameter 
    * follows the [`{.Add}`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ.md>) syntax
    * expecting `<number>` `<period>` 
    * where `<period>` is in `day(s)` `hour(s)` `minute(s)` `month(s)`
    * e.g, `30 days`.

    ---
    <br/>

1. **How to cancel a `Delete`?**

    To cancel a scheduled deletion, save the item again with an empty `Delete`.

    ---
    <br/>

1. **How to know if the item was deleted on timeout?**

    [Talker 😃 domains](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>) can register a `Hook` on the [`Build@Itemizer`](<../Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>) method to listen to delete events on the [Itemized 🪣 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).
    * Upon deletion, [Itemizer 🛢 helper domains](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>) invoke the [`Raised@Itemizer` 🔔 event](<../../🛢🔔 Itemizer events/🛢🔔 Raised.md>).

    ---
    <br/>

1. **What is the `Version` for?**

    The `Version` argument is used for optimistic concurrency.
    * When [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) call the [`Read@Itemizer`](<../Item Read 👥🚀🛢/🛢 Read 🚀 call.md>) method followed by changes to an [Item 🛢](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>), other [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) threads may be changing the same [Item 🛢](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) concurrently.
  
    * To avoid locking items with a standard ACID transaction, the [`Save@Itemizer`](<🛢 Save 🚀 call.md>) method checks the original version collected on the [`Read@Itemizer`](<../Item Read 👥🚀🛢/🛢 Read 🚀 call.md>) method.
  
    * If the version has changed due to a concurrent [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) in the [Talker 😃 domain](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>), then the [Itemizer 🛢 helper domain](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>) rejects the change, forcing the [Talker 😃 domain](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>) to re-run the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ---
    <br/>

1. **What are the possible statuses?**

    | Status | Details
    |-|-
    | `OK`        | The item was saved successfully.
    | `BLOCKED` | There is already an item with the same key and a different content, and the table schema was configured with `NoUpdates` to block any changes after the first [`Save@Itemizer` 🚀 call](<🛢 Save 🚀 call.md>).
    | `OUTDATED`  | The `.Version` of the item saved in the dataset (let's call it `A`) is different from the one given in `Item.Version` (let's call it B), meaning that item `A` has changed since item `B` was pulled with the [`Read@Itemizer` 🚀 call](<../Item Read 👥🚀🛢/🛢 Read 🚀 call.md>) call.
    
    ---
    <br/>