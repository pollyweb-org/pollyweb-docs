
# [🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [`HOST`](<🧩 HOST.md>)/`BOOKING`

> Inherits from [`nlweb.dom/TOKEN 🧩`](<../../../30 🧩 Data/Tokens 🎫/🧩 Token schemas/🧩 TOKEN.md>)

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /HOST/BOOKING
Title: Booking 
Description: Token for a booking

Translations:
  - Language: pt-br
    Translation: Agendamento

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