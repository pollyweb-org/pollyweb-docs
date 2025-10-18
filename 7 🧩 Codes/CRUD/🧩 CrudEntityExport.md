
# [🧩](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>): CrudEntityExport

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /CRUD/ENTITY/EXPORT
Name: Entity Export
Description: >
  Definition of an exportable code supported by the entity.

Blueprint:
  Properties:
    - Format  # Export only one item, or all items: ONE|MANY
    - If      # Export only if the given property is True.
    - Map     # Dictionary of properties to export in <name>:<value>.
    - Rank    # Name of rank property to sort the items.

  Format:
    type: object
    required: [Format, Map]
    properties:

      Format:
        enum: [ONE, MANY]
        description: >
          Export only one item, or all items.
            - If format is ONE and more that 1 item exists, then the user 
              will be asked to select the item on every share.

      If:
        type: string
        description: >
          Export only if the given property is True.

      Map:
        description: >
          Value or dictionary of properties to export in <name>:<value>.
          - The value can be a string or another dictionary.
          - Use '.' to reference sub properties, ex. 'Country.ISD'.
          - Use '@' to reference external entites, ex. 'Property@AnotherEntity'.
          - Properties of format MANY will are rendered as arrays.
        oneOf: 
          - type: string
          - type: object
            additionalProperties: 
              oneOf: 
                - type: string
                - type: object

      Rank:
        - type: string
          description: >
            Name of rank property to sort the items.
            - The property must have format RANK.
            - Order is descendent, from 5 starts to 1 star.