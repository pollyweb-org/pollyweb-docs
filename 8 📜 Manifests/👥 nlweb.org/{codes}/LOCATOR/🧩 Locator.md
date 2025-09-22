
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): Locator

> Inherited by:
> <br/>• [`nlweb/TOKEN 🧩`](<../TOKEN/🧩 Token.md>)
> <br/>• [`nlweb/HOST 🧩`](<../HOST/🧩 Host.md>)
> <br/>• [`nlweb/ALIAS  🧩`](<../../🧩 Alias.md>)

<br/>

```yaml
🤝: nlweb.org/MANIFEST/CODE

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
