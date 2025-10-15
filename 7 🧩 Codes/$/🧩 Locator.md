
# [🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): Locator

* Inherited by:
  * [`.TOKEN` 🧩](<🧩 Token.md>)
  * [`.HOST` 🧩](<../HOST/🧩 Host.md>)
  * [`.ALIAS` 🧩](<🧩 Alias.md>)

<br/>

## Definition

> [🤝:](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/11 🧩 CODE schema.md>)

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
