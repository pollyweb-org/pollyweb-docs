
# 🧩 [Schema Code](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): Manifest


 > Referenced by [domain Manifest 📜](<01 📜 Domain Manifest.md>)

<br/>


| Property | Type | Notes
|-|-|-
| [`Identity`](<14 🧩 Identity schema.md>)  | object | Domain identification.
| [`Datasets`](<15 🧩 Offer schema.md>)  | array | List of services offered.
| [`Trusts`](<17 🧩 Trust schema.md>)   | array | List of trusted domains and roles.
| [`Delegates`](<13 🧩 Delegate schema.md>) | array | List of delegated codes.
| [`Codes`](<11 🧩 Code schema.md>)     | array | List of defined codes.
|

<br/>

> 🤝: [`.MANIFEST/CODE`](<11 🧩 Code schema.md>)

```yaml

Path: /MANIFEST
Name: Domain Manifest

Schema:
  Version: 1.0

  Format:
    type: object
    required: [Identity]
    properties:

      Identity:
        $ref: nlweb.org/MANIFEST/IDENTITY:1.0

      Datasets:
        type: array
        description: list of services offered.
        items: 
          $ref: nlweb.org/MANIFEST/OFFER:1.0

      Trusts:
        type: array
        description: >
          List of trusted domains and roles.
        items:
          $ref: nlweb.org/MANIFEST/TRUST:1.0

      Delegates:
        type: array
        description: >
          List of delegated codes.
        items: 
          $ref: nlweb.org/MANIFEST/DELEGATE:1.0

      Codes: 
        type: array
        description: >
          List of defined codes:
        items:
          $ref: nlweb.org/MANIFEST/CODE:1.0