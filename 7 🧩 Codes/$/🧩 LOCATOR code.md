
# [🧩](<../../4 ⚙️ Solution/30 Data/🧩 Schema Codes/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 Data/🧩 Schema Codes/🧩 Schema Code.md>): Locator

* Inherited by:
  * [`.TOKEN` 🧩](<../../4 ⚙️ Solution/30 Data/🎫 Tokens/🧩 Token schemas/🧩 TOKEN.md>)
  * [`.HOST` 🧩](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🧩 Host schemas/🧩 HOST.md>)
  * [`.ALIAS` 🧩](<../../4 ⚙️ Solution/45 🤲 Helper domains/75 🖨️ Printers/🖨️🧩 Printer schemas/🧩 ALIAS.md>)

<br/>

## Definition

> [🤝:](<../../4 ⚙️ Solution/30 Data/🧩 Schema Codes/🧩 Schema Code.md>) [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /LOCATOR

Schema:
  Version: 1.0
  
  Properties:
    - Code      # e.g., airlines.any-igo.org/SSR/WCHR/CRED:1.0
    - Domain    # ex. health.any-nation.org
    - Resource  # ex. ANY-RESOURCE-KEY
    - '*'

  Format:
    type: object
    properties:

      Code:
        type: string
        title: A Schema Code.

      Domain:
        type: string
        title: Domain that holds the resource.

      Resource:
        type: string
        title: Unique index of a resource in the context of the domain.
