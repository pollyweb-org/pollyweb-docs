
# [🧩](<../../4 ⚙️ Solution/25 Data/Schema Codes/02 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/25 Data/Schema Codes/02 🧩 Schema Code.md>): PersonaNameSocial

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/40 🧩 CODE code.md>)

```yaml
Path: /PERSONA/NAME/SOCIAL
Name: Social name

Description: >
  How a person wants to be refered to, socially.
  Tipically: first and last name, sometimes with a prefix/title.

References:
  GOV.UK Design System: https://design-system.service.gov.uk/patterns/names/

Translations:
  pt: Nome social

Schema:

  Properties:
    - Name      # Preferred social name
    - Pronouns  # //NAME/PRONOUNS
    
  Format: 
    type: object
    required: [Name]
    properties:
      Name:
        type: string
      Pronouns: 
        $ref: nlweb.org/PERSONA/NAME/PRONOUNS:1.0