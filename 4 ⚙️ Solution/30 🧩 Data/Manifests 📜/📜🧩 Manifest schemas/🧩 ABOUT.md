# [🧩](<../../Codes 🧩/🧩 Schema Code.md>) [`.MANIFEST`](<🧩 MANIFEST.md>) `/ABOUT`

> Part of [`.MANIFEST` 🧩](<🧩 MANIFEST.md>)

> Implements [domain Manifest 📜](<../📜 Manifest/📜 Manifest.md>) 

<br/>

## Example

```yaml
About:
    Domain: any-domain.dom
    Title: Any Domain
    Description: This is a dummy domain.
    SmallIcon: 'https://picsum.photos/20/20'
    BigIcon: 'https://picsum.photos/100/100'

    Feedback: any-feedback.nlweb.dom

    Translations: 
        en: Any Domain
        pt: Um domínio qualquer
```

| Property | Type | Notes
|-|-|-
| `Domain` | string | DNS domain name
| `Title` | string | Optional human readable title of the domain
| `Description` | string | Optional human readable description
| `SmallIcon`  | string | Optional URL to a small icon (20x20)
| `BigIcon`   | string | Optional URL to a big icon (100x100)
| `Feedback` | string | Optional [Buffer ⏳ helper domain](<../../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) name <br/>- if not defined, then no feedback is given
| `Translations` | dict | Optional translations of the domain name
|

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<🧩 CODE.md>)

```yaml
Path: /MANIFEST/ABOUT
Title: Domain identification

Blueprint:
  Version: 1.0

  Format:
    type: object
    required: [Domain]
    properties:
      
      Domain: 
        $ref: Domain@nlweb.dom/TYPES
      
      Title: 
        type: string
        
      SmallIcon: 
        type: string
        format: uri
        
      BigIcon: 
        type: string
        format: uri
        
      Feedback:
        $ref: Domain@.MANIFEST/ABOUT

      Translations: 
        type: array
        uniqueItems: true
        items:
          oneOf:
          
            - $ref: .MANIFEST/TRANSLATION

            - type: object
              propertyNames: 
                $ref: Language@.MANIFEST/TRANSLATION
      