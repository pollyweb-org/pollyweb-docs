
# [🧩](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>): Token

> Schema of a [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/$ 🎫 Token.md>)

<br/>

## Definition

> [🤝:](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>) [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/40 🧩 CODE code.md>)

```yaml
Path: /TOKEN
Name: Token
Description: >
  Base schema for verifiable tokens.
  The * can be replaced by schemas that inherit this.  

Schemas:
  Version: 1.0
  Inherits: nlweb.org/LOCATOR:1.0

  Properties:
    - Issued   #date
    - Starts   #date 
    - Expires  #date
    - '*'
    - Signature

  Format:
    type: object
    properties:
      Issued:
        type: date
      Starts:
        type: date
      Expires:
        type: date
      Signature:
        type: string