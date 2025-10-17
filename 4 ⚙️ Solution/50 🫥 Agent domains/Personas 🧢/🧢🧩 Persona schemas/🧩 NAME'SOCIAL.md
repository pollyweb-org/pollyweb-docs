
# [🧩](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>): PersonaNameSocial

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/🧩 Manifest schemas/🧩 CODE.md>)

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
        $ref: nlweb.dom/PERSONA/NAME/PRONOUNS:1.0