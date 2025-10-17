
# [🧩](<../../Schema Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../Schema Codes 🧩/🧩 Schema Code.md>): Token

> Schema of a [Token 🎫](<../🎫 Token.md>)

<br/>

## Definition

> [🤝:](<../../Schema Codes 🧩/🧩 Schema Code.md>) [`.MANIFEST/CODE`](<../../../40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /TOKEN
Name: Token
Description: >
  Base schema for verifiable tokens.
  The * can be replaced by schemas that inherit this.  

Schemas:
  Version: 1.0
  Inherits: nlweb.dom/LOCATOR:1.0

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