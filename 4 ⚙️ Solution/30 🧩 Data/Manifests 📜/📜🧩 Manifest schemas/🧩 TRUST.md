
# [🧩](<../../Codes 🧩/🧩 Schema Code.md>) [`.MANIFEST`](<../📜 Manifest/📜 Manifest.md>) `/TRUST`

> About
* Part of [`.MANIFEST` 🧩](<../📜 Manifest/📜 Manifest.md>)
* Implements [domain Manifest 📜](<../📜 Manifest/📜 Manifest.md>) 
* Used [`Trusts@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>)

<br/>

## Properties

| Property | Type | Notes| Examples
|-|-|-|-
| `Expires`        |text| Date limit  in UTC timestamp | `2024-01-10`
| `Domain` |text| [Domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) to [Trust 🫡](<../../Trusts 🫡/🫡 Domain Trust.md>) <br/>- defaults to `ANY` | `ANY` `pollyweb.org` 
| or `Domains` | array | Additional list of domains  | `[a.co, b.co]`
| `Query`  |text| [Schema Codes 🧩](<../../Codes 🧩/🧩 Schema Code.md>) to [Trust 🫡](<../../Trusts 🫡/🫡 Domain Trust.md>) | `ANY` `/PERSONA/*`
| or `Queries`  | array | Additional list of queries | `[*]`
| `Role`     | enum | Role of domains to [Trust 🫡](<../../Trusts 🫡/🫡 Domain Trust.md>) <br/>- `VAULT` `CONSUMER`  <br/>- defaults to `ANY` | `ANY` `VAULT`
| or `Roles`     | array | Additional list of roles | `[*]`
| `Action`         | enum | Giving or removing [Trust 🫡](<../../Trusts 🫡/🫡 Domain Trust.md>) <br/>- `GRANT` `REVOKE` `INHERIT` <br/> - defaults to `GRANT` | `GRANT`
|


### `Role` property

  || Value | Notes
  |-|-|-
  || `VAULT` | The info disclosed by the named [Vault 🗄️](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) is trusted.  
  || `CONSUMER` | The named [Consumer 💼](<../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) is allowed to perform queries.
  || `*` | Default, includes all options above.
  |


### `Action` property

||Value|Notes
|-|-|-
|| `GRANT` | Adds a trusted node to all possible trust paths.
||          | This is the default, if not specified.
|| `REVOKE` | Blocks the domain/role, even if there' a GRANT.
|| `INHERIT` | Inherits all revokes from a [Firewall 🔥 domain](<../../../45 🤲 Helper domains/Firewalls 🔥/🔥🤲 Firewall helper.md>).
|
  
* Note: When a [Schema 🧩](<../../Codes 🧩/🧩 Schema Code.md>) is removed from [`.MANIFEST/TRUSTS`](<🧩 TRUST.md>), 
    * domains should explicitly inform the `REVOKE`;
    * otherwise, it might not be propagated by [Graph 🕸 domains](<../../../45 🤲 Helper domains/Graphs 🕸/🕸 Graph helper/🕸🤲 Graph helper.md>).


<br/>

## Defaults

* Inherit from [Firewall 🔥 domains](<../../../45 🤲 Helper domains/Firewalls 🔥/🔥🤲 Firewall helper.md>) the revokes to malicious domains. 
  ```yaml
  # Protection from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
  ```

* Trust [Helper 🤲 domains](<../../../41 🎭 Domain Roles/Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>) certified by PollyWeb.
  ```yaml
  # Certified Helpers
  - Action: GRANT
    Domain: pollyweb.org
    Query: .HELPER/*
  ```


<br/>

## Definition 

> 🤝: [`.MANIFEST/CODE`](<🧩 CODE.md>)

```yaml
Path: /MANIFEST/TRUST
Title: Domain trust

Blueprint:
  Version: 1.0

  Format:
    type: object

    # Query or Queries must exist.
    oneOf:

      - required: [Query]
        properties: 
          Query:
            type: string
            example: pollyweb.org/PERSONA/*

      - required: [Queries]
        properties:
          Queries:
            type: array
            items: string
            minItems: 1

    # Everything else is optional.
    properties:

      Title: 
        type: string

      Action:
        enum: [GRANT, REVOKE, INHERIT]
        default: GRANT

      Expires:
        $ref: Timestamp@pollyweb.org/TYPES

      Domain:
        $ref: Domain@pollyweb.org/TYPES
        default: ANY

      Domains:
        type: array
        items: 
          $ref: Domain@pollyweb.org/TYPES
        minItems: 1

      Role:
        enum: [CONSUMER, VAULT, ANY]
        default: ANY

      Roles:
        type: array
        minItems: 1
        items:
          enum: [CONSUMER, VAULT, ANY]
```          