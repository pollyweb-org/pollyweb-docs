
# [🧩](<../../Codes 🧩/🧩 Schema Code.md>) `.TOKEN`

> About
* Schema of a [Token 🎫](<../🎫 Token/🎫 Token.md>)
* Inherits from [`.LOCATOR` 🧩](<../../../../7 🧩 Codes/$/🧩 LOCATOR.md>)

<br/>

## Definition

> [🤝:](<../../Codes 🧩/🧩 Schema Code.md>) [`.MANIFEST/CODE`](<../../Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /TOKEN
Version: 1.0
Inherits: .LOCATOR

Emoji: 🎫
Title: Token
Description: >
  Base schema for verifiable tokens.
  The * can be replaced by schemas that inherit this.  

Example: 

  # From .LOCATOR
  Schema: .TOKEN          # Schema derived from .TOKEN
  Domain: any-issuer.dom  # The Issuer name
  Key: token-1234         # Resource key in the Issuer
  Properties:             # Any optional data fields
      Property1: Value1
      Property2: Value2

  # From .TOKEN
  Schema: who.int/VACCINES/COVID-2:1.0
  Issued: 2024-09-21T12:34:00Z
  Starts: 2024-01-10T13:45:00.000Z
  Expires: 2028-12-10T13:45:00.000Z
  Signature: ABCMIQDALK2Fd...
  DKIM: pk1

Fields:
  - Issued   #date
  - Starts   #date 
  - Expires  #date
  - '*'
  - Signature

Asserts:
  AllOf: Issued, Starts, Signature
  Times: Issued, Starts, Expires
```        