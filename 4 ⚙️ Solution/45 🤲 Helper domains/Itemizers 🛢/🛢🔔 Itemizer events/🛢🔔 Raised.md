# 🛢🐌😃 Raised @ Talker

> Implementation

* Implements [Item 🛢 Handlers](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>)

> Purpose

* An [Itemizer 🛢 helper](<../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>) domain 
    * streams an event with its [Streamer 🌬️ domain role](<../../../41 🎭 Domain Roles/Streamers 🌬️/🌬️🎭 Streamer role.md>) 
    * saying that an [Itemized 🛢 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) item has expired 
    * after being deleted with an [`UNDO`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/UNDO ↩️/↩️ UNDO ⌘ cmd.md>) possibility
    * via the [`Delete@Itemizer`](<../🛢🅰️ Itemizer methods/Item Delete 👥🚀🛢/🛢 Delete 🚀 call.md>) method.



## Async Message 🐌

```yaml
Header:
    From: any-itemizer.dom
    To: any-talker.dom
    Subject: Raised@Itemizer

Body:
    Event: EXPIRED
    On: 2018-12-10T13:45:00.000Z
    Handler: MyHandler
    Item: 
        ID: <token-uuid>
        Wallet: <wallet-id>
        Status: ACTIVE
    New:
        Status: ACTIVE
    Old:
        Status: OFFERED
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header    |`From`|text| [Itemizer 🛢](<../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>) | [`Build@`](<../🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           |`To`|text| [Talker 😃](<../🛢🅰️ Itemizer methods/Item Delete 👥🚀🛢/🛢 Delete 🚀 call.md>) | [`Build@`](<../🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           | `Subject`     | string    | `Raised@Itemizer`
| Body      | `Event`| enum | See [Item 🛢 Handlers](<../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) | [`Build@`](<../🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
||`On`| time | When it happened | -
|| `Handler`     | string    | Handler [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) name | [`Build@`](<../🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           | `Item`        | map    | Current [Item 🛢](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) version | -
|           | `New`     | map    | New property versions | -
|           | `Old`     | map    | Old property versions | -
|

