
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): Manifest
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /MANIFEST
Name: Domain Manifest

Description: >
  Public information about a domain, available for querying on a well-known 
    web address - e.g. for (any-domain.com), the GET URL returning the 
    manifest in YAML format should be https://nlweb.{domain}/manifest. 
  - It is published to listeners by the Manifester component, 
    and then shared with subscribed Graphs.
  - It's in YAML (not JSON) for human-readability and to allow for comments.

Resources:
  NLWEB: 📜 https://quip.com/lcSaAX7AiEXL/-Domain

Schema:
  Version: 1.0

  Properties:
    - Identity     # Domain identification.
    - Datasets     # List of services offered.
    - Trusts       # List of trusted domains and roles.
    - Delegates    # List of delegated codes.
    - Codes        # List of defined codes.

  Format:
    type: object
    required: [Identity]
    properties:

      Identity:
        $ref: nlweb.org/MANIFEST/IDENTITY:1.0

      Datasets:
        type: array
        description: list of services offered.
        items: 
          $ref: nlweb.org/MANIFEST/OFFER:1.0

      Trusts:
        type: array
        description: >
          List of trusted domains and roles.
        items:
          $ref: nlweb.org/MANIFEST/TRUST:1.0

      Delegates:
        type: array
        description: >
          List of delegated codes.
        items: 
          $ref: nlweb.org/MANIFEST/DELEGATE:1.0

      Codes: 
        type: array
        description: >
          List of defined codes:
        items:
          $ref: nlweb.org/MANIFEST/CODE:1.0

          