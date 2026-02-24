
# [🧩](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) `.CRUD` `/ENTITY`

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /CRUD/ENTITY
Title: CRUD Entity
Description: Configuration of a CRUD entity.

Blueprint:
  Properties:
    - About       # Singleton configuration of the entitity.
    - Properties  # List of properties in the entity.
    - Exports     # List of codes exported by the entity.

  Format: 
    type: object
    required: [About, Properties]
    properties:
      
      About:
        $ref: pollyweb.org/CRUD/ENTITY/ABOUT

      Properties:
        type: object
        additionalProperties:
          $ref: pollyweb.org/CRUD/ENTITY/PROPERTY
        description: List of properties in the entity.

      Exports:
        type: object
        additionalProperties:
          $ref: pollyweb.org/CRUD/ENTITY/EXPORT
        description: List of codes exported by the entity.

```