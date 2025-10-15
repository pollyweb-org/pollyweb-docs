
# 🧩 [Schema Code](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): ManifestOffer

 > Referenced by [domain Manifest 📜](<01 📜 Domain Manifest.md>)

<br/>

```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /MANIFEST/OFFER
Name: Domain service offer

Schema: 
  Properties: 
    - Dataset # reference to a code schema for list items to return
    - Requires # List of properties required as arguments

  Example: 
    Dataset: Code@standards.any-igo.org/639-1
    Requires:
      Language: nlweb.org/LOCALE/LANGUAGE:1.0

  Format: 
    type: object
    required: [Dataset, Requires]
    properties: 

      Dataset:
        $ref: Schema@nlweb.org/TYPES
        example: nlweb.org/LOCALE/COUNTRY:1.0
        description: schema of the dataset.

      Requires:
        type: object
        description: Arguments for querying the dataset.
        additionalProperties:
          $ref: Schema@nlweb.org/TYPES
          description: The schema of the argument.