
# [🧩](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>): Types

<br/>

## Definition

> [🤝:](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /TYPES

Blueprint: 
  Format: 
    properties: 

      Code:
        type: string
        example: nlweb.dom/LOCATOR
        description: >
          Reference to a data type defined by the manifest of an authority.
          It's composed by the authority's domain and code path.
          For example, for [nlweb.dom/LOCATOR]:
          - the manifest is at http://nlweb.dom.com/manifest;
          - the schema definition is at 'Path:/LOCATOR' inside the manifest.
          Note: the manifest may delegate the definition to sub manifests.

      Domain:
        type: string
        format: hostname  
        example: any-domain.dom
        description: An internet domain name.

      Key:
        type: string
        description: Public Key, from a a key pair.

      Rank:
        type: integer
        minimum: 1
        maximum: 5
        description: Star rank.

      Schema: 
        type: string
        example: nlweb.dom/LOCATOR:3.11
        description: >
          Reference to the schema of data type defined by the manifest of an authority.
          It's composed by the authority's domain, code path, and an optional version.
          For example, for [nlweb.dom/LOCATOR:3.11]:
          - the manifest is at http://nlweb.dom.com/manifest;
          - the schema definition is at 'Path: /LOCATOR' inside the manifest;
          - the version of the schema is 3.11 (if omitted, defaults to 1.0).
          For example, for [nlweb.dom/LOCATOR]:
          - the version of the schema is 1.0 (the default).
          Note: the manifest may delegate the definition to sub manifests.

      Timestamp:
        type: string
        format: utc.datetime
        example: '2098-12-10T13:45:00.000Z'
        description: Date time in UTC format.

      UUID:
        type: string
        format: uuid
        example: 28ff57b4-76f6-4944-a710-a71f9d667cee
        description: Universal unique identifier.