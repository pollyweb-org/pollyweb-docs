
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): ManifestTranslation
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /MANIFEST/TRANSLATION
Name: Manifest translation

Schema:
  Version: 1.0

  Properties:
    - Language      # Translated language, e.g. "en" (string)
    - Translation   # Human readable translation of the name (string)

  Format:
    type: object
    required: [Language, Translation]
    properties:
      
      Language:
        ref$: Code@standards.any-igo.org/639-1

      Translation:
        type: string
        example: Random name translated