
# [🧩](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/02 🧩 Schema Code.md>): StorageFile

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/40 🧩 CODE code.md>)

```yaml
Path: /STORAGE/FILE
Description: Schema of a file share when migrating storages.

Schema:
  Location: https://nlweb.org/schemas/file.json
  Format:
    type: object
    properties:
      name:
        type: string
      type:
        type: string