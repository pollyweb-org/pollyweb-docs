
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): ManifestDelegate

 > Referenced by [domain Manifest 📜](<../../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>)

<br/>

```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /MANIFEST/DELEGATE
Name: Domain delegate

Description: >
  Delegated domain for authority-managed codes.
  - It allows for a manifest to be smaller, while keeping the ownership 
    of the code group. For example, (profile.nlweb.org) defines all codes 
    for /PROFILE on behalf of (nlweb.org).
  - The delegated domain must reference the domain of the Delegator, as 
    described in nlweb.org/MANIFEST/CODE.

Schema:
  Version: 1.0

  Properties:
    - Delegate  # Domain to delegate to - e.g. profile.nlweb.org (string)
    - Code      # Relative path of the code or group - e.g. /PROFILE (string)

  Format:
    type: object
    required: [Delegate, Code]
    properties:

      Delegate:
        $ref: Domain@nlweb.org/TYPES
        example: profile.nlweb.org
        description: >
          Domain authority to whom a code tree was delegated by another 
          domain authority, by adding it to the Delegates list.

      Code: 
        type: string
        example: /PROFILE