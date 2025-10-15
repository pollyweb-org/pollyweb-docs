
# [🧩](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>): PersonaMeals

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/40 🧩 CODE code.md>)

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
      $ref: Code@airlines.any-igo.org/SSR/MEAL