# 🛢🐌😃 Raised @ Talker

> Implementation

* Implements [Item 🛢 Triggers](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Events.md>)

> Purpose

* An [Itemizer 🛢 helper](<../🛢🤲 Itemizer helper.md>) domain 
    * streams an event with its [Streamer 🌬️ domain role](<../../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) 
    * saying that an [Itemized 🛢 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) item has expired 
    * after being deleted with an [`UNDO`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/UNDO ↩️/↩️ UNDO ⌘ cmd.md>) possibility
    * via the [`Delete@Itemizer`](<../🛢🅰️ Itemizer methods/Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>) method.


> Used by 

* [`TokenTimeout` 📃 script](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Tokens 🎫 table/🪣🔔 OnTokenPurged/🤵 OnTokenPurged 📃 handler.md>)


## Async Message 🐌

```yaml
Header:
    From: any-itemizer.dom
    To: any-talker.dom
    Subject: Raised@Itemizer

Body:
    Trigger: EXPIRED
    Handler: MyHandler
    Item: {...}
    Changes: {...}
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header    |`From`|domain| [Itemizer 🛢](<../🛢🤲 Itemizer helper.md>) | [`Build@`](<../🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           |`To`|domain| [Talker 😃](<../🛢🅰️ Itemizer methods/Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>) | [`Build@`](<../🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           | `Subject`     | string    | `Raised@Itemizer`
| Body      | `Trigger`| enum | See [Item 🛢 Triggers](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Events.md>) | [`Build@`](<../🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|| `Handler`     | string    | Handler [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) name | [`Build@`](<../🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           | `Item`        | object    | Affected [Item 🛢](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) | -
|           | `Changes`     | object    | Original values changed | -
|

