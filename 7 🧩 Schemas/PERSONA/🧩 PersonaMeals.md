
# 🧩 [Schema Code](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): PersonaMeals
```yaml
🤝: nlweb.org/MANIFEST/CODE

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