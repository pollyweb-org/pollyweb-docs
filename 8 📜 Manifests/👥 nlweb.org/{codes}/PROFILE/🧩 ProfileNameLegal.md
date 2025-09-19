```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /PROFILE/NAME/LEGAL
Name: Full legal name

Description: > 
  A person's full name, tipically for legal purposes.

Translations:
  pt: Nome legal completo

References:
  GOV.UK Design System: https://design-system.service.gov.uk/patterns/names/

Schema:

  Properties:
    - Name      # Legal name

  Format:
    type: object
    required: [Name]
    properties:
      Name:
        type: string
