
# [🧩](<../../4 ⚙️ Solution/25 Data/Schema Codes/02 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/25 Data/Schema Codes/02 🧩 Schema Code.md>): PersonaLocation

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/40 🧩 CODE code.md>)

```yaml
Path: /PERSONA/LOCATION
Name: Position

Description: 
  Geografic coordinates of a location in latitude and longitude.

Schema:  

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