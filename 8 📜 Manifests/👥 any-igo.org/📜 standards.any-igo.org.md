
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>): standards.any-igo.org

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: standards.any-igo.org
  Name: ISO, International Organization for Standardization


Codes:

  # --------------------------------------------------
  # [🧩](<../../4 ⚙️ Solution/25 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) /639-1 (Language codes)
  # --------------------------------------------------

  - Path: /639-1
    Name: Language codes
    Description: >
      ISO 639 is a standardized nomenclature used to classify languages. 
      In 639-1, each language is assigned a two-letter lowercase abbreviation.
    References: 
      ISO: https://www.iso.org/iso-639-language-codes.html
      Wikipedia: https://en.wikipedia.org/wiki/ISO_639-1
      Wikipedia Codes: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    Schemas:
      Properties: 
        - Code # e.g. "en" or "en-us"
        - Name # English
      Format:
        type: object
        required: [Code, Name]
        properties:
          Code: 
            oneOf:
              - type: string
                minLength: 2
                maxLength: 2
                example: en
              - type: string
                minLength: 5
                maxLength: 5
                example: en-us
          Name: 
            type: string
            example: English

  # --------------------------------------------------
  # [🧩](<../../4 ⚙️ Solution/25 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) /3166-1 (ISO 3166 Country Codes)
  # --------------------------------------------------

  - Path: /3166-1
    Name: ISO 3166 Country Codes
    Description: > 
      Internationally recognized codes of letters and/or numbers that 
      refer to countries and their subdivisions. 

    References:
      Official page: https://www.iso.org/iso-3166-country-codes.html
      List of countries: https://www.iso.org/obp/ui/#search/code/
      Wikipedia 1: https://en.wikipedia.org/wiki/ISO_3166-1
      Wikipedia 2: https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes

    Schemas:
      - Properties:
          - Name    # https://en.wikipedia.org/wiki/ISO_3166-1
          - Alpha2  # https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
          - Alpha3  # https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3
          - Numeric # https://en.wikipedia.org/wiki/ISO_3166-1_numeric

        Format:
          type: object
          required: [Name, Alpha2, Alpha3, Numeric]
          properties:
            Name:
              type: string
            Alpha2:
              description: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
              type: string
              minLength: 2
              maxLength: 2
            Alpha3:
              description: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3
              type: string
              minLength: 3
              maxLength: 3
            Numeric:
              type: int
              minimum: 0
              maximum: 999