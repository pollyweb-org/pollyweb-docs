<!-- TODO: detail -->

# 👥🚀🛢 Transact @ Itemizer

> Part of [Itemizer 🛢 helper](<../../🛢🤲 Itemizer helper.md>)

> Implements the [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/SAVE 💾 item.md>) and [`DELETE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/DELETE 🗑️ item.md>) commands.

> Purpose:

* Saves and deletes items 
  * on an [Itemized 🛢 datasets](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
  * as a single transaction
  * as requested by a [Talker 😃 domain](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>).

<br/>

## Synchronous Request

```yaml
Header:
    From: any-talker.dom
    To: any-itemizer.dom
    Subject: Transact@Itemizer

Body:
    Blame: SaveToken

    Saves:
      - Table: MyPool
        Key: my-item-key
        Timeout: 30 days
        Data: {...}

    Deletes:
      - Table: Pool2
        Key: another-item-key
        Timeout: 30 days
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Talker 😃 domain](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) name
|           | `To`          | string    | [Itemizer 🛢 domain](<../../🛢🤲 Itemizer helper.md>) name
|           | `Subject`     | string    | `Transact@Itemizer`
| Body      | `Blame`     | string    | Reference for traceability
|           | `Saves`       | array     | List of items to save
|           | `Deletes`     | array     | List of items to delete
| Saves   | `Table`    | string  | Case insensitive name
|         | `Key`     | string  | Case insensitive key
|         | `Timeout` | string  | Optional scheduled delete
|         | `Data`    | object  | Object to save
| Deletes | `Table`    | string  | Case insensitive name
|         | `Key`     | string  | Case insensitive key
|         | `Timeout` | string  | Optional [`UNDO`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/UNDO ↩️.md>) time
|