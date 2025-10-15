# [🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) [`.MANIFEST`](<10 🧩 MANIFEST code.md>) `/DELEGATE`

> Part of [`.MANIFEST` 🧩](<10 🧩 MANIFEST code.md>)

> Implements [domain Manifest 📜](<01 📜 Domain Manifest.md>) 


* Delegated domain for authority-managed codes.
  * It allows for a manifest to be smaller, while keeping the ownership of the code group. 
  * For example, `profile.nlweb.org` defines all codes for `/PERSONA` on behalf of `nlweb.org`.
  * The delegated domain must reference the domain of the `Delegator`, as described in [`.MANIFEST/CODE` 🧩](<11 🧩 CODE code.md>).

<br/>

## Properties
| Property | Type | Notes
|-|-|-
| `Delegate` | string | Domain to delegate to - e.g. `profile.nlweb.org` 
| `Code`     | string | Relative path of the code or group - e.g. `/PERSONA` 
|

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<11 🧩 CODE code.md>)

```yaml
Path: /MANIFEST/DELEGATE
Name: Domain delegate

Schema:
  Version: 1.0

  Format:
    type: object
    required: [Delegate, Code]
    properties:

      Delegate:
        $ref: Domain@nlweb.org/TYPES
        example: profile.nlweb.org
        
      Code: 
        type: string
        example: /PERSONA