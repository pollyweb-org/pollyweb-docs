# [🧩](<../../25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>) [`.MANIFEST`](<10 🧩 MANIFEST code.md>) [`/CODE`](<40 🧩 CODE code.md>) `/SCHEMA`

> Part of [`.MANIFEST/CODE` 🧩](<40 🧩 CODE code.md>)

> Implements [domain Manifest 📜](<01 📜 Domain Manifest.md>) 


<br/> 

## Example

```yaml
Version: 1.0
Inherits: .TOKEN:1.0
Location: https://any-domain/any-schema.json
Properties:
  - Prop1       # Description of Prop1
  - Prop2:      # Description of Prop2
      - Prop2A  # Description of Prop2A
      - Prop2B  # Description of Prop2B
Format: 
  $ref: <property>@<code>:<version>
```

| Property | Type | Notes
|-|-|-
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
  Properties: Code, Version, Issuer, Locator, Issued, Expires, *, Signature
  ```

* Example of an inherited token with additional metadata:
  ```yaml
  # Schema: airlines.any-igo.org/SSR/WCHR:1.0
  Inherits: nlweb.org/TOKEN:1.0
  Properties: IsElectric, Size, NeedsAssistant, DateOfBirth
  ```

### `$ref` property

* Imports the format from another code in a domain manifest.
* The format is `<domain>/<path>:<version>`.
* This is the only special property.
* Everything else is defined by [JSON schema](<https://json-schema.org/>).

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<40 🧩 CODE code.md>)

```yaml
Path: /MANIFEST/CODE/SCHEMA
Description: Schema for authority-managed code.

Schema:
  Version: 1.0
  
  Format:
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
        example: nlweb.org/TOKEN:1.0
        
      Location:
        type: string
        format: uri
        example: https://schema.org/Person
        
      Format:
        type: object

        properties: 
          $ref: 
            type: string
            example: nlweb.org/MANIFEST/TRANSLATION:1.0