# [🧩](<../../30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) `.MANIFEST`

> Implements [domain Manifest 📜](<$ 📜 Domain Manifest.md>) 


<br/>

## Properties

| Property | Type | Notes
|-|-|-
| [`About` 🧩](<20 🧩 ABOUT code.md>) | object | [Domain 👥](<../$ 👥 Domains/$ 👥 Domain.md>) identification
| [`Datasets` 🧩](<60 🧩 OFFER code.md>)  | array | Optional services offered
| [`Trusts` 🧩](<50 🧩 TRUST code.md>)   | array | Optional [Trusted 👍](<../43 👍 Trusts/$ 👍 Domain Trust.md>) domains and roles
| [`Codes` 🧩](<40 🧩 CODE code.md>)     | array | Optional [Schema Codes 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) defined
| [`Delegates` 🧩](<30 🧩 DELEGATE code.md>) | array | Optional [Schema Codes 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) delegated
|

<br/>

## Definition

> [🤝:](<../../30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) [`.MANIFEST/CODE`](<40 🧩 CODE code.md>)

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