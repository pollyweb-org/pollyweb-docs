# [🧩](<../../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) [`.MANIFEST`](<🧩 MANIFEST.md>) `/TRANSLATION`

> Used by [`.MANIFEST/ABOUT` 🧩](<🧩 ABOUT.md>) and
[`.MANIFEST/CODE` 🧩](<🧩 CODE.md>)

> Implements [domain Manifest 📜](<../📜 Manifest.md>) 

<br/>

## Example

```yaml
Language: en
Translation: Any Domain
```

| Property | Type | Notes|
|-|-|-
| `Language`      | string | Translated language, e.g. `en`<br/>- from [`standards.any-igo.org` 📜](<../../../../8 📜 Manifests/👥 any-igo.org/📜 standards.any-igo.org.md>)
| `Translation`   | string | Human readable translation of the name
|

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<🧩 CODE.md>)

```yaml
Path: /MANIFEST/TRANSLATION
Name: Manifest translation

Schema:
  Version: 1.0

  Format:
    type: object
    required: [Language, Translation]
    properties:
      
      Language:
        ref$: Code@standards.any-igo.org/639-1

      Translation:
        type: string
        example: Random name translated