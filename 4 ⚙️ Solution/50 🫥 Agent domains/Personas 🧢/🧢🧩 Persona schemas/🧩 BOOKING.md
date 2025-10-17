
# [🧩](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>): PersonaBooking

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PERSONA/BOOKING
Name: Booking contact
Description: Share contact info for bookings.

Translations:
  pt-br: Contacto para agendamentos

Schema:
    
  Properties:
    - Name     # String /PERSONA/NAME/SOCIAL
    - Pronouns # String /PERSONA/NAME/PRONOUNS
    - Phones   # List of /PERSONA/PHONE
    - Emails   # List of /PERSONA/EMAIL

  Format:
    type: object
    required: [Name, Pronouns, Phones, Emails]
    properties:

      Name:
        $ref: nlweb.dom/PERSONA/NAME/SOCIAL

      Pronouns:
        $ref: nlweb.dom/PERSONA/NAME/PRONOUNS

      Phones:
        type: array
        minItems: 1
        items:
          $ref: nlweb.dom/PERSONA/PHONE

      Emails:
        type: array
        minItems: 1
        items:
          type: nlweb.dom/PERSONA/EMAIL