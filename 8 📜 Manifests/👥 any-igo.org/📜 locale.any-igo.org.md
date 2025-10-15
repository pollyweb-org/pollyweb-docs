
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>): locale.any-igo.org

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: locale.any-igo.org
  Name: Unicode Common Locale Data Repository (CLDR)
  Description: > 
    Provides key building blocks for software to support the world's languages, 
    with the largest and most extensive standard repository of locale data available. 
  References: 
    Homepage: https://cldr.unicode.org/
    GitHub: https://github.com/unicode-org/cldr/tree/main


Datasets:

  # [🧩](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) //COUNTRY list.
  - Dataset: nlweb.org/LOCALE/COUNTRY:1.0
    Requires: 
      Language: Code@standards.any-igo.org/639-1
    
  # [🧩](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) //DIALCODE list.
  - Dataset: nlweb.org/LOCALE/DIALCODE:1.0
    Requires: 
      Language: Code@standards.any-igo.org/639-1
      

Codes: 

  - Path: /TERRITORY
    Name: Country/Region (Territory) Names
    Description: >
      Country and region names (a.k.a. Territories) 
      may be used as part of Language/Locale Names, 
      or may be used in UI menus and lists to select countries or regions.
    References:
      CLDR: https://cldr.unicode.org/translation/displaynames/countryregion-territory-names
    Schemas:
      - Properties:
          - Code      # Alpha2@standards.any-igo.org/3166-1, e.g. "PT"
          - Name      # Name of the country in a given language, e.g. "Portugal"
        Format:
          type: array
          item:
            required: [ Code, Name ]
            properties: 
              Code:
                $ref: Alpha2@standards.any-igo.org/3166-1
              Name:
                type: string