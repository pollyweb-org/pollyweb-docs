
# [🧩](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>): HostOrderSelf

> Inherits from [`nlweb.org/TOKEN 🧩`](<../$/🧩 TOKEN code.md>)

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/40 🧩 CODE code.md>)

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