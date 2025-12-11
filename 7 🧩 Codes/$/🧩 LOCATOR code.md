
# [🧩](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>): Locator

> About
* Inherited by: [`.TOKEN`](<../../4 ⚙️ Solution/30 🧩 Data/Tokens 🎫/🧩 Token schemas/🧩 TOKEN.md>) [`.HOST`](<../../4 ⚙️ Solution/41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>) [`.ALIAS`](<../../4 ⚙️ Solution/45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>)

<br/>

## Definition

> [🤝:](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /LOCATOR
Version: 1.0
  
Example:
    Schema: airlines.any-igo.dom/SSR/WCHR/CRED:1.0
    Domain: health.any-nation.dom
    Resource: ANY-RESOURCE-KEY

Fields:
    Schema: A Schema Code.
    Domain: Domain that holds the resource.
    Resource: Unique index of a resource in the context of the domain.

Asserts:
    AllOf: Schema, Domain, Resource
    Texts: Schema, Domain, Resource
```