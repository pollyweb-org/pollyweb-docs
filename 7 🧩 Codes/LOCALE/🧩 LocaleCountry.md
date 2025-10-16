
# [🧩](<../../4 ⚙️ Solution/30 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 Data/1 🧩 Schema Codes/🧩 Schema Code.md>): LocaleCountry

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /LOCALE/COUNTRY
Name: Country response
Description: List of countries, for UI lists.

Schema:
  Version: 1.0

  Properties:
    - Display # Interpolation '{Flag} {Country}'
    - Flag    # Flag to display, ex. 🇬🇧
    - Country # Common country name, ex. United Kingdom
    - Alpha2  # Country code, ex. UK 
    
  Format:
    type: object
    required: [Display,Flag,Country,Alpha2]
    properties: 

      Display:
        type: string
        example: 🇬🇧 United Kingdom

      Alpha2:
        $ref: Alpha2@standards.any-igo.org/3166-1:1.0
        example: UK

      Country: 
        $ref: Name@locale.any-igo.org/TERRITORY:1.0
        example: United Kingdom
        
      Flag:
        $reg: Emoji@unicode.any-igo.org/FLAG:1.0
        example: 🇬🇧