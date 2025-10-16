
# [🧩](<../../4 ⚙️ Solution/30 Data/🧩 Schema Codes/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 Data/🧩 Schema Codes/🧩 Schema Code.md>): PalmPassport

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PALM/PASSPORT
Name: Passport
Description: Share bind of Passport with Palm.

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
          