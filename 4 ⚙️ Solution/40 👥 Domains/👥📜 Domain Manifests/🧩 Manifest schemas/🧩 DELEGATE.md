# [🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) [`.MANIFEST`](<🧩 MANIFEST.md>) `/DELEGATE`

> Part of [`.MANIFEST` 🧩](<🧩 MANIFEST.md>)

> Implements [domain Manifest 📜](<../📜 Manifest.md>) 


* Delegated domain for authority-managed codes.
  * It allows for a manifest to be smaller, while keeping the ownership of the code group. 
  * For example, `profile.nlweb.dom` defines all codes for `/PERSONA` on behalf of `nlweb.dom`.
  * The delegated domain must reference the domain of the `Delegator`, as described in [`.MANIFEST/CODE` 🧩](<🧩 CODE.md>).

<br/>

## Example

```yaml
- Delegate: profile.nlweb.dom
  Code: /PERSONA
```

| Property | Type | Notes
|-|-|-
| `Delegate` | string | Domain to delegate to.
| `Code`     | string | Relative path of the code or group.
|

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<🧩 CODE.md>)

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
        $ref: Domain@nlweb.dom/TYPES
        
      Code: 
        type: string