
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): ProfileAllergies
```yaml
🤝: nlweb.org/MANIFEST/CODE
          
Path: /PROFILE/ALLERGIES
Name: Allergies
Description: Share allergy info.

Translations:
  pt: Alergias

Schema:

  Properties:
    - Allergy # e.g. Peanuts
    - Level   # e.g. [LOW, HIGH, MEDIUM]
    - Notes   # free text

  Format:
    type: array
    items:
      type: object
      required: [Allergy, Level]
      properties:

        Allergy:
          type: string
          example: Peanuts

        Level:
          type: string
          enum: [LOW, MEDIUM, HIGH]

        Notes: 
          type: string
          maxLength: 1000