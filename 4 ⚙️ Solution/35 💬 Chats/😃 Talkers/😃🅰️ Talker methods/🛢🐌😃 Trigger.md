# 🛢🐌😃 Trigger @ Itemizer

```yaml
Header:
    From: any-itemizer.dom
    To: any-talker.dom
    Subject: Trigger@Itemizer

Body:
    Trigger: MyTrigger
    Item: {...}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Itemizer 🛢 domain](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🤲 Itemizer helper.md>) name
|           | `To`          | string    | [Talker 😃 domain](<../😃 Talker.md>) name
|           | `Subject`     | string    | `Trigger@Itemizer`
| Body      | `Trigger`     | string    | `Trigger` from {{Transact@Itemizer}} 
|           | `Item`        | object    | [Itemized 🛢 item](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>) triggered
|