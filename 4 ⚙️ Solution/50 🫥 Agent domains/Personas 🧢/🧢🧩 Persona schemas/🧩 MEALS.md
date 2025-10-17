
# [🧩](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>): PersonaMeals

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PERSONA/MEALS
Name: Meal preferences
Description: >
  This is taken from the list of SSR (Special Service Requests)
  defined by Any IGO Airlines (International Air Transport Association).

Translations:
  pt-br: Preferências alimentares

Schema: 
  Format: 
    type: array
    items:
      $ref: Code@airlines.any-igo.dom/SSR/MEAL