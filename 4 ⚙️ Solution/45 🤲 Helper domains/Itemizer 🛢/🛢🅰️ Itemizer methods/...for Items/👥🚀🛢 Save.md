<!-- TODO: detail -->


# 👥🚀🛢 Save @ Itemizer

> Part of [Itemizer 🛢 helper](<../../🛢🤲 Itemizer helper.md>)

> Implements the [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/SAVE 💾 item.md>) commands from [Talker 😃 domains](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>).

> Purpose

* Saves an item
  * on an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
  * as requested by a [Talker 😃 domain](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>).

<br/>

## Synchronous Request

```yaml
Header:
    From: any-talker.dom
    To: any-itemizer.dom
    Subject: Save@Itemizer

Body:
    Set: MySet
    Item: {...}
    Script: SaveToken
    Version: <version-uuid> # Optional
    Delete: 30 days         # Optional
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Talker 😃](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) from [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>)
|           | `To`          | string    | [Itemizer 🛢](<../../🛢🤲 Itemizer helper.md>) from [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>)
|           | `Subject`     | string    | `Save@Itemizer`
| Body    | `Set`    | string  | `Set` from [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>)
|         | `Item`    | object  | Object to save
|         | `Version` | uuid    | Optional version from [`Get@Itemizer`](<👥🚀🛢 Get.md>)
|        | `Script` | string    | Optional [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... ⌘ commands/📃 Script.md>) for traceability
|         | `Delete` | string  | Optional scheduled delete
|

<br/>

## FAQ

1. **What's the format of `Delete`?**

    The `Delete` parameter 
    * expects `<number>` `<period>` 
    * where `<period>` is in `days` `hours` `minutes` `months`
    * e.g, `30 days`.

    ---
    <br/>


1. **How to know if the item was deleted on timeout?**

    [Talker 😃 domains](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) can register a `Hook` on the [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>) method to listen to delete events on the [Itemized 🪣 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).
    * Upon deletion, [Itemizer 🛢 helper domains](<../../🛢🤲 Itemizer helper.md>) invoke the [`Trigger@Talker`](<../../../../35 💬 Chats/😃 Talkers/😃🅰️ Talker methods/🛢🐌😃 Deleted.md>) method.

    ---
    <br/>

1. **What is the `Version` for?**

    The `Version` argument is used for optimistic concurrency.
    * When [Scripts 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... ⌘ commands/📃 Script.md>) call the [`Get@Itemizer`](<👥🚀🛢 Get.md>) method followed by changes to an [Item 🛢](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>), other [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... ⌘ commands/📃 Script.md>) threads may be changing the same [Item 🛢](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) concurrently.
  
    * To avoid locking items with a standard ACID transaction, the [`Save@Itemizer`](<👥🚀🛢 Save.md>) method checks the original version collected on the [`Get@Itemizer`](<👥🚀🛢 Get.md>) method.
  
    * If the version has changed due to a concurrent [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/SAVE 💾 item.md>) in the [Talker 😃 domain](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>), then the [Itemizer 🛢 helper domain](<../../🛢🤲 Itemizer helper.md>) rejects the change, forcing the [Talker 😃 domain](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) to re-run the [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... ⌘ commands/📃 Script.md>).

    ---
    <br/>