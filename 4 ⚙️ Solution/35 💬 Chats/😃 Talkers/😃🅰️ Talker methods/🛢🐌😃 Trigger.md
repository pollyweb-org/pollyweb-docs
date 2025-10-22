# 🛢🐌😃 Trigger @ Itemizer

> Used by 

* [`TokenTimeout` 📃 script](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📃 Broker scripts/...triggers/🤵📃 Token 🎫 Timeout.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-itemizer.dom
    To: any-talker.dom
    Subject: Trigger@Itemizer

Body:
    Hook: MyTrigger
    Item: {...}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Itemizer 🛢 domain](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🤲 Itemizer helper.md>) name
|           | `To`          | string    | [Talker 😃 domain](<../😃 Talker.md>) name
|           | `Subject`     | string    | `Trigger@Itemizer`
| Body      | `Hook`     | string    | `Hook` from [`Build@Itemizer`](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🅰️ Itemizer methods/...for Tables/👥🐌🛢 Build.md>)
|           | `Item`        | object    | [Item 🛢](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) from [`Transact@Itemizer`](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🅰️ Itemizer methods/...for Items/👥🚀🛢 Save.md>) 
|