
# [🧩](<../../Codes 🧩/🧩 Schema Code.md>) `.TOKEN` Schema

> About
* Schema of a [Token 🎫](<../🎫 Token/🎫 Token.md>)

<br/>

## Definition

> [🤝:](<../../Codes 🧩/🧩 Schema Code.md>) [`.MANIFEST/CODE`](<../../Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /TOKEN
Version: 1.0

Emoji: 🎫
Title: Token
Description: >
  Base schema for verifiable tokens.
  The * can be replaced by schemas that inherit this.  

Example: 
  Token: token-1234       
  Issuer: any-issuer.dom  
  Schema: any-authority.com/ANY/PATH:1.0 
  Context: {A:1,B:2} 
  Issued: 2024-09-21T12:34:00Z
  Starts: 2024-01-10T13:45:00.000Z
  Expires: 2028-12-10T13:45:00.000Z
  Identity: any-identity.dom
  Biostamp: person-1234
  Signature: ABCMIQDALK2Fd...
  DKIM: pk1

Asserts:
  AllOf: Token, Issuer, Schema, Issued, Starts, Signature, DKIM
  UUID: Token, Biostamp
  Texts: Signature, DKIM
  Times: Issued, Starts, Expires
  Issuer.IsDomain:
  Identity.IsDomain:
  Schema.IsSchema:
```        