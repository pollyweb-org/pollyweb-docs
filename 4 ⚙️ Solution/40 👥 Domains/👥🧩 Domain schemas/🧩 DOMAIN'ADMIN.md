
# [🧩](<../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [`HOST`](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>)/`ADMIN`


## Definition

> 🤝: [`.MANIFEST/CODE`](<../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /HOST/ADMIN

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