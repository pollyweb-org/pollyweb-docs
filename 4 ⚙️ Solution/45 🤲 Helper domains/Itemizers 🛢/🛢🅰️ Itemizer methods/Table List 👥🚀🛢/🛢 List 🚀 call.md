<!-- TODO: detail -->

# 👥🚀🛢 List

> Part of [Itemizer 🛢 helper](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>)

> Purpose: 

* Lists the registered tables from [`Build@Itemizer`](<../Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>).

<br/>

## Synchronous Call 🚀

```yaml
Header:
    From: any-domain.dom
    To: any-itemizer.dom
    Subject: List@Itemizer
```

|Object|Property|Type|Description
|-|-|-|-
|Header |`From`|text| Caller [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name
|       |`To`|text| [Itemizer 🛢 domain](<../../🛢 Itemizer helper/🛢🤲 Itemizer helper.md>)
|       |`Subject`  |text| `List@Itemizer`
|

<br/>

## Synchronous Response

```yaml
Tables:
  - Name: MyTable
    Created: 2024-01-01T12:00:00Z
    ItemCount: 100
```

|Object|Property|Type|Description
|-|-|-|-
|Top     |`Tables`    | array   | List of registered tables
|Tables  |`Name`      | string  | Name from [`Build@Itemizer`](<../Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
|        |`Created`   | string  | ISO8601 date of creation
|        |`ItemCount` | integer | Number of items in the table
|