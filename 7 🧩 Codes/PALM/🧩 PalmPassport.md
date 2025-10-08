
# 🧩 [Schema Code](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): PalmPassport
```yaml
🤝: nlweb.org/MANIFEST/CODE


Path: /PALM/PASSPORT
Name: Passport
Description: Share bind of Passport with Palm.

Resources:
  NLWEB: 🤝🖐️ https://quip.com/2VbFAchUGm3k

Translations:
  - Language: pt-br
    Translation: Passaporte

Schema:  
  Version: 1.0

  Properties:
    - Palm:
        - PalmID
        - Palmist
    - Passports:
        - Type
        - Number
        - Issuer 

  Format:
    type: object
    properties:

      Palm:
        type: object
        properties:
          PalmID:
            type: string
          Palmist:
            type: string

      Passports:
        type: array
        items:
          type: object
          properties:
            Type:
              type: string
            Number:
              type: string
            Issuer:
              type: string
          