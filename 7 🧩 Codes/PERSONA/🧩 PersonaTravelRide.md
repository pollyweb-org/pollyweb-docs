
# [🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): PersonaTravelRide
```yaml
🤝: nlweb.org/MANIFEST/CODE

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
  