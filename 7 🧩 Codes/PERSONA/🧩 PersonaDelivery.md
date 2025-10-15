
# [🧩](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>): PersonaDelivery

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/40 🧩 CODE code.md>)

```yaml
Path: /PERSONA/DELIVERY
Name: Delivery address

Translations:
  pt: Endereço de entrega

Schema: 

  Properties:
    - Recipient # A name of a person or organization.
    - Country   # Country@//ADDRESS
    - Address   # Address@//ADDRESS
    - Phones    # List of contact phones.
    - Notes     # Additional delivery intructions.

  Format:
    type: object
    properties:

      Recipient:
        type: string
        description: >
          Name of the person or organization waiting for the delivery.

      Country: 
        $ref: Country@nlweb.org/PERSONA/ADDRESS:1.0

      Address:
        $ref: Address@nlweb.org/PERSONA/ADDRESS:1.0

      Phones:
        type: array
        items:
          $ref: nlweb.org/PERSONA/PHONE:1.0

      Notes:
        type: string
        description: Additional delivery intructions.
        example: Leave at the door step.