
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /PROFILE/DELIVERY
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
        $ref: Country@nlweb.org/PROFILE/ADDRESS:1.0

      Address:
        $ref: Address@nlweb.org/PROFILE/ADDRESS:1.0

      Phones:
        type: array
        items:
          $ref: nlweb.org/PROFILE/PHONE:1.0

      Notes:
        type: string
        description: Additional delivery intructions.
        example: Leave at the door step.
