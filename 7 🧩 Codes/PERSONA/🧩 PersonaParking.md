
# [🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): PersonaParking
Path: /PERSONA/PARKING
Name: Vehicle
Description: Share vehicle licence plate and type for parking.

References:
  Smart Data Models: https://github.com/smart-data-models/dataModel.Transportation
  Wikipedia: https://en.wikipedia.org/wiki/Vehicle_registration_plate

Translations:
  pt: Viatura

Schema:

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
        $ref: Alpha2@standards.any-igo.org/3166-1
        description: The country of registration.