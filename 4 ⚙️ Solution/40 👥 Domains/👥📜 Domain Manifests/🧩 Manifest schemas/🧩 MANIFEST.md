# [🧩](<../../../30 Data/🧩 Schema Codes/🧩 Schema Code.md>) `.MANIFEST`

> Implements [domain Manifest 📜](<../📜 Manifest.md>) 


<br/>

## Properties

| Property | Type | Notes
|-|-|-
| [`About` 🧩](<🧩 ABOUT.md>) | object | [Domain 👥](<../../👥 Domains/👥 Domain.md>) identification
| [`Datasets` 🧩](<🧩 OFFER.md>)  | array | Optional services offered
| [`Trusts` 🧩](<🧩 TRUST.md>)   | array | Optional [Trusted 👍](<../../👥👍 Domain Trusts/👍 Domain Trust.md>) domains and roles
| [`Codes` 🧩](<🧩 CODE.md>)     | array | Optional [Schema Codes 🧩](<../../../30 Data/🧩 Schema Codes/🧩 Schema Code.md>) defined
| [`Delegates` 🧩](<🧩 DELEGATE.md>) | array | Optional [Schema Codes 🧩](<../../../30 Data/🧩 Schema Codes/🧩 Schema Code.md>) delegated
|

<br/>

## Definition

> [🤝:](<../../../30 Data/🧩 Schema Codes/🧩 Schema Code.md>) [`.MANIFEST/CODE`](<🧩 CODE.md>)

```yaml
Path: /MANIFEST
Name: Domain Manifest

Schema:
  Version: 1.0

  Format:
    type: object
    required: [Identity]
    properties:

      About:
        $ref: .MANIFEST/ABOUT

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