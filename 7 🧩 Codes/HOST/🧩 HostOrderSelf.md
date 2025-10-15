
# [🧩](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>): HostOrderSelf

> Inherits from [`nlweb.org/TOKEN 🧩`](<../../4 ⚙️ Solution/30 🧩 Data/30 🎫 Tokens/🧩 Token schemas/🧩 TOKEN.md>)

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /HOST/ORDER/SELF
Name: Order
Description: Token for a self order

Translations:
  - Language: pt-br
    Translation: Encomenda

Schema:  
  Version: 1.0
  Inherits: nlweb.org/TOKEN:1.0
  
  Properties: 
    - Summary

  Format:
    type: object
    properties:
      Summary:
        type: string   