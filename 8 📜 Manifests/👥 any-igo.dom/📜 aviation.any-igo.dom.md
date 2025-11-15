
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): aviation.any-igo.dom
<!--# 💺🏛️ https://quip.com/pm6aAVZug6N2-->

```yaml
🤝: nlweb.dom/MANIFEST
```

```yaml
About:
  Domain: aviation.any-igo.dom
  Title: All Aviation Members
```

```yaml
Schemas:
```

```yaml
  # Share of passport.
  - Path: /PASSPORT
    Title: Passport
    Translations:
      - Language: pt-br
        Translation: Passaporte
    Schemas:
      - Version: 1.0
        Location: https://en.wikipedia.org/wiki/Machine-readable_passport
        Properties: 
          - type        # for countries that distinguish between different types of passports
          - issuer      # country or org, ISO 3166-1 alpha-3
          - surname     # name of the person
          - givenName   # note: countries like Malasya don't differentiate surname and given name
          - number      # passport number
          - nationality # ISO 3166-1 alpha-3
          - birthDate   # date
          - birthPlace  # place of birth
          - sex         # M:male, F:female, U:unspecified
          - height      # e.g., 1.70m
          - issued      # date
          - expiration  # date
          - photo       # image serialized in base64
```

```yaml

  # Share of nationality, for Data Localization.
  - Path: /PASSPORT/COUNTRY
    Title: Nationality
    Translations:
      - Language: pt-br
        Translation: Nacionalidade
    Schemas:
      - Version: 1.0
        Format:
          # https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
          type: string     
```