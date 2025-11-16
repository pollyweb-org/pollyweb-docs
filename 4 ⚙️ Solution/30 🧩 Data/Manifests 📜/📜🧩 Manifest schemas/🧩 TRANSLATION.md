# [🧩](<../../Codes 🧩/🧩 Schema Code.md>) [`.MANIFEST`](<../📜 Manifest/📜 Manifest.md>) `/TRANSLATION`

> Part of [`.MANIFEST` 🧩](<../📜 Manifest/📜 Manifest.md>)

> Implements [domain Manifest 📜](<../📜 Manifest/📜 Manifest.md>) 

* Localized metadata for manifest sections such as [`/ABOUT`](<🧩 ABOUT.md>) and [`/CODE`](<🧩 CODE.md>).
* Accepts either an array of translation objects or a map keyed by language codes.

<br/>

## Example

```yaml
Translations:
  - Language: pt-br
    Title: Um domínio qualquer
    Description: Isto é um domínio de exemplo.
```

| Property | Type | Notes
|-|-|-
| `Language` |text| [BCP-47 language tag](<https://www.rfc-editor.org/rfc/bcp/bcp47.txt>) identifying the translation
| `Title` |text| Optional translated title
| `Description` |text| Optional translated description
|

<br/>

## Definition

> 🤝: [`.MANIFEST/TRANSLATION`](<🧩 TRANSLATION.md>)

```yaml
Path: /MANIFEST/TRANSLATION
Title: Localization entry

Blueprint:
  Version: 1.0

  Format:
    type: object
    required: [Language]
    properties:

      Language:
        type: string
        pattern: '^[a-z]{2,3}(-[a-z0-9]{2,8})*$'

      Title:
        type: string

      Description:
        type: string
```
