# 🤝 Delete@Helper 🐌 call

> About
* Part of the [Helper 🤲 domain](<../../🤲 Helper/🤲👥 Helper domain.md>)
 
<br/>

## Asynchronous Message 🐌

```yaml
Header:
    From: any-domain.dom
    To: any-helper.dom
    Subject: Delete@Helper

Body:
    Set: AnySet
    Key: 123
```


<br/>

|Object|Property|Type|Purpose|Default
|-|-|-|-|-
|Header|`From`|text| Client [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name|
||`To`|text| [Helper 🤲 domain](<../../🤲 Helper/🤲👥 Helper domain.md>) name |   
||`Subject`|text| `Delete@Helper` |
|Body|`Set`|text| [Set](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>) name to delete |
||`Key`|any| Key of the item to delete |

