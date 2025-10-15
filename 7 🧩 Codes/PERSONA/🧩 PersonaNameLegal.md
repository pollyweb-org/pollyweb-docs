
# [🧩](<../../4 ⚙️ Solution/25 Data/Schema Codes/02 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/25 Data/Schema Codes/02 🧩 Schema Code.md>): PersonaNameLegal

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/40 🧩 CODE code.md>)

```yaml
Path: /PERSONA/NAME/LEGAL
Name: Full legal name

Description: > 
  A person's full name, tipically for legal purposes.

Translations:
  pt: Nome legal completo

References:
  GOV.UK Design System: https://design-system.service.gov.uk/patterns/names/

Schema:

  Properties:
    - Name      # Legal name

  Format:
    type: object
    required: [Name]
    properties:
      Name:
        type: string