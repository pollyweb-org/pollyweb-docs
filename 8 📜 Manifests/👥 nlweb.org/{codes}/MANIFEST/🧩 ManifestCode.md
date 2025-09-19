
# 🧩 ManifestCode
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /MANIFEST/CODE
Description: Authority-managed code.

Schema:
  Version: 1.0

  Properties:
    - Path          # Relative path of the code or group - e.g., /PROFILE (string)
    - Delegator     # OPtional domain of the domain that delegated the code (string)
    - Description   # Human readable Description of the code (string)
    - Name          # Human readable name of the code (string)
    - Resources     # Dictionary of external resources
    - Translations  # List of /MANIFEST/TRANSLATION (array)
    - Schemas       # List of /MANIFEST/CODE/SCHEMA (array)

  Format:
    type: object
    required: [Path]
    properties:

      Path:
        type: string
        example: /SSR/WCHR
        description: >
          Code for a user’s information in the given domain.
          - Domains that defined codes are called "authorities".
          - For shares from vaults to consumers, use <authority>/<code-path.
          - When a version is required, use <authority>/<code-path>:<schema-version>.
          - Version usages include check-in QRs, tokens, and json validations.

      Delegator:
        $ref: Domain@nlweb.org/TYPES
        example: nlweb.org
        description: > 
          Authority that delegated the definition of a code to this domain, 
          by adding this domain to its list of nlweb.org/MANIFEST/DELEGATE.

      Name: 
        type: string
        example: Profile codes
        details: >
          Human readable name of the code.
          This will be the name presented to users on their wallets upon
          sharing requests from consumer domains.

      Resources:
        type: object
        additionalProperties:
          type: string
        description: >
          Dictionary of external resources.
          These are tipically URLs to relevant webpages.

      Translations:
        type: array
        items: 
          $ref: nlweb.org/MANIFEST/TRANSLATION:1.0
      
      Schemas: 
        type: array
        items: 
          $ref: nlweb.org/MANIFEST/CODE/SCHEMA:1.0
