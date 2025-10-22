<!-- TODO: detail -->

# 👥🚀🛢 Get @ Itemizer

> Part of [Itemizer 🛢 helper](<../../🛢🤲 Itemizer helper.md>)

> Implements the [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) command

> Purpose:

* Retrieves an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
    * as requested by a [Talker 😃](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>)


## Synchronous Request 🚀

```yaml
Header:
    From: any-talker.dom
    To: any-itemizer.dom
    Subject: Get@Itemizer

Body:
    Table: MyPool
    Key: MyKey
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Talker 😃 domain](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) name
|           | `To`          | string    | [Itemizer 🛢 domain](<../../🛢🤲 Itemizer helper.md>) name
|           | `Subject`     | string    | `Get@Itemizer`
| Body      | `Table`     | string    | Name from [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>)
|           | `Key`        | string    | Key from [`Save@Itemizer`](<👥🚀🛢 Save.md>)
|


<br/>

## Synchronous Response

```yaml
.Table: MyTable
.Version: <version-uuid>
{Item object}
```

||Property|Type|Description
|-|-|-|-
|| `.Table`   | string | Table name for the [`.SAVE` 📃 script](<../../../../35 💬 Chats/😃 Talkers/😃📃 Talker scripts/😃📃 .SAVE script.md>)
|| `.Version` | uuid   | Version for [`Save@Itemizer`](<👥🚀🛢 Save.md>)
|| `{Item object}`        | object    | [Item 🛢](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) saved on [`Save@Itemizer`](<👥🚀🛢 Save.md>)
|