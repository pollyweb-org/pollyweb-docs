
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): QR

```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /QR

Schema:
  Output: QR
  Version: 1.0
  
  Properties:
    - Code     # ex. airlines.any-igo.org/SSR/WCHR/CRED
    - Version  # ex. 1
    - Issuer   # ex. health.any-nation.org
    - Locator  # ex. ace79fcb-fa93-4544-bbe3-644b31df03db
    - '*'

  Format:
    type: object
    properties:

      Code:
        type: string
        description: https://quip.com/3mKNASbBpnng#temp:C:eVd92c29500621a4395928f6d216
        title: Global unique identifier of a code.

      Version:
        type: string
        description: https://quip.com/3mKNASbBpnng#temp:C:eVde82fdd62ed194493afa0b9134
        title: Version of the data matching a schema

      Issuer:
        type: string
        description: https://quip.com/k0piAXze1T81#temp:C:KdIa893b7f9c8e34c4f98ec29fe6
        title: Domain that issued the QR

      Locator:
        type: string
        description: https://quip.com/k0piAXze1T81#temp:C:KdIb122e50709a341e48c11af73a
        title: Unique index of the code in the context of the issuer
