
# [🧩](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>): PayPayer

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PAY/PAYER
Name: Payer
Description: Share code for payers.

References:
  NLWEB: 💳 https://quip.com/HyzNATeThi0Q/-PayNLWEBorg

Translations:
  - Language: pt-br
    Translation: Pagador
    
Schema:
  Version: 1.0
  Location: https://en.wikipedia.org/wiki/Domain_name
  Format: 
    type: string
    