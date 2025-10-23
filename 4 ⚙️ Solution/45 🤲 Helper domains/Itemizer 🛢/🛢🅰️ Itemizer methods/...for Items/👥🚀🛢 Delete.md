<!-- TODO: detail -->

# 👥🚀🛢 Delete @ Itemizer

> Part of [Itemizer 🛢 helper](<../../🛢🤲 Itemizer helper.md>)

> Implements the  [`DELETE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/DELETE 🗑️ item.md>) commands via the [`.DELETE` 📃 script](<../../../../35 💬 Chats/😃 Talkers/😃📃 Talker scripts/😃📃 .DELETE 🗑️ script.md>).

> Purpose

* Deletes items 
  * on an [Itemized 🛢 datasets](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
  * as requested by a [Talker 😃 domain](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>)
  * via the [`.DELETE` 📃 script](<../../../../35 💬 Chats/😃 Talkers/😃📃 Talker scripts/😃📃 .DELETE 🗑️ script.md>).

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-talker.dom
    To: any-itemizer.dom
    Subject: Delete@Itemizer

Body:
    Script: MyScript
    Set: MySet
    Key: [ MyKey1, MyKey2 ]
    Undo: 30 days # Optional
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Talker 😃](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) from [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>)
|           | `To`          | string    | [Itemizer 🛢](<../../🛢🤲 Itemizer helper.md>) from [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>)
|           | `Subject`     | string    | `Delete@Itemizer`
| Body    | `Script`     | string    | [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands/📃 Script.md>) for traceability
|         | `Set`    | string  | `Set` from [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>)
|         | `Key`     | string[]  | Case insensitive keys
|         | `Undo` | string  | Optional [`UNDO`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/UNDO ↩️.md>) time
|

<br/>

## Synchronous

```yaml
# HTTP 200, OK
```

<br/>

## FAQ


1. **What's the format of `Undo`?**

    The `Undo` parameter 
    * expects `<number>` `<period>` 
    * where `<period>` is in `days` `hours` `minutes` `months`
    * e.g, `30 days`.

    ---
    <br/>

1. **How to know if the item was deleted on timeout?**

    [`Talker`](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) domains can register a hook on [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>) to listen to delete events on the [`Itemized dataset`](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).
    * Upon deletion, [`Itemizer helper`](<../../🛢🤲 Itemizer helper.md>) invoke the [`Trigger@Talker`](<../../../../35 💬 Chats/😃 Talkers/😃🅰️ Talker methods/🛢🐌😃 Deleted.md>) method.

    ---
    <br/>

1. **Why not an async message?**

    [Talker 😃 domains](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) need to take immediate decisions upon failures when processing deletes, so they need to know immediately if the action was successful or not.

    ---
    <br/>
