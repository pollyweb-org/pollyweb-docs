
# [🧩](<../../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) [Schema Code](<../../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>): HostBooking

> Inherits from [`nlweb.org/TOKEN 🧩`](<../../../30 Data/30 🎫 Tokens/🧩 Token schemas/🧩 TOKEN.md>)

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /HOST/BOOKING
Name: Booking 
Description: Token for a booking

Translations:
  - Language: pt-br
    Translation: Agendamento

Schema:  
  Version: 1.0
  Inherits: nlweb.org/TOKEN:1.0
  
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