
# [🧩](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>) [`.MANIFEST`](<🧩 MANIFEST.md>) `/TRUST`

> Part of [`.MANIFEST` 🧩](<🧩 MANIFEST.md>)

> Implements [domain Manifest 📜](<../📜 Manifest.md>) 
  
> Used by [`Trusted@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusted.md>) and [`Trusts@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts.md>)

<br/>

## Properties

| Property | Type | Notes| Examples
|-|-|-|-
| `Expires`        | string | Date limit  in UTC timestamp | `2024-01-10`
| `Domain` | string | [Domain 👥](<../../../40 👥 Domains/👥 Domain.md>) to [Trust 👍](<../../../30 🧩 Data/Trusts 👍/👍 Domain Trust.md>) <br/>- defaults to `*` | `*` `nlweb.dom` 
| or `Domains` | array | Additional list of domains  | `[a.co, b.co]`
| `Query`  | string | [Schema Codes 🧩](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>) to [Trust 👍](<../../../30 🧩 Data/Trusts 👍/👍 Domain Trust.md>) | `*` `/PERSONA/*`
| or `Queries`  | array | Additional list of queries | `[*]`
| `Role`     | enum | Role of domains to [Trust 👍](<../../../30 🧩 Data/Trusts 👍/👍 Domain Trust.md>) <br/>- `VAULT` `CONSUMER`  <br/>- defaults to `*` | `*` `VAULT`
| or `Roles`     | array | Additional list of roles | `[*]`
| `Action`         | enum | Giving or removing [Trust 👍](<../../../30 🧩 Data/Trusts 👍/👍 Domain Trust.md>) <br/>- `GRANT` `REVOKE` `INHERIT` <br/> - defaults to `GRANT` | `GRANT`
|


### `Role` property

  || Value | Notes
  |-|-|-
  || `VAULT` | The info disclosed by the named [Vault 🗄️](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) is trusted.  
  || `CONSUMER` | The named [Consumer 💼](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) is allowed to perform queries.
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
  
* Note: When a [Schema Code 🧩](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>) is removed from [`.MANIFEST/TRUSTS`](<🧩 TRUST.md>), 
    * domains should explicitly inform the `REVOKE`;
    * otherwise, it might not be propagated by [Graph 🕸 domains](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🤲 Graph helper.md>).


<br/>

## Defaults

* Inherit from [Firewall 🔥 domains](<../../../45 🤲 Helper domains/Firewalls 🔥/🔥🤲 Firewall helper.md>) the revokes to malicious domains. 
  ```yaml
  # Protection from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
  ```

* Trust [Helper 🤲 domains](<../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) certified by NLWeb.
  ```yaml
  # Certified Helpers
  - Action: GRANT
    Domain: nlweb.dom
    Query: .HELPER/*
  ```


<br/>

## Definition 

> 🤝: [`.MANIFEST/CODE`](<🧩 CODE.md>)

```yaml
Path: /MANIFEST/TRUST
Name: Domain trust

Schema:
  Version: 1.0

  Format:
    type: object

    # Query or Queries must exist.
    oneOf:

      - required: [Query]
        properties: 
          Query:
            type: string
            example: nlweb.dom/PERSONA/*

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
        $ref: Timestamp@nlweb.dom/TYPES

      Domain:
        $ref: Domain@nlweb.dom/TYPES
        default: '*'

      Domains:
        type: array
        items: 
          $ref: Domain@nlweb.dom/TYPES
        minItems: 1

      Role:
        enum: [CONSUMER, VAULT, '*']
        default: '*'

      Roles:
        type: array
        minItems: 1
        items:
          enum: [CONSUMER, VAULT, '*']