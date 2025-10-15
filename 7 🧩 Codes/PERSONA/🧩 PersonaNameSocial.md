
# [🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): PersonaNameSocial

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<11 🧩 CODE code.md>)

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