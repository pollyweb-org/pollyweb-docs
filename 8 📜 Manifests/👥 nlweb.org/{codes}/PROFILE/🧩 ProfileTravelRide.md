
# 🧩 ProfileTravelRide
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /PROFILE/TRAVEL/RIDE
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
  
