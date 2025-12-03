# [🧩](<../../Codes 🧩/🧩 Schema Code.md>) [`.MANIFEST`](<../📜 Manifest/📜 Manifest.md>) `/DELEGATE`

> Part of [`.MANIFEST` 🧩](<../📜 Manifest/📜 Manifest.md>)

> Implements [domain Manifest 📜](<../📜 Manifest/📜 Manifest.md>) 


* Delegated domain for authority-managed codes.
  * It allows for a manifest to be smaller, while keeping the ownership of the code group. 
  * For example, `profile.nlweb.dom` defines all codes for `/PERSONA` on behalf of `nlweb.dom`.
  * The delegated domain must reference the domain of the `Delegator`, as described in [`.MANIFEST/CODE` 🧩](<🧩 CODE.md>).

<br/>

## Example

```yaml
- Delegate: profile.nlweb.dom
  Schema: /PERSONA
```

| Property | Type | Notes
|-|-|-
| `Delegate` |text| Domain to delegate to.
| `Schema`     |text| Relative path of the code or group.
|

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<🧩 CODE.md>)

```yaml
Path: /MANIFEST/DELEGATE
Title: Domain delegate

Blueprint:
  Version: 1.0

  Format:
    type: object
    required: [Delegate, Code]
    properties:

      Delegate:
        $ref: Domain@nlweb.dom/TYPES
        
      Schema: 
        type: string
```        