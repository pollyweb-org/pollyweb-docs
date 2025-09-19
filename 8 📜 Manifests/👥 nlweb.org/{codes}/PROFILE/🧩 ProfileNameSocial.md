```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /PROFILE/NAME/SOCIAL
Name: Social name

Description: >
  How a person wants to be refered to, socially.
  Tipically: first and last name, sometimes with a prefix/title.

References:
  GOV.UK Design System: https://design-system.service.gov.uk/patterns/names/

Translations:
  pt: Nome social

Schema:

  Properties:
    - Name      # Preferred social name
    - Pronouns  # //NAME/PRONOUNS
    
  Format: 
    type: object
    required: [Name]
    properties:
      Name:
        type: string
      Pronouns: 
        $ref: nlweb.org/PROFILE/NAME/PRONOUNS:1.0
