# [🧩](<../../Codes 🧩/🧩 Schema Code.md>) [`.MANIFEST`](<../📜 Manifest/📜 Manifest.md>) `/ABOUT`

> Part of [`.MANIFEST` 🧩](<../📜 Manifest/📜 Manifest.md>)

> Implements [domain Manifest 📜](<../📜 Manifest/📜 Manifest.md>) 

<br/>

## Example

```yaml
About:
    Domain: any-domain.dom
    Language: en-us
    Title: Any Domain
    Description: This is a dummy domain.
    SmallIcon: 'https://picsum.photos/20/20'
    BigIcon: 'https://picsum.photos/100/100'

    Translations: 
      - Language: pt-br
        Title: Um domínio qualquer
        Description: Isto é um domínio de exemplo.
```

| Property | Type | Notes
|-|-|-
| `Domain` |text| DNS domain name
| `Language`|text| [Manifest 📜](<../📜 Manifest/📜 Manifest.md>) language, defaults to `en-us`
| `Title` |text| Optional human readable title of the domain
| `Description` |text| Optional human readable description
| `SmallIcon`  |text| Optional URL to a small icon (20x20)
| `BigIcon`   |text| Optional URL to a big icon (100x100)
| `Translations` | [set](<../../../37 Scripts 📃/📃 Holders 🧠/Set 📚 holders/🧠 Set holders.md>) | Optional translations of the domain name
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

      Translations: 
        type: array
        uniqueItems: true
        items:
          oneOf:
          
            - $ref: .MANIFEST/TRANSLATION

            - type: object
              propertyNames: 
                $ref: Language@.MANIFEST/TRANSLATION
      