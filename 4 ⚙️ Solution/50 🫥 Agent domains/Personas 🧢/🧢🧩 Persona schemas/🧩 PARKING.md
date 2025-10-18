
# [🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>): PersonaParking

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PERSONA/PARKING
Name: Vehicle
Description: Share vehicle licence plate and type for parking.

References:
  Smart Data Models: https://github.com/smart-data-models/dataModel.Transportation
  Wikipedia: https://en.wikipedia.org/wiki/Vehicle_registration_plate

Translations:
  pt: Viatura

Blueprint:

  Properties:
    - Plate   # The registration plate.
    - Country # The country of registration.
    
  Format:
    type: object
    properties:
      
      Plate:
        type: string
        maxLenght: 20
        description: The registration plate.

      Country:
        $ref: Alpha2@standards.any-igo.dom/3166-1
        description: The country of registration.