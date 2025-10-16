
# [🧩](<../../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) [Schema Code](<../../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>): PersonaNameLegal

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

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