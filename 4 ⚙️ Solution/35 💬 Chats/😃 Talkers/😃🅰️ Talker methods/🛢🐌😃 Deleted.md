# 🛢🐌😃 Deleted @ Talker

> Purpose

* An [Itemizer 🛢 helper](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🤲 Itemizer helper.md>) domain 
    * notifies a [Talker 😃 domain](<../😃 Talker role.md>) 
    * that an [Itemized 🛢 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) item has expired 
    * after being deleted with an [`UNDO`](<../😃⚙️ Talker cmds/for data/UNDO ↩️.md>) possibility
    * via the [`Delete@Itemizer`](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🅰️ Itemizer methods/...for Items/👥🚀🛢 Delete.md>) method.

<br/>

> Used by 

* [`TokenTimeout` 📃 script](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📃 Broker scripts/...triggers/🤵📃 Token 🎫 Timeout.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-itemizer.dom
    To: any-talker.dom
    Subject: Deleted@Itemizer

Body:
    Hook: MyTrigger
    Item: {...}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Itemizer 🛢](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🤲 Itemizer helper.md>) from [`Delete@Itemizer`](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🅰️ Itemizer methods/...for Items/👥🚀🛢 Delete.md>)
|           | `To`          | string    | [Talker 😃](<../😃 Talker role.md>) from [`Delete@Itemizer`](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🅰️ Itemizer methods/...for Items/👥🚀🛢 Delete.md>)
|           | `Subject`     | string    | `Deleted@Itemizer`
| Body      | `Hook`     | string    | `Hook` from [`Build@Itemizer`](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🅰️ Itemizer methods/...for Tables/👥🐌🛢 Build.md>)
|           | `Item`        | object    | [Item 🛢](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) from [`Delete@Itemizer`](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🅰️ Itemizer methods/...for Items/👥🚀🛢 Delete.md>)
|