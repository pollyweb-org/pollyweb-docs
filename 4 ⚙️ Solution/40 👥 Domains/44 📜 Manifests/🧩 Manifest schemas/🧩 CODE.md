# [🧩](<../../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) [`.MANIFEST`](<🧩 MANIFEST.md>) `/CODE`

> Part of [`.MANIFEST` 🧩](<🧩 MANIFEST.md>)

> Implements [Schema Code🧩](<../../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)

> Indexed by [`Schema@Graph`](<../../../45 🛠️ Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Schema.md>)

<br/>

## Example

```yaml
Path: /GROUP/SUBGROUP/ANY-CODE
Delegator: any-delegator.com
Name: Any name
Description: Any description

Resources:

Translations: 
  en: Any Code
  pt: Um código qualquer

Schema: 
  Version: 1.0
  Format: {JSON Schema}

```

| Property | Type | Notes|
|-|-|-
| `Path`| string | Relative path of the [Code 🧩](<../../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)  or group
| [`Delegator 🧩`](<🧩 DELEGATE.md>) | string | Optional [Authority 🏛️ domain](<../../../45 🛠️ Helper domains/14 🏛️ Authorities/$ 🏛️🛠️ Authority helper.md>) that delegated: <br/>- i.e., added it to [`.MANIFEST/DELEGATE` 🧩](<🧩 DELEGATE.md>)
| `Name` | string | Human name of the [Schema Code 🧩](<../../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) 
| `Description`| string | Human  description of the [Schema Code 🧩](<../../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)  
| `Resources`  | map | Dictionary of external resources
| `Translations` | map | Dictionary of translations
| [`Schema 🧩`](<🧩 SCHEMA.md>)| object | Schema with [`.MANIFEST/CODE/SCHEMA` 🧩](<🧩 SCHEMA.md>)
|

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<🧩 CODE.md>)

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

      Delegator:
        $ref: Domain@nlweb.org/TYPES

      Name: 
        type: string

      Translations:
        type: array
        items: 
          $ref: .MANIFEST/TRANSLATION
      
      Schemas: 
        type: array
        items: 
          $ref: .MANIFEST/CODE/SCHEMA