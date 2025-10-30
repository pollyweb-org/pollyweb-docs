
# [🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>): PersonaLocation

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PERSONA/LOCATION
Name: Position

Description: 
  Geografic coordinates of a location in latitude and longitude.

Blueprint:  

  Properties:
    - Latitude  
    - Longitude    
  
  Format:
    type: object
    required: [Latitude, Longitude]
    properties:
      Latitude:
        type: number
      Longitude:
        type: number  