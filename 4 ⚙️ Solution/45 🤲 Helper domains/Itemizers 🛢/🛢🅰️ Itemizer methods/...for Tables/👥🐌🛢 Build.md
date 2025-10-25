<!-- TODO: detail -->

# 👥🐌🛢 Build

> Part of [Itemizer 🛢 helper](<../../🛢🤲 Itemizer helper.md>)


> Purpose:

* Builds an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
    * as requested by a [Talker 😃](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>)

> Examples:

* [`Wallets` 🪣 table](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Wallets/🤵🪣 Wallets table.md>)
* [`Notifiers` 🪣 table](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Notifiers/🤵🪣 Notifiers table.md>)
* [`Binds` 🪣 table](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Binds 🔗/🤵🪣 Binds table.md>)

## Async Message

```yaml
Header:
    From: any-talker.dom
    To: any-itemizer.dom
    Subject: Build@Itemizer

Body:
    Set: MySet
    Key: MyKey
    Parents: {...}
    Children: {...}
    Distincts: {...}
    Triggers: {...}
    NoUpdates: True  # it's False by default
```
|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Talker 😃 domain](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>)  name
| |         `To` | string | [Itemizer 🛢 domain](<../../🛢🤲 Itemizer helper.md>) name
| |         `Subject` | string | `Build@Itemizer`
| Body      | `Name`     | string    |  [Itemized 🪣 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) name
|           | `Key`        | string[]  | Index for [`Save@`](<../...for Items/👥🚀🛢 Save.md>) and [`Get@`](<../...for Items/👥🚀🛢 Get.md>)
|           | `Parents` | map |		List of parent items
|           | `Children` |map	| List of children items
|           | `Distincts`|	map |	List of grouped fields
|           | `NoUpdates` | bool | Blocks item updates
|           | `Triggers`| map | Hooks for [`Triggered@Talker`](<../../🛢🔔 Itemizer events/🛢🔔 Triggered.md>)
|

<br/>

## FAQ

1. **Are names of Sets case insensitive?**

    Yes. 
    
    * Names of [Itemized 🪣 datasets](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) and their internal properties are case insensitive.

    ---
    <br/>
