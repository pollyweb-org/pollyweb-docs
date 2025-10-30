

# [🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [`HOST`](<🧩 HOST.md>)/`ORDER`/`SELF`


> Inherits from [`nlweb.dom/TOKEN 🧩`](<../../../30 🧩 Data/Tokens 🎫/🧩 Token schemas/🧩 TOKEN.md>)

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /HOST/ORDER/SELF
Name: Order
Description: Token for a self order

Translations:
  - Language: pt-br
    Translation: Encomenda

Blueprint:  
  Version: 1.0
  Inherits: nlweb.dom/TOKEN:1.0
  
  Properties: 
    - Summary

  Format:
    type: object
    properties:
      Summary:
        type: string   