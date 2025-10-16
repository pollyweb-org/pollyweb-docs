
# [🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>): PersonaEmergency

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PERSONA/EMERGENCY
Name: Emergency contacts

Translations:
  pt: Contatos de emergência

Schema:
    
  Properties:
    # List of:
    - Name          # /PERSONA/NAME/SOCIAL
    - Pronouns      # /PERSONA/NAME/PRONOUNS
    - Phone         # /PERSONA/PHONE
    - Relationship  # ex. Partner
    - Notes         # ex. Leave a message

  Format:   
    type: array
    items:
      type: object
      required: [Name, Pronouns, Phone, Relationship]
      properties:

        Name:
          $ref: nlweb.org.com/PERSONA/NAME/SOCIAL

        Pronouns:
          $ref: nlweb.org.com/PERSONA/NAME/PRONOUNS

        Phone:
          $ref: nlweb.org.com/PERSONA/PHONE

        Relationship:
          type: string
          example: Partner

        Notes:
          type: string
          example: Leave a message.
          description: Optional notes.