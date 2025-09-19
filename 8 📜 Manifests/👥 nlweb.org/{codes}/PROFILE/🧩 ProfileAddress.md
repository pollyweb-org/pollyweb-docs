
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /PROFILE/ADDRESS
Name: Address

Descriptions: >
  Consumers may use Google's Geocoding API to translate the address to coordinates.
  * Request: https://maps.googleapis.com/maps/api/geocode/json?address={Address},{Country}&key={key}

References: 
  Google Geocoding: https://developers.google.com/maps/documentation/javascript/geocoding

Translations:
  pt-pt: Morada
  pt-br: Endereço

Schema:  

  Properties:
    - Country         # ISO 3166-1 alpha-2 country code
    - Address         # Human readable multi-line address

  Format:
    type: object
    required: [Country, Address]
    properties:

      Country:
        $ref: Alpha2@standards.any-igo.org/3166-1

      Address:
        type: string
        description: Complete national address.  
