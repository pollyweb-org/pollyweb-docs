
# [🧩](<../../4 ⚙️ Solution/30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>): LocaleDialcode

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /LOCALE/DIALCODE
Name: Country dialing codes response
Description: List of country dialing codes, for UI lists.

Schema:
  Version: 1.0

  Properties:
    - Display # Interpolation '{Flag} {Country} (+{ISD})'
    - Flag    # Flag to display, ex. 🇬🇧
    - ISD     # International code, ex. 44
    - Country # Common country name, ex. United Kingdom
    - Alpha2  # Country code, ex. UK 

  Format:
    type: object
    required: [Display,Flag,ISD,Country,Alpha2]
    properties: 

      Display:
        type: string
        example: 🇬🇧 United Kingdom (+44)

      ISD:
        $ref: Code@telcos.any-igo.dom/ISD:1.0

      Alpha2:
        $ref: Alpha2@standards.any-igo.dom/3166-1:1.0

      Country: 
        $ref: Name@locale.any-igo.dom/TERRITORY:1.0

      Flag:
        $reg: Emoji@unicode.any-igo.dom/FLAG:1.0
        example: 🇬🇧