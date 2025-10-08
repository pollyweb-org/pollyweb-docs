
# 🧩 [Schema Code](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): HostOrderSelf

> Inherits from [`nlweb.org/TOKEN 🧩`](<../TOKEN/🧩 Token.md>)

```yaml
🤝: nlweb.org/MANIFEST/CODE

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