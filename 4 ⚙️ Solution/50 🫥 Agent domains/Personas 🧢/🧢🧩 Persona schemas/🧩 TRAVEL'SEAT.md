
# [🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>): PersonaTravelSeat

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PERSONA/TRAVEL/SEAT
Title: Seat preferences
Description: Share details on seat preferences.

Translations:
  pt: Preferência de assento

Blueprint:
    
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
        $ref: Rank@pollyweb.org/TYPES
      FaceBackwards:
        $ref: Rank@pollyweb.org/TYPES
      WithTable:
        $ref: Rank@pollyweb.org/TYPES
      WithoutTable:
        $ref: Rank@pollyweb.org/TYPES
      AtWindow:
        $ref: Rank@pollyweb.org/TYPES
      AtAisle:
        $ref: Rank@pollyweb.org/TYPES
      AtMiddle:
        $ref: Rank@pollyweb.org/TYPES
      AtFront:
        $ref: Rank@pollyweb.org/TYPES
      AtBack:
        $ref: Rank@pollyweb.org/TYPES
      OverWing:
        $ref: Rank@pollyweb.org/TYPES
      NearToilets:
        $ref: Rank@pollyweb.org/TYPES
      LongSeat:
        $ref: Rank@pollyweb.org/TYPES
      WideSeat:
        $ref: Rank@pollyweb.org/TYPES
```