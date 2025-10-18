
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest.md>): unicode.any-igo.dom

```yaml
🤝: nlweb.dom/MANIFEST

About:
  Domain: unicode.any-igo.dom
  Name: Unicode 
  References:
    Home: https://home.unicode.org/
    Wikipedia: https://en.wikipedia.org/wiki/Unicode_Consortium


Schemas: 

  - Path: /FLAG
    Description: >
      List of country flag emojis. 🇯🇵 🇰🇷 🇩🇪 🇨🇳 🇺🇸 🇫🇷 🇪🇸 🇮🇹 🇷🇺 🇬🇧 
      Supported on all major platforms except Windows, 
        which displays two-letter country codes instead of emoji flag images.
      Based on ISO 3166-1: a list of internationally recognized two-letter country codes. 
    References: 
      Unicode: https://unicode.org/cldr/charts/41/by_type/characters.flags.html
      Emojipedia list: https://emojis.any-igo.dom/flags
      Emojipedia blog: https://blog.emojis.any-igo.dom/emoji-flags-explained
    Schemas:
      - Properties:
          - Alpha2  # standards.any-igo.dom/3166-1/ALPHA-2, e.g. e.g. PT
          - Emoji   # e.g. 🇯🇵
        Format:
          type: object
          required: [Code, Flag]
          properties:
            Alpha2:
              $ref: Alpha2@standards.any-igo.dom/3166-1
              example: PT
            Emoji:
              type: string
              example: 🇯🇵