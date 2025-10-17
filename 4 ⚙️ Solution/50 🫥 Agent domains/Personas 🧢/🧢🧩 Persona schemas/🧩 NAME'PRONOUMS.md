
# [🧩](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>): PersonaNamePronouns

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PERSONA/NAME/PRONOUNS
Name: Personal gender pronouns

Description: >
    "Personal gender pronouns" (or PGPs) are pronouns 
    that people ask others to use in reference to themselves. 
    They may be plural gender-neutral pronouns such as they, them, their(s)

References:
  GOV.UK Design System: https://design-system.service.gov.uk/patterns/gender-or-sex/
  Mermaids: https://mermaidsuk.org.uk/news/tag/pronouns/

Translations:
  pt: Pronomes pessoais de gênero

Schema:

  Format: 
    type: string
    enum: [he/him, she/her, they/them]