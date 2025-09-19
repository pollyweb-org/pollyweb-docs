
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): ProfileTravelSeat
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /PROFILE/TRAVEL/SEAT
Name: Seat preferences
Description: Share details on seat preferences.

Translations:
  pt: Preferência de assento

Schemas:
    
  Properties:
    - FaceForward
    - FaceBackwards
    - WithTable
    - WithoutTable
    - AtWindow
    - AtAisle
    - AtMiddle
    - AtFront
    - AtBack
    - OverWing
    - NearToilets
    - LongSeat
    - WideSeat

  Format:
    type: object
    properties:
      FaceForward:
        $ref: Rank@nlweb.org/TYPES
      FaceBackwards:
        $ref: Rank@nlweb.org/TYPES
      WithTable:
        $ref: Rank@nlweb.org/TYPES
      WithoutTable:
        $ref: Rank@nlweb.org/TYPES
      AtWindow:
        $ref: Rank@nlweb.org/TYPES
      AtAisle:
        $ref: Rank@nlweb.org/TYPES
      AtMiddle:
        $ref: Rank@nlweb.org/TYPES
      AtFront:
        $ref: Rank@nlweb.org/TYPES
      AtBack:
        $ref: Rank@nlweb.org/TYPES
      OverWing:
        $ref: Rank@nlweb.org/TYPES
      NearToilets:
        $ref: Rank@nlweb.org/TYPES
      LongSeat:
        $ref: Rank@nlweb.org/TYPES
      WideSeat:
        $ref: Rank@nlweb.org/TYPES