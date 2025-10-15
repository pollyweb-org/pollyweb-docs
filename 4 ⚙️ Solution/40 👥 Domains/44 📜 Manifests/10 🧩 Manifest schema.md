# [🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) `.MANIFEST`

> Implements [domain Manifest 📜](<01 📜 Domain Manifest.md>) 


<br/>

## Properties

| Property | Type | Notes
|-|-|-
| [`Identity` 🧩](<14 🧩 IDENTITY schema.md>) | object | [Domain 👥](<../41 📨 Messages/00 👥 Domain.md>) identification
| [`Datasets` 🧩](<15 🧩 Offer schema.md>)  | array | Optional services offered
| [`Trusts` 🧩](<17 🧩 Trust schema.md>)   | array | Optional [Trusted 👍](<../43 👍 Trusts/01 👍 Domain Trust.md>) domains and roles
| [`Codes` 🧩](<11 🧩 CODE schema.md>)     | array | Optional [Schema Codes 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) defined
| [`Delegates` 🧩](<13 🧩 DELEGATE schema.md>) | array | Optional [Schema Codes 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) delegated
|

<br/>

## Definition

> [🤝:](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) [`.MANIFEST/CODE`](<11 🧩 CODE schema.md>)

```yaml
Path: /MANIFEST
Name: Domain Manifest

Schema:
  Version: 1.0

  Format:
    type: object
    required: [Identity]
    properties:

      Identity:
        $ref: .MANIFEST/IDENTITY

      Datasets:
        type: array
        items: 
          $ref: .MANIFEST/OFFER

      Trusts:
        type: array
        items:
          $ref: .MANIFEST/TRUST

      Delegates:
        type: array
        items: 
          $ref: .MANIFEST/DELEGATE

      Codes: 
        type: array
        items:
          $ref: .MANIFEST/CODE