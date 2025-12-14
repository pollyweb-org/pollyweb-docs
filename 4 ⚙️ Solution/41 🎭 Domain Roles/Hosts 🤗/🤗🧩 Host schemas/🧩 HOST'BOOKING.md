
# [🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [`.HOST`](<🧩 HOST.md>)/`BOOKING`

> Inherits from [`.TOKEN 🧩`](<../../../30 🧩 Data/Tokens 🎫/🧩 Token schemas/🧩 TOKEN.md>)

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /HOST/BOOKING

Title: Booking 
Description: Token for a booking
Translations:
    pt-br: Agendamento

Fields: 
    For: What is booked
    Time: When it is scheduled
    Place: Where it will take place
    Seat: Assigned seat, if any
    Latitude: Location latitude
    Longitude: Location longitude

Example: 
    For: Flight AB123
    Time: '10:35'
    Place: Gate 34
    Seat: 36B
    Latitude: 17.7283
    Longitude: -138.5184

Asserts:
    AllOf: For, Time, Place
    Texts: For, Place, Seat
    Times: Time
    Nums: Latitude, Longitude
    Place.MaxLength: 100
    Latitude.IsBetween: -90, 90
    Longitude.IsBetween: -180, 180
```

<br/>

## Deprecated

```yaml
Blueprint:  
  Version: 1.0
  Inherits: nlweb.dom/TOKEN:1.0
  
  Properties: 
    - For       # ex. Flight AB123
    - Time      # ex. 10:35
    - Place     # ex. Gate 34
    - Seat      # ex. 36B
    - Latitude  # ex. 17.7283
    - Longitude # ex. -138.5184
  Format:
    type: object
    properties:
      For:
        type: string
      Time:
        type: time
      Place:
        type: string
        title: Name of the place
        maxLength: 100
      Latitude:
        type: number
        minimum: -90
        maximum: 90
      Longitude:
        type: number
        minimum: -180
        maximum: 180
```  