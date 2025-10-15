
# [🧩](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>): CrudEntityPropertyInternal

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/40 🧩 CODE code.md>)

```yaml
Path: /CRUD/ENTITY/PROPERTY/INTERNAL
Name: Internal list property

Description: >
  Loads ONE|MANY options from an internal entity.
  - The entity should remain unavailable until there is at least one
    item in the table of the dependent entities.

Schema:
  Properties:
    - From  # Entity providing the information.
    - Show  # Returned property to show to the user.
    - Save  # Returned property to be saved.

  Format:
    type: object
    required: [From, Show, Save]
    properties:

      From:
        format: string
        example: Phone
        description: Internal entity to get the options from.

      Show: 
        format: string
        example: Title
        description: Returned property to show to the user.

      Save: 
        format: array
        items: 
          type: string
        example: [Country, Number]
        description: Returned properties to be saved.
      