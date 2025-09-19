
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): ProfileBooking
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /PROFILE/BOOKING
Name: Booking contact
Description: Share contact info for bookings.

Translations:
  pt-br: Contacto para agendamentos

Schema:
    
  Properties:
    - Name     # String /PROFILE/NAME/SOCIAL
    - Pronouns # String /PROFILE/NAME/PRONOUNS
    - Phones   # List of /PROFILE/PHONE
    - Emails   # List of /PROFILE/EMAIL

  Format:
    type: object
    required: [Name, Pronouns, Phones, Emails]
    properties:

      Name:
        $ref: nlweb.org/PROFILE/NAME/SOCIAL

      Pronouns:
        $ref: nlweb.org/PROFILE/NAME/PRONOUNS

      Phones:
        type: array
        minItems: 1
        items:
          $ref: nlweb.org/PROFILE/PHONE

      Emails:
        type: array
        minItems: 1
        items:
          type: nlweb.org/PROFILE/EMAIL