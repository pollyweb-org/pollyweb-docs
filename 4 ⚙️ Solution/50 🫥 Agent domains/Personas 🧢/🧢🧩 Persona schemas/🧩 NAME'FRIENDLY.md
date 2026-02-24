
# [🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>): PersonaNameFriendly

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PERSONA/NAME/FRIENDLY
Title: Friendly name

Description: >
  How a person wants to be refered to amongst friends.
  Tipically: just the first name, or a nickname.

Translations:
  pt: Nome amigável

Blueprint:

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
        $ref: pollyweb.org/PERSONA/NAME/PRONOUNS:1.0
```