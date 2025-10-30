
# [🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>): PersonaAddress

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PERSONA/ADDRESS
Name: Address

Descriptions: >
  Consumers may use Google's Geocoding API to translate the address to coordinates.
  * Request: https://maps.googleapis.com/maps/api/geocode/json?address={Address},{Country}&key={key}

References: 
  Google Geocoding: https://developers.google.com/maps/documentation/javascript/geocoding

Translations:
  pt-pt: Morada
  pt-br: Endereço

Blueprint:  

  Properties:
    - Country         # ISO 3166-1 alpha-2 country code
    - Address         # Human readable multi-line address

  Format:
    type: object
    required: [Country, Address]
    properties:

      Country:
        $ref: Alpha2@standards.any-igo.dom/3166-1

      Address:
        type: string
        description: Complete national address.  