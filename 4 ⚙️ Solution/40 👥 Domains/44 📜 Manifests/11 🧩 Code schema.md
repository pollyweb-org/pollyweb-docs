
# 🧩 [Schema Code](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): ManifestCode

> Referenced by [domain Manifest 📜](<01 📜 Domain Manifest.md>)

<br/>

## Properties

| Property | Type | Notes|
|-|-|-
| `Path`| string | Relative path of the [Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)  or group
| [`Delegator`](<13 🧩 Delegate schema.md>) | string | Optional [Authority 🏛️ domain](<../43 👍 Trusts/02 🏛️🛠️ Authority helper.md>) that delegated: <br/>- i.e., added it to [`.MANIFEST/DELEGATE`](<13 🧩 Delegate schema.md>)
| `Description`| string | Human  description of the [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)  
| `Name` | string | Human name of the [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) 
| `Resources`  | map | Dictionary of external resources
| [`Translations`](<16 🧩 Translation schema.md>) | array | List of [`.MANIFEST/TRANSLATION`](<16 🧩 Translation schema.md>)
| [`Schemas`](<12 🧩 CodeSchema schema.md>)| array | List of [`.MANIFEST/CODE/SCHEMA`](<12 🧩 CodeSchema schema.md>)
|

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<11 🧩 Code schema.md>)

```yaml
Path: /MANIFEST/CODE
Description: Authority-managed code.

Schema:
  Version: 1.0

  Format:
    type: object
    required: [Path]
    properties:

      Path:
        type: string
        example: /SSR/WCHR

      Delegator:
        $ref: Domain@nlweb.org/TYPES
        example: nlweb.org

      Name: 
        type: string
        example: Persona codes

      Resources:
        type: object
        additionalProperties:
          type: string

      Translations:
        type: array
        items: 
          $ref: .MANIFEST/TRANSLATION
      
      Schemas: 
        type: array
        items: 
          $ref: .MANIFEST/CODE/SCHEMA