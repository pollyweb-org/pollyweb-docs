🤝: nlweb.org/MANIFEST/CODE

Path: /MANIFEST/IDENTITY
Name: Domain identification
Description: > 
  Information for wallets to present the domain to end users.

Schema:
  Version: 1.0

  Properties:
    - Domain        # DNS domain name, e.g. any-domain.com (string)
    - Name          # Optional human readable title of the domain (string)
    - Description   # Optional human readable description (string)
    - SmallIcon     # Optional URL to a small icon (20x20)
    - BigIcon       # Optional URL to a big icon (100x100)
    - Translations  # Optional list of translations of the domain name.

  Format:
    type: object
    required: [Domain]
    properties:
      
      Domain: 
        $ref: Domain@nlweb.org/TYPES
        example: any-domain.com
        description: > 
          DNS domain name to reach the domain.
          The DNS registration needs to contain a DKIM with DNSSEC.
          The following endpoints need to exist:
          1. https://dtwf.{domain}/inbox (POST, receiving messages)
          2. https://dtwf.{domain}/manifest (GET, exposing the manifest)
      
      Name: 
        type: string
        example: Any Domain
        description: 
          Name displayed by wallets, if there's no matching translation.
          Translations in the wallet's language take precedence.

      SmallIcon: 
        type: string
        format: uri
        example: 'https://picsum.photos/20/20'
        description: >
          URL to a small icon (20x20) to be used by wallets.

      BigIcon: 
        type: string
        format: uri
        example: 'https://picsum.photos/100/100'
        description: >
          URL to a big icon (100x100) to be used by wallets.

      Translations: 
        type: array
        uniqueItems: true
        description: > 
          List of translations of the domain name.
        items:
          oneOf:
          
            - $ref: nlweb.org/MANIFEST/TRANSLATION:1.0
              example: 
                Language: en
                Translation: Name

            - type: object
              propertyNames: 
                $ref: nlweb.org/MANIFEST/TRANSLATION:1.0#Language
              example: 
                en: Name

