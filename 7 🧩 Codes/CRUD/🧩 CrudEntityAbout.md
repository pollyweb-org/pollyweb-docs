
# [🧩](<../../4 ⚙️ Solution/30 Data/🧩 Schema Codes/🧩 Schema Code.md>) `.CRUD` `/ENTITY` `/ABOUT`

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /CRUD/ENTITY/ABOUT
Name: Entity About
Description: Singleton configuration of the entitity.

Schema:
  Properties:
    - Details  # Detailed information about the entity.
    - Format   # Indicates the multiplicity, ex. [ONE,MANY]
    - List     # Property to be presented in lists.
    - Many     # Name for multiple entities, ex. Feet.
    - One      # Name for one single entity, ex. Foot.
    - Rank     # Order of presenting for the list of items.

  Format: 
    type: object
    required: [Details, Format, One]
    properties:

      Details: 
        type: string
        description: > 
          Detailed information about the entity.

      Format: 
        enum: [ONE, MANY]
        description: >
          Indicates the multiplicity or items:
          - ONE: a single item is created automatically.
          - MANY: many items are allowed to be created.

      List: 
        type: string
        example: Title
        description: >
          Property to be presented in lists.
          * The property must exist in the list of properties.
          * The property must have unique index.

      Many: 
        type: string
        example: Feet
        description: Name for multiple entities.

      One:
        type: string
        example: Foot
        description: Name for one single entity.

      Rank:
        type: string
        example: Rank
        description: >
          Property to order the list of items.
          * must be an integer, from highest to lowest.
          * must exist in the list of properties.