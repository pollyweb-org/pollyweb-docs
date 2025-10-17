
# [🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>): HostOrderSelf

> Inherits from [`nlweb.dom/TOKEN 🧩`](<../../../30 🧩 Data/Tokens 🎫/🧩 Token schemas/🧩 TOKEN.md>)

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /HOST/ORDER/SELF
Name: Order
Description: Token for a self order

Translations:
  - Language: pt-br
    Translation: Encomenda

Schema:  
  Version: 1.0
  Inherits: nlweb.dom/TOKEN:1.0
  
  Properties: 
    - Summary

  Format:
    type: object
    properties:
      Summary:
        type: string   