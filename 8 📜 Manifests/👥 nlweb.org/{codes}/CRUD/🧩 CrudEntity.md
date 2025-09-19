
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): CrudEntity
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /CRUD/ENTITY
Name: CRUD Entity
Description: Configuration of a CRUD entity.

Schema:
  Properties:
    - About       # Singleton configuration of the entitity.
    - Properties  # List of properties in the entity.
    - Exports     # List of codes exported by the entity.

  Format: 
    type: object
    required: [About, Properties]
    properties:
      
      About:
        $ref: nlweb.org/CRUD/ENTITY/ABOUT

      Properties:
        type: object
        additionalProperties:
          $ref: nlweb.org/CRUD/ENTITY/PROPERTY
        description: List of properties in the entity.

      Exports:
        type: object
        additionalProperties:
          $ref: nlweb.org/CRUD/ENTITY/EXPORT
        description: List of codes exported by the entity.