<!-- TODO: detail -->

# 👥🚀🛢 List

> Part of [Itemizer 🛢 helper](<../../../🛢🤲 Itemizer helper.md>)

> Purpose: 

* Lists the registered tables from [`Build@Itemizer`](<../👥🐌🛢 Build/👥🐌🛢 Build.md>).

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-domain.dom
    To: any-itemizer.dom
    Subject: List@Itemizer
```

|Object|Property|Type|Description
|-|-|-|-
|Header |`From`     | string | Caller [domain 👥](<../../../../../40 👥 Domains/👥 Domain.md>) name
|       |`To`       | string | [Itemizer 🛢 domain](<../../../🛢🤲 Itemizer helper.md>)
|       |`Subject`  | string | `List@Itemizer`
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
|Tables  |`Name`      | string  | Name from [`Build@Itemizer`](<../👥🐌🛢 Build/👥🐌🛢 Build.md>)
|        |`Created`   | string  | ISO8601 date of creation
|        |`ItemCount` | integer | Number of items in the table
|