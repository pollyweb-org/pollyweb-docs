# 👥🚀🛢 Delete @ Itemizer

> Part of [Itemizer 🛢 helper](<../../🛢🤲 Itemizer helper.md>)

> Implements the  [`DELETE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) commands via the [`.DELETE` 📃 script](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE 📃 script.md>).

> Purpose

* Deletes items 
  * on an [Itemized 🛢 datasets](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
  * as requested by a [Talker 😃 domain](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)
  * via the [`.DELETE` 📃 script](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE 📃 script.md>).

<br/>

## Synchronous Call 🚀

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
| Header    |`From`|text| [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>) from [`Build@Itemizer`](<../Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           |`To`|text| [Itemizer 🛢](<../../🛢🤲 Itemizer helper.md>) from [`Build@Itemizer`](<../Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           | `Subject`     | string    | `Delete@Itemizer`
| Body    | `Script`     | string    | [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) for traceability
|         | `Set`    | string  | `Set` from [`Build@Itemizer`](<../Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|         | `Key`     | string[]  | Case insensitive keys
|         | `Undo` | string  | Optional [`UNDO`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/UNDO ↩️/↩️ UNDO ⌘ cmd.md>) time
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

    [Talker 😃 helper domains](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>) can register a hook on [`Build@Itemizer`](<../Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>) to listen to delete events on the [Itemized 🪣 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).
    * Upon deletion, [Itemizer 🛢 helper domains](<../../🛢🤲 Itemizer helper.md>) invoke the [`Raised@Itemizer` 🔔 event](<../../🛢🔔 Itemizer events/🛢🔔 Raised.md>).

    ---
    <br/>

1. **Why not an async message?**

    [Talker 😃 domains](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>) need to take immediate decisions upon failures when processing deletes, so they need to know immediately if the action was successful or not.

    ---
    <br/>


1. **What happens if an item is deleted twice?**

    Deletes don't raise errors of the key does not exist.
    * Thus, they silently survive retries by callers.
    
    On the the other hand, if the caller sends a key that never existed, that is ignored as well.
    * This allows for bugs to remain undetected on the caller;
    * but that's the caller's responsibility to remove their bugs.

    ---
    <br/>