# 🧑‍💻🐌😃 Awake @ Talker

> Purpose

* Triggers a [`Wait` 🪣 item](<../../😃🪣 Talker tables/😃🪣 Waits ⏸️ table.md>)


<br/>

## Async Message 🐌

```yaml
Header:
    From: any-itemizer.dom
    To: any-talker.dom
    Subject: Awake@Itemizer

Body:
    Wait: <wait-uuid>
    Item: {...}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Itemizer 🛢](<../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🤲 Itemizer helper.md>) from [`Delete@Itemizer`](<../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/...for Items/Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>)
|           | `To`          | string    | [Talker 😃](<../../😃 Talker role.md>) from [`Delete@Itemizer`](<../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/...for Items/Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>)
|           | `Subject`     | string    | `Deleted@Itemizer`
| Body      | `Hook`     | string    | `Hook` from [`Build@Itemizer`](<../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/...for Tables/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|           | `Item`        | object    | [Item 🛢](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) from [`Delete@Itemizer`](<../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/...for Items/Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>)
|