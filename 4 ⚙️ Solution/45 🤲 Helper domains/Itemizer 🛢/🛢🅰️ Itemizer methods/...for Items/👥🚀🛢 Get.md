<!-- TODO: detail -->

# 👥🚀🛢 Get @ Itemizer

> Part of [Itemizer 🛢 helper](<../../🛢🤲 Itemizer helper.md>)

> Implements the [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET ⏬ item.md>) command

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
    Set: MySet
    Key: [ MyKey1, Key2 ]
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Talker 😃](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) from [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>)
|           | `To`          | string    | [Itemizer 🛢](<../../🛢🤲 Itemizer helper.md>) from [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>)
|           | `Subject`     | string    | `Get@Itemizer`
| Body      | `Set`     | string    | Set from [`Build@Itemizer`](<../...for Tables/👥🐌🛢 Build.md>)
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
|| `.Table`   | string | Table name for the [`.SAVE` 📃 script](<../../../../35 💬 Chats/😃 Talkers/😃📃 Talker scripts/...for datasets 🪣/😃📃 .SAVE script.md>)
|| `.Version` | uuid   | Version for [`Save@Itemizer`](<👥🚀🛢 Save.md>)
|| `{Item object}`        | object    | [Item 🛢](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) saved on [`Save@Itemizer`](<👥🚀🛢 Save.md>)
|