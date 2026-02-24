

# [🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [`HOST`](<🧩 HOST.md>)/`ORDER`/`SELF`


> Inherits from [`pollyweb.org/TOKEN 🧩`](<../../../30 🧩 Data/Tokens 🎫/🧩 Token schemas/🧩 TOKEN.md>)

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /HOST/ORDER/SELF
Version: 1.0
Inherits: pollyweb.org/TOKEN:1.0

Title: Order
Description: Token for a self order

Translations:
    pt-br:
        Title: Encomenda

Fields: 
    Summary:

Asserts:
    Texts: Summary
```        