
# [🧩](<../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) `DOMAIN`



## Definition

> 🤝: [`.MANIFEST/CODE`](<../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /DOMAIN

Title: Domain admin
Translations:
    pt-br: Admin de domínio

Fields: 
    Domain: Domain to administer

Example:
    Domain: mydomain.dom

Asserts:
    AllOf: Domain
    Domain.IsDomain: 
```    
Use: [`.IsDomain`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>)