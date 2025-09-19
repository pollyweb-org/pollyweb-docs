🤝: nlweb.org/MANIFEST/CODE

Path: /PROFILE/EMERGENCY
Name: Emergency contacts

Translations:
  pt: Contatos de emergência

Schema:
    
  Properties:
    # List of:
    - Name          # /PROFILE/NAME/SOCIAL
    - Pronouns      # /PROFILE/NAME/PRONOUNS
    - Phone         # /PROFILE/PHONE
    - Relationship  # ex. Partner
    - Notes         # ex. Leave a message

  Format:   
    type: array
    items:
      type: object
      required: [Name, Pronouns, Phone, Relationship]
      properties:

        Name:
          $ref: nlweb.org.com/PROFILE/NAME/SOCIAL

        Pronouns:
          $ref: nlweb.org.com/PROFILE/NAME/PRONOUNS

        Phone:
          $ref: nlweb.org.com/PROFILE/PHONE

        Relationship:
          type: string
          example: Partner

        Notes:
          type: string
          example: Leave a message.
          description: Optional notes.