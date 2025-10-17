
# [🧩](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>): StorageFile

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /STORAGE/FILE
Description: Schema of a file share when migrating storages.

Schema:
  Location: https://nlweb.dom/schemas/file.json
  Format:
    type: object
    properties:
      name:
        type: string
      type:
        type: string