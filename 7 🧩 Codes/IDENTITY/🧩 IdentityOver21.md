
# [🧩](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>): IdentityOver21

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /IDENTITY/OVER21
Title: Over 21 years old

Description: >
  Used by verify if the person is over 21 years old.
  This is drinking age in the United States.

Blueprint:
  Version: 1.0

  Properties:
    - Over21   
  
  Format:
    type: object
    require: [Over21]
    properties:

      Over21:
        type: boolean
  