# 🛢🐌😃 Triggered @ Talker

> Purpose

* An [Itemizer 🛢 helper](<../🛢🤲 Itemizer helper.md>) domain 
    * notifies a [Talker 😃 domain](<../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) 
    * that an [Itemized 🛢 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) item has expired 
    * after being deleted with an [`UNDO`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/UNDO/UNDO ↩️.md>) possibility
    * via the [`Delete@Itemizer`](<../🛢🅰️ Itemizer methods/Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>) method.

<br/>

> Used by 

* [`TokenTimeout` 📃 script](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Tokens 🎫 table/🤵 Tokens Timeout 📃 trigger.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-itemizer.dom
    To: any-talker.dom
    Subject: Triggered@Itemizer

Body:
    Trigger: EXPIRED
    Handler: MyHandler
    Item: {...}
    Changes: {...}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Itemizer 🛢](<../🛢🤲 Itemizer helper.md>) from [`Delete@Itemizer`](<../🛢🅰️ Itemizer methods/Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>)
|           | `To`          | string    | [Talker 😃](<../🛢🅰️ Itemizer methods/Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>)
|           | `Subject`     | string    | `Triggered@Talker`
| Body      | `Trigger`| enum | See [Itemized 🪣 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) triggers
|| `Handler`     | string    | Handler from [`Build@Itemizer`](<../🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           | `Item`        | object    | [Item 🛢](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) from [`Delete@Itemizer`](<../🛢🅰️ Itemizer methods/Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>)
|           | `Changes`     | object    | Old values of changed properties
|

