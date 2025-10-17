
# [🧩](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>): PersonaTravelSeat

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PERSONA/TRAVEL/SEAT
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
        $ref: Rank@nlweb.dom/TYPES
      FaceBackwards:
        $ref: Rank@nlweb.dom/TYPES
      WithTable:
        $ref: Rank@nlweb.dom/TYPES
      WithoutTable:
        $ref: Rank@nlweb.dom/TYPES
      AtWindow:
        $ref: Rank@nlweb.dom/TYPES
      AtAisle:
        $ref: Rank@nlweb.dom/TYPES
      AtMiddle:
        $ref: Rank@nlweb.dom/TYPES
      AtFront:
        $ref: Rank@nlweb.dom/TYPES
      AtBack:
        $ref: Rank@nlweb.dom/TYPES
      OverWing:
        $ref: Rank@nlweb.dom/TYPES
      NearToilets:
        $ref: Rank@nlweb.dom/TYPES
      LongSeat:
        $ref: Rank@nlweb.dom/TYPES
      WideSeat:
        $ref: Rank@nlweb.dom/TYPES