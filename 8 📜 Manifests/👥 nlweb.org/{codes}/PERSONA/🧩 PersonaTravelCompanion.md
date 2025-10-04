
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): PersonaTravelCompanion
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /PERSONA/TRAVEL/COMPANION
Name: Travel Group

Description: > 
  Elements of a travel group.
  Tipically used in the check-in funnel of airline bookings.
  The list should contain all travellers, including the wallet owner.

Translations:
  pt: Grupo de Viagem

Schema:

  Properties:
    - Name       # First and last name of the person.
    - DocType    # Travel document type.
    - DocNumber  # Document type.
    - Expiration # Document expiration date.
    - Country    # Document issuer country.

  Format: 

    Name:
      type: string
      description: Group member name.

    DocType:
      enum: [ID, PASSPORT]
      description: Document type. 

    DocNumber:
      type: string
      description: Document number.

    Expiration:
      type: string
      format: date
      description: Document expiration date.

    Country: 
      $ref: Alpha2@standards.any-igo.org/3166-1
      description: Document issuer country.