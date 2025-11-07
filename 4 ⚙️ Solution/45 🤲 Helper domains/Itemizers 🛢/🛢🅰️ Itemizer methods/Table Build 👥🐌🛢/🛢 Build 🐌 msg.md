# 👥🐌🛢 Build

> Part of [Itemizer 🛢 helper](<../../🛢🤲 Itemizer helper.md>)


> Purpose

* Builds an [Itemized 🪣 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
    * as requested by a [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)

> Examples

* [`Wallets` 🪣 table](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 BrokerWallets 🪣 table.md>)
* [`Notifiers` 🪣 table](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Notifiers 📣 table/🤵 BrokerNotifiers 🪣 table.md>)
* [`Binds` 🪣 table](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Binds 🔗 table/🤵 BrokerBinds 🪣 table.md>)

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
    Triggers: {...}
    NoUpdates: True  # it's False by default
```
|Object|Property|Type|Description
|-|-|-|-
| Header    |`From`|domain| [Talker 😃 domain](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)  name
| |         `To` | string | [Itemizer 🛢 domain](<../../🛢🤲 Itemizer helper.md>) name
| |         `Subject` | string | `Build@Itemizer`
| Body      | `Name`     | string    |  [Itemized 🪣 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) name
|           | `Key`        | string[]  | Index for [`Save@`](<../Item Save 👥🚀🛢/🛢 Save 🚀 request.md>) and [`Get@`](<../Item Get 👥🚀🛢/🛢 Get 🚀 request.md>)
|           | `Parents` | dict |		List of parent items
|           | `Propagate`| string[] | List of parents to propagate
|           | `Children` |dict	| List of children items
|           | `Distincts`|	map |	List of grouped fields
|           | `NoUpdates` | bool | Blocks item updates
|           | `Triggers`| dict | Hooks for [`Triggered@Talker`](<../../🛢🔔 Itemizer events/🛢🔔 Triggered.md>)
|

<br/>

## FAQ

1. **Are names of Sets case insensitive?**

    Yes. 
    
    * Names of [Itemized 🪣 datasets](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) and their internal properties are case insensitive.

    ---
    <br/>
