# [🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) [`.MANIFEST`](<10 🧩 Manifest schema.md>) `/TRANSLATION`

> Used by [`.MANIFEST/IDENTITY` 🧩](<14 🧩 Identity schema.md>) and
[`.MANIFEST/CODE` 🧩](<11 🧩 Code schema.md>)

> Implements [domain Manifest 📜](<01 📜 Domain Manifest.md>) 

<br/>

## Properties

| Property | Type | Notes|
|-|-|-
| `Language`      | string | Translated language, e.g. `en`<br/>- from [`standards.any-igo.org` 📜](<../../../8 📜 Manifests/👥 any-igo.org/📜 standards.any-igo.org.md>)
| `Translation`   | string | Human readable translation of the name
|

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<11 🧩 Code schema.md>)

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