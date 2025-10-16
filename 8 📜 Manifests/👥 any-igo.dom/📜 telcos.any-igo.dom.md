
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>): telcos.any-igo.dom
# 🇺🇳 ITU - International Telecommunication Union

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: telcos.any-igo.dom
  Name: ITU - International Telecommunication Union
  Description: >
    Specialized agency of the United Nations responsible for many matters related 
    to information and communication technologies.
  References:
    Home: https://www.itu.int/en/Pages/default.aspx
    Wikipedia: https://en.wikipedia.org/wiki/International_Telecommunication_Union

Codes:

  - Path: /ISD
    Name: International Subscriber Dialing (ISD)
    Description: Telephone country codes.
    References:
      Wikipedia: https://en.wikipedia.org/wiki/List_of_country_calling_codes
    Schemas:
      - Properties:
          - Code    # e.g. 1 for US
          - Country # see Alpha2@standards.any-igo.dom/3166-1
        Format:
          type: object
          properties:
            Code: 
              type: integer
              minimum: 1
              maximum: 999
            Country:
              $ref: Alpha2@standards.any-igo.dom/3166-1