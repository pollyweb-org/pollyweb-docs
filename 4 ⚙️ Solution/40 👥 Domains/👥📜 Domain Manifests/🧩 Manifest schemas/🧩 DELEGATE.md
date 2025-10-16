# [🧩](<../../../30 Data/🧩 Schema Codes/🧩 Schema Code.md>) [`.MANIFEST`](<🧩 MANIFEST.md>) `/DELEGATE`

> Part of [`.MANIFEST` 🧩](<🧩 MANIFEST.md>)

> Implements [domain Manifest 📜](<../📜 Manifest.md>) 


* Delegated domain for authority-managed codes.
  * It allows for a manifest to be smaller, while keeping the ownership of the code group. 
  * For example, `profile.nlweb.org` defines all codes for `/PERSONA` on behalf of `nlweb.org`.
  * The delegated domain must reference the domain of the `Delegator`, as described in [`.MANIFEST/CODE` 🧩](<🧩 CODE.md>).

<br/>

## Example

```yaml
- Delegate: profile.nlweb.org
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
        $ref: Domain@nlweb.org/TYPES
        
      Code: 
        type: string