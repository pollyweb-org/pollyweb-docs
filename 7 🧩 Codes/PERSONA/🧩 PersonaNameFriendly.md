
# [🧩](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>): PersonaNameFriendly

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PERSONA/NAME/FRIENDLY
Name: Friendly name

Description: >
  How a person wants to be refered to amongst friends.
  Tipically: just the first name, or a nickname.

Translations:
  pt: Nome amigável

Schema:

  Properties:
    - Name      # Preferred friendly name
    - Pronouns  # //NAME/PRONOUNS

  Format:
    type: object
    required: [Name]
    properties:
      Name:
        type: string
      Pronouns: 
        $ref: nlweb.org/PERSONA/NAME/PRONOUNS:1.0