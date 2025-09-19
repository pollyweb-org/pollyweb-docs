
# 🧩 Token
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /TOKEN
Name: Token
Description: >
  Base schema for verifiable tokens.
  The * can be replaced by schemas that inherit this.  

Schemas:
  Output: QR
  Version: 1.0
  Inherits: nlweb.org/QR:1.0

  Properties:
    - Issued   #date
    - Starts   #date 
    - Expires  #date
    - '*'
    - Signature

  Format:
    type: object
    properties:
      Issued:
        type: date
      Starts:
        type: date
      Expires:
        type: date
      Signature:
        type: string
