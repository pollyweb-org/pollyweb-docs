
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): ProfileNameFriendly
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /PROFILE/NAME/FRIENDLY
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
        $ref: nlweb.org/PROFILE/NAME/PRONOUNS:1.0