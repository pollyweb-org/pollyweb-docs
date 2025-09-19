
# 🧩 ManifestCodeSchema
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /MANIFEST/CODE/SCHEMA
Description: Schema for authority-managed code.

Resources:  
  JSON Schema Reference: https://json-schema.org/understanding-json-schema/reference

Schema:
  Version: 1.0
  
  Properties:
    - Output        # intent: SHARE|QR (enum)
    - Version       # Version of the schema as "major/breaks.minor/safe" (string)
    - Attributes    # Optional human readable list of attributes (array)
    - Inherits      # Optional inheritance for QR codes
    - Location      # Optional external location of the JSON schema (string)
    - Format:       # Optional JSON schema for machine validation (object)
        - $ref      # Sub-schema from another code:version#property.

  Format:
    type: object
    required: []
    properties:

      Output:
        enum: [SHARE, QR]
        description: >
          SHARE: the code is used to be shared between vaults and consumers.
          QR: the code is used for host check-ins it for offline tokens.

      Version:
        type: string
        default: 1.0
        example: 1.0
        description: > 
          Version of the schema as "<major>.<minor>".
          By convention, major versions mean that there was a breaking change.
          Minor versions mean that the the version is backward compatible.

      Properties:
        type: array
        contains: 
          - type: string
          - type: array
        description: >
          Simple list of code attributes for two purposes:
          1. Human readable description of the properties;
          2. Sequence definition for QR codes.

      Inherits:
        type: string
        example: nlweb.org/TOKEN:1.0
        description: >
          Another code from with to inherit the QR properties.
          - Format: <authority-domain>/<code-path>:<schema-version>
          - Note: the inherited schema should use * as a placeholder.
          Example of a parent sequence: 
          - Schema: nlweb.org/TOKEN:1.0
          - Properties: Code, Version, Issuer, Locator, Issued, Expires, *, Signature
          Example of an inherited token with additional metadata:
          - Schema: airlines.any-igo.org/SSR/WCHR:1.0
          - Inherits: nlweb.org/TOKEN:1.0
          - Properties: IsElectric, Size, NeedsAssistant, DateOfBirth

      Location:
        type: string
        format: uri
        example: https://schema.org/Person
        description: > 
          Optional external location of the JSON schema.

      Format:
        type: object
        description: >
          Format in JSON Schema for authority-managed code.
          Intended for automated machine validation.
          See https://json-schema.org/ for details.

        properties: 
          $ref: 
            type: string
            example: nlweb.org/MANIFEST/TRANSLATION:1.0
            description: > 
              Imports the format from another code in a domain manifest.
              The format is '<domain>/<path>:<version>'.
              This is the only special property.
              Everything else is defined by JSON Schema.
