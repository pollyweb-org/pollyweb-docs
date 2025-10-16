# [🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) [`.MANIFEST`](<🧩 MANIFEST.md>) `/CODE`

> Part of [`.MANIFEST` 🧩](<🧩 MANIFEST.md>)

> Implements [Schema Code🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)

> Indexed by [`Schema@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Schema.md>)

<br/>

## Example

```yaml
Path: /GROUP/SUBGROUP/ANY-CODE
Delegator: any-delegator.com
Name: Any name
Description: Any description

Resources:
  resource1: details1
  resourceN: detailsN

Translations: 
  en: Any Code
  pt: Um código qualquer

Schema: 
  Version: 1.0
  Inherits: .TOKEN:1.0
  Location: https://schema.org/Person
  Properties:
    - Prop1       # Description of Prop1
    - Prop2:      # Description of Prop2
        - Prop2A  # Description of Prop2A
        - Prop2B  # Description of Prop2B
  Format: 
    $ref: <property>@<code>:<version>

```

| Property | Type | Notes|
|-|-|-
| `Path`| string | Relative path of the [Code 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)  or group
| [`Delegator 🧩`](<🧩 DELEGATE.md>) | string | Optional [Authority 🏛️ domain](<../../../45 🤲 Helper domains/Authorities 🏛️/🏛️🤲 Authority helper.md>) that delegated: <br/>- i.e., added it to [`.MANIFEST/DELEGATE` 🧩](<🧩 DELEGATE.md>)
| `Name` | string | Human name of the [Schema Code 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) 
| `Description`| string | Human  description of the [Schema Code 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)  
| `Resources`  | map | Dictionary of external resources
| `Translations` | map | Dictionary of translations
| `Version`       | string | Version in `major/breaks`.`minor/safe`   
| `Properties`    | array  | Optional human readable list of attributes |
| `Inherits`      | string | Optional inheritance for QR codes | `.TOKEN`
| `Location`      | url | Optional external location of the [JSON schema](<https://json-schema.org/>) |
| `Format`       | object | Optional [JSON schema](<https://json-schema.org/>) for machine validation |
| `$ref 🧩`  | string | Sub-schema from `property`@`code`:`version`
|



### `Version` property

* Version of the schema as `<major>`.`<minor>`.
* By convention, major versions mean that there was a breaking change.
* Minor versions mean that the the version is backward compatible.


### `Properties` property

* Simple list of code attributes for two purposes:
  * 1/ Human readable description of the properties;
  * 2/ Sequence definition for QR codes.


### `Inherits` property

* Another code from with to inherit the QR properties.
  * Format: `<authority-domain>/<code-path>:<schema-version>`       
  * Note: the inherited schema should use `*` as a placeholder.

* Example of a parent sequence:
  ```yaml 
  # Schema: nlweb.org/TOKEN:1.0
  Properties: [ Code, Version, Issuer, Locator, Issued, Expires, *, Signature ]
  ```

* Example of an inherited token with additional metadata:
  ```yaml
  # Schema: airlines.any-igo.org/SSR/WCHR:1.0
  Inherits: nlweb.org/TOKEN:1.0
  Properties: [ IsElectric, Size, NeedsAssistant, DateOfBirth ]
  ```

### `$ref` property

* Imports the format from another code in a domain manifest.
* The format is `<domain>/<path>:<version>`.
* This is the only special property.
* Everything else is defined by [JSON schema](<https://json-schema.org/>).

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
      
      Schema: 
        type: object
        required: []
        properties:

          Version:
            type: string
            default: 1.0

          Properties:
            type: array
            contains: 
              - type: string
              - type: array

          Inherits:
            type: string
            
          Location:
            type: string
            format: uri
            
          Format:
            type: object

            properties: 
              $ref: 
                type: string