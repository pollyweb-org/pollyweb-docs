# [🧩](<../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) [`.MANIFEST`](<10 🧩 MANIFEST code.md>) `/TRANSLATION`

> Used by [`.MANIFEST/ABOUT` 🧩](<20 🧩 ABOUT code.md>) and
[`.MANIFEST/CODE` 🧩](<40 🧩 CODE code.md>)

> Implements [domain Manifest 📜](<$ 📜 Domain Manifest.md>) 

<br/>

## Example

```yaml
Language: en
Translation: Any Domain
```

| Property | Type | Notes|
|-|-|-
| `Language`      | string | Translated language, e.g. `en`<br/>- from [`standards.any-igo.org` 📜](<../../../8 📜 Manifests/👥 any-igo.org/📜 standards.any-igo.org.md>)
| `Translation`   | string | Human readable translation of the name
|

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<40 🧩 CODE code.md>)

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