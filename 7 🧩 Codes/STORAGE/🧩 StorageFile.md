
# [🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): StorageFile
```yaml
🤝: nlweb.org/MANIFEST/CODE

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