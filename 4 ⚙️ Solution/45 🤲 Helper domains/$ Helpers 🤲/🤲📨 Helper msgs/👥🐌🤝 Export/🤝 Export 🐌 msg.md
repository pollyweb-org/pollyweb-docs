# 🤝 Export@Helper 🐌 call

> About
* Part of [Biller 🤝 domain](<../../../Billers 🤝/🤝 Biller/🤝 Biller 🤲 helper.md>)

<br/>

## Asynchronous Message 🐌

```yaml
Header:
    From: any-domain.dom
    To: any-biller.dom
    Subject: Export@Biller

Body:
    Export: <export-uuid>
    Read: {...}  # Inputs for Read@Helper
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|From|text| Client [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) |Standard|Routing|

