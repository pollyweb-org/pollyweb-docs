
# [🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>): PersonaEmergency

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PERSONA/EMERGENCY
Title: Emergency contacts

Translations:
  pt: Contatos de emergência

Blueprint:
    
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
          $ref: pollyweb.org/PERSONA/NAME/SOCIAL

        Pronouns:
          $ref: pollyweb.org/PERSONA/NAME/PRONOUNS

        Phone:
          $ref: pollyweb.org/PERSONA/PHONE

        Relationship:
          type: string
          example: Partner

        Notes:
          type: string
          example: Leave a message.
          description: Optional notes.
```