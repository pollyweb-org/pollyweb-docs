
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): ManifestTrust

 > Referenced by [domain Manifest 📜](<../../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) and [domain Trust 👍](<../../../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>).

<br/>


```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /MANIFEST/TRUST
Name: Domain trust

Description: >
  Domains trusted (or not) by this one.
  NOTE: When a Code is removed from the trusts, domains should explicitly inform the REVOKE, otherwise it might not be propagated by filters.

Schema:
  Version: 1.0

  Properties:
    - Title          # Optional description of the trust (string)
    - Action         # Giving or removing trust [GRANT, REVOKE] (enum)
    - Expires        # Date limit of the trust in UTC timestamp
    - Role/Roles     # Purpose of referred actor [VAULT, CONSUMER] (enum)
    - Query/Queries  # Codes to trust - e.g. nlweb.org/PROFILE/* (string|array)
    - Domain/Domains # Domains to trust - e.g. nlweb.org (string|array)

  Format:
    type: object

    # Query or Queries must exist.
    oneOf:

      - required: [Query]
        properties: 
          Query:
            type: string
            example: nlweb.org/PROFILE/*
            description: > 
              Code or codes to trust.
              To trust a family of codes, the /* is required.
              For example, nlweb.org/PROFILE (without the *) only trusts the root code.

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
        description: Optional description of the trust.

      Action:
        enum: [GRANT, REVOKE, INHERIT]
        default: GRANT
        description: > 
          Giving or removing trust:
            - GRANT: adds a trusted node to all possible trust paths.
            - REVOKE: blocks the domain/role, even if there' a GRANT.
            - INHERIT: inherits all revokes from a firewall domain.
          Notes: 
            - REVOKE/INHERIT prevail over GRANT.
            - When a Code is removed from trusts, domains should consider explicitly 
              inform the REVOKE, otherwise it might not be propagated by graphs.

      Expires:
        $ref: Timestamp@nlweb.org/TYPES
        description: Date limit of the trust in UTC timestamp.

      Domain:
        $ref: Domain@nlweb.org/TYPES
        default: '*'
        description: > 
          Domain to trust.
          Merges with Domains, if available.

      Domains:
        type: array
        items: 
          $ref: Domain@nlweb.org/TYPES
        minItems: 1
        description: > 
          Domains to trust.
          Merges with Domain, if available.

      Role:
        enum: [CONSUMER, VAULT, '*']
        default: '*'
        description: > 
          Role of Domains to trust.
            - CONSUMER: the named domain is allowed to perform queries.
            - VAULT: the info disclosed by the named domain is trusted.
            - *: default, includes all options above.
          Notes: 
            - Merges with Roles, if available.

      Roles:
        type: array
        minItems: 1
        items:
          enum: [CONSUMER, VAULT, '*']
        description: > 
          Roles of Domains to trust.
          Merges with Role, if available.