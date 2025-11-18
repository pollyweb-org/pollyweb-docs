# 👥🐌🛢 Build

> Part of [Itemizer 🛢 helper](<../../🛢🤲 Itemizer helper.md>)


> Purpose

* Builds an [Itemized 🪣 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
    * as requested by a [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)

> Examples

* [`Wallets` 🪣 table](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
* [`Notifiers` 🪣 table](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Notifiers 📣 table/🪣 Notifiers/🤵 Broker.Notifiers 🪣 table.md>)
* [`Binds` 🪣 table](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>)

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
    Propagate: [...]
    Children: {...}
    Distincts: {...}
    Handlers: {...}
    NoUpdates: True  # it's False by default
```
|Object|Property|Type|Description
|-|-|-|-
| Header    |`From`|text| [Talker 😃 domain](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)  name
| |         `To` |text| [Itemizer 🛢 domain](<../../🛢🤲 Itemizer helper.md>) name
| |         `Subject` |text| `Build@Itemizer`
| Body      | `Name`     | string    |  [Itemized 🪣 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) name
|           | `Key`        | string[]  | Index for [`Save@`](<../Item Save 👥🚀🛢/🛢 Save 🚀 call.md>) and [`Read@`](<../Item Read 👥🚀🛢/🛢 Read 🚀 call.md>)
|           | [`Parents`](<../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) | map |		List of parent items
|           | [`Propagate`](<../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Propagate.md>) | string[] | List of parents to propagate
|           | [`Children`](<../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Children.md>) |map	| List of children items
|           | [`Distincts`](<../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Distincts.md>) |	map |	List of grouped fields
|           | [`NoUpdates`](<../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 NoUpdates.md>) | bool | Blocks item updates
|           | [`Handlers`](<../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) | map | [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) for [`Raised@Itemizer` 🔔](<../../🛢🔔 Itemizer events/🛢🔔 Raised.md>)
|

<br/>

## FAQ

1. **Are names of Sets case insensitive?**

    Yes. 
    
    * Names of [Itemized 🪣 datasets](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) and their internal properties are case insensitive.

    ---
    <br/>
