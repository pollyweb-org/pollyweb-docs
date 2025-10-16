
# [🧩](<../../4 ⚙️ Solution/30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>): CrudEntityPropertyExternal

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /CRUD/ENTITY/PROPERTY/EXTERNAL
Name: External list property

Descrition: >
  Loads ONE|MANY options from an external domain.

Schema:
  Properties:
    - From  # Domain providing the information.
    - Read  # Code structure to read from the source.
    - Show  # Returned property to show to the user.
    - Save  # Returned property to be saved.

  Format:
    type: object
    required: [From, Read, Show, Save]
    properties: 

      From:
        format: string
        example: any-domain.com
        description: Domain providing the information.

      Read:
        format: string
        example: nlweb.org/LOCALE/DIALCODE
        description: Code structure to read from the source.

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