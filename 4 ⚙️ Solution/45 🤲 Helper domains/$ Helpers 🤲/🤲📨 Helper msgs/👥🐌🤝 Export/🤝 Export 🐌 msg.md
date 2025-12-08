# 🤝 Export@Helper 🐌 call

> About
* Part of the [Helper 🤲 domain](<../../🤲 Helper/🤲👥 Helper domain.md>)
* Slowly sends a large number of items into the client domain's {{Buffer}} 
* Applies the same filtering as [`Read@Helper` 🚀 call](<../👥🚀🤝 Read/🤝 Read 🚀 call.md>)


<br/>

## Asynchronous Message 🐌

```yaml
Header:
    From: any-domain.dom
    To: any-biller.dom
    Subject: Export@Helper

Body:
    Export: <export-uuid>
    Read: {...}  # Inputs for Read@Helper
```

<br/>


|Object|Property|Type|Purpose
|-|-|-|-
|Header|`From`|text| Client [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name|
||`To`|text| [Helper 🤲 domain](<../../🤲 Helper/🤲👥 Helper domain.md>) name |   
||`Subject`|text| `Export@Helper` |
|Body|`Export`|uuid| Client identifier for this export |
||`Read`|map| Inputs for [`Read@Helper`](<../👥🚀🤝 Read/🤝 Read 🚀 call.md>) 

