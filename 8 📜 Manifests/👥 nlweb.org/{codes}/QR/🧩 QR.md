
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): QR

```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /QR

Schema:
  Output: QR
  Version: 1.0
  
  Properties:
    - Code     # e.g., airlines.any-igo.org/SSR/WCHR/CRED:1.0
    - Issuer   # ex. health.any-nation.org
    - Resource  # ex. ANY-RESOURCE-KEY
    - '*'

  Format:
    type: object
    properties:

      Code:
        type: string
        title: A Schema Code.

      Issuer:
        type: string
        title: Domain that issued the QR.

      Resource:
        type: string
        title: Unique index of a resource in the context of the issuer.
