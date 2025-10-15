
# [🧩](<../../25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>) [`.MANIFEST`](<10 🧩 MANIFEST code.md>) `/TRUST`

> Part of [`.MANIFEST` 🧩](<10 🧩 MANIFEST code.md>)

> Implements [domain Manifest 📜](<$ 📜 Domain Manifest.md>) 
  
> Used by [`Trusted@Graph`](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/02 👥🚀🕸 Trusted.md>) and [`Trusts@Graph`](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/03 👥🚀🕸 Trusts.md>)

<br/>

## Properties

| Property | Type | Notes| Examples
|-|-|-|-
| `Expires`        | string | Date limit  in UTC timestamp | `2024-01-10`
| `Domain` | string | [Domain 👥](<../41 📨 Messages/00 👥 Domain.md>) to [Trust 👍](<../43 👍 Trusts/01 👍 Domain Trust.md>) <br/>- defaults to `*` | `*` `nlweb.org` 
| or `Domains` | array | Additional list of domains  | `[a.co, b.co]`
| `Query`  | string | [Schema Codes 🧩](<../../25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>) to [Trust 👍](<../43 👍 Trusts/01 👍 Domain Trust.md>) | `*` `/PERSONA/*`
| or `Queries`  | array | Additional list of queries | `[*]`
| `Role`     | enum | Role of domains to [Trust 👍](<../43 👍 Trusts/01 👍 Domain Trust.md>) <br/>- `VAULT` `CONSUMER`  <br/>- defaults to `*` | `*` `VAULT`
| or `Roles`     | array | Additional list of roles | `[*]`
| `Action`         | enum | Giving or removing [Trust 👍](<../43 👍 Trusts/01 👍 Domain Trust.md>) <br/>- `GRANT` `REVOKE` `INHERIT` <br/> - defaults to `GRANT` | `GRANT`
|


### `Role` property

  || Value | Notes
  |-|-|-
  || `VAULT` | The info disclosed by the named [Vault 🗄️](<../../25 Data/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) is trusted.  
  || `CONSUMER` | The named [Consumer 💼](<../../25 Data/27 💼 Consumers/04 💼🎭 Consumer role.md>) is allowed to perform queries.
  || `*` | Default, includes all options above.
  |


### `Action` property

||Value|Notes
|-|-|-
|| `GRANT` | Adds a trusted node to all possible trust paths.
||          | This is the default, if not specified.
|| `REVOKE` | Blocks the domain/role, even if there' a GRANT.
|| `INHERIT` | Inherits all revokes from a [Firewall 🔥 domain](<../../45 Helpers/21 Firewalls/03 🔥🛠️ Firewall helper.md>).
|
  
* Note: When a [Schema Code 🧩](<../../25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>) is removed from [`.MANIFEST/TRUSTS`](<50 🧩 TRUST code.md>), 
    * domains should explicitly inform the `REVOKE`;
    * otherwise, it might not be propagated by [Graph 🕸 domains](<../../42 Backbone/20 🕸 Graphs/$ 🕸🛠️ Graph helper.md>).


<br/>

## Defaults

* Inherit from [Firewall 🔥 domains](<../../45 Helpers/21 Firewalls/03 🔥🛠️ Firewall helper.md>) the revokes to malicious domains. 
  ```yaml
  # Protection from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
  ```

* Trust [Helper 🛠️ domains](<../../45 Helpers/$ 🛠️ Helpers/$ 🛠️👥 Helper domain.md>) certified by NLWeb.
  ```yaml
  # Certified Helpers
  - Action: GRANT
    Domain: nlweb.org
    Query: .HELPER/*
  ```


<br/>

## Definition 

> 🤝: [`.MANIFEST/CODE`](<40 🧩 CODE code.md>)

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
            example: nlweb.org/PERSONA/*

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
        $ref: Timestamp@nlweb.org/TYPES

      Domain:
        $ref: Domain@nlweb.org/TYPES
        default: '*'

      Domains:
        type: array
        items: 
          $ref: Domain@nlweb.org/TYPES
        minItems: 1

      Role:
        enum: [CONSUMER, VAULT, '*']
        default: '*'

      Roles:
        type: array
        minItems: 1
        items:
          enum: [CONSUMER, VAULT, '*']