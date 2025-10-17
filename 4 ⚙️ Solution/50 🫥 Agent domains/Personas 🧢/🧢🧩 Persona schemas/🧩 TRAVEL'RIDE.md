
# [🧩](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>): PersonaTravelRide
<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PERSONA/TRAVEL/RIDE
Name: Ride Preferences
Description: >
  Ride preferences during a trip, for example in a taxi.

Schema:  

  Properties:
    - Conversation    # [QUITE, MUSIC, CHAT, WHATEVER]
    - Temperature     # [WARM, HOT, COOL, COLD, WHATEVER]

  Format:
    Conversation:
      enum: [QUITE, MUSIC, CHAT, WHATEVER]
    Temperature:
      enum: [WARM, HOT, COOL, COLD, WHATEVER]
  