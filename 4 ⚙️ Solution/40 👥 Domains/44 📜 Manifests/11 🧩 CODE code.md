# [🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) [`.MANIFEST`](<10 🧩 MANIFEST code.md>) `/CODE`

> Part of [`.MANIFEST` 🧩](<10 🧩 MANIFEST code.md>)

> Implements [Schema Code🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)

> Indexed by [`Schema@Graph`](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/08 👥🚀🕸 Schema.md>)

<br/>

## Example

```yaml
Path: /GROUP/SUBGROUP/ANY-CODE
Delegator: any-delegator.com
Name: Any name
Description: |
  Any description

Schema: 
  Version: 1.0
  Format: {JSON Schema}

```

| Property | Type | Notes|
|-|-|-
| `Path`| string | Relative path of the [Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)  or group
| [`Delegator 🧩`](<13 🧩 DELEGATE code.md>) | string | Optional [Authority 🏛️ domain](<../43 👍 Trusts/02 🏛️🛠️ Authority helper.md>) that delegated: <br/>- i.e., added it to [`.MANIFEST/DELEGATE` 🧩](<13 🧩 DELEGATE code.md>)
| `Name` | string | Human name of the [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) 
| `Description`| string | Human  description of the [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)  
| `Resources`  | map | Dictionary of external resources
| [`Translations 🧩`](<16 🧩 TRANSLATION code.md>) | array | List of [`.MANIFEST/TRANSLATION` 🧩](<16 🧩 TRANSLATION code.md>)
| [`Schema 🧩`](<12 🧩 SCHEMA code.md>)| object | Schema with [`.MANIFEST/CODE/SCHEMA` 🧩](<12 🧩 SCHEMA code.md>)
|

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<11 🧩 CODE code.md>)

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

      Translations:
        type: array
        items: 
          $ref: .MANIFEST/TRANSLATION
      
      Schemas: 
        type: array
        items: 
          $ref: .MANIFEST/CODE/SCHEMA