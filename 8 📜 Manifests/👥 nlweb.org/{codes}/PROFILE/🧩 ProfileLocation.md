
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /PROFILE/LOCATION
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
