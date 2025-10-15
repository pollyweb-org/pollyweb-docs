
# [🧩](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>): PersonaBooking

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/40 🧩 CODE code.md>)

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
        $ref: nlweb.org/PERSONA/NAME/SOCIAL

      Pronouns:
        $ref: nlweb.org/PERSONA/NAME/PRONOUNS

      Phones:
        type: array
        minItems: 1
        items:
          $ref: nlweb.org/PERSONA/PHONE

      Emails:
        type: array
        minItems: 1
        items:
          type: nlweb.org/PERSONA/EMAIL