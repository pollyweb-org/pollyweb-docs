<!-- TODO: detail -->

# 👥🚀🛢 Save @ Itemizer

> Part of [Itemizer 🛢 helper](<../../🛢🤲 Itemizer helper.md>)

> Implements the [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/SAVE 💾 item.md>) commands from [Talker 😃 domains](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>).

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
    Key: my-item-key
    Item: {...}
    Script: SaveToken
    Timeout: 30 days
    Version: <version-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Talker 😃](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) from [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>)
|           | `To`          | string    | [Itemizer 🛢](<../../🛢🤲 Itemizer helper.md>) from [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>)
|           | `Subject`     | string    | `Save@Itemizer`
| Body    | `Set`    | string  | `Set` from [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>)
|         | `Key`     | string  | Case insensitive key
|         | `Item`    | object  | Object to save
|        | `Script` | string    | Optional [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) for traceability
|         | `Timeout` | string  | Optional scheduled delete
|         | `Version` | uuid    | Optional version from [`Get@Itemizer`](<👥🚀🛢 Get.md>)
|

<br/>

## FAQ

1. **What is the `Version` for?**

    The version argument is used for optimistic concurrency.
    * When a [Scripts 📃](<📃 Script.md>)

    ---
    <br/>