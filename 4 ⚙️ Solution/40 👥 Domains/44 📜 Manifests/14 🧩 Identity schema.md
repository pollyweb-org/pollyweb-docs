# 🧩 [`.MANIFEST`](<10 🧩 Manifest schema.md>) `/IDENTITY`

> Part of [`.MANIFEST` 🧩](<10 🧩 Manifest schema.md>)

> Implements [domain Manifest 📜](<01 📜 Domain Manifest.md>) 

<br/>

## Properties

| Property | Type | Notes
|-|-|-
| `Domain` | string | DNS domain name, e.g. `any-domain.com`
| `Name` | string | Optional human readable title of the domain
| `Description` | string | Optional human readable description
| `SmallIcon`  | string | Optional URL to a small icon (20x20)
| `BigIcon`   | string | Optional URL to a big icon (100x100)
| `Feedback` | string | Optional [Buffer ⏳ helper domain](<../42 🌬️ Streams/03 ⏳🛠️ Buffer helper.md>) name <br/>- if not defined, then no feedback is given
| [`Translations` 🧩](<16 🧩 Translation schema.md>) | array | Optional translations of the domain name
|

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<11 🧩 Code schema.md>)

```yaml
Path: /MANIFEST/IDENTITY
Name: Domain identification

Schema:
  Version: 1.0

  Format:
    type: object
    required: [Domain]
    properties:
      
      Domain: 
        $ref: Domain@nlweb.org/TYPES
        example: any-domain.com
      
      Name: 
        type: string
        example: Any Domain
        
      SmallIcon: 
        type: string
        format: uri
        example: 'https://picsum.photos/20/20'
        
      BigIcon: 
        type: string
        format: uri
        example: 'https://picsum.photos/100/100'
        
      Feedback:
        example: any-buffer.com
        $ref: Domain@.MANIFEST/IDENTITY

      Translations: 
        type: array
        uniqueItems: true
        items:
          oneOf:
          
            - $ref: .MANIFEST/TRANSLATION
              example: 
                Language: en
                Translation: Name

            - type: object
              propertyNames: 
                $ref: Language@.MANIFEST/TRANSLATION
              example: 
                en: Name

      