
# [🧩](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>): PersonaTravelSeat

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/40 🧩 CODE code.md>)

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