
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): IdentityOver21

```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /IDENTITY/OVER21
Name: Over 21 years old

Description: >
  Used by verify if the person is over 21 years old.
  This is drinking age in the United States.

Schema:
  Version: 1.0
  Output: SHARE

  Properties:
    - Over21   
  
  Format:
    type: object
    require: [Over21]
    properties:

      Over21:
        type: boolean
  