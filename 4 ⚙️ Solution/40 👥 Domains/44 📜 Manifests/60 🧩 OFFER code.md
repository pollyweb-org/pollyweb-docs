# [🧩](<../../25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) [`.MANIFEST`](<10 🧩 MANIFEST code.md>) `/OFFER`

> Part of [`.MANIFEST` 🧩](<10 🧩 MANIFEST code.md>)

> Implements [domain Manifest 📜](<$ 📜 Domain Manifest.md>) 


<br/>

## Properties

| Property | Type | Notes
|-|-|-
| `Dataset` | string | Reference to a [Schema Code 🧩](<../../25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) that defines the dataset being offered
| `Requires` | map | List of properties required as arguments to query the dataset 
|

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<40 🧩 CODE code.md>)

```yaml
Path: /MANIFEST/OFFER
Name: Domain service offer

Schema: 

  Example: 
    Dataset: Code@standards.any-igo.org/639-1
    Requires:
      Language: nlweb.org/LOCALE/LANGUAGE:1.0

  Format: 
    type: object
    required: [Dataset, Requires]
    properties: 

      Dataset:
        $ref: Schema@nlweb.org/TYPES
        example: nlweb.org/LOCALE/COUNTRY:1.0
 
      Requires:
        type: object
        additionalProperties:
          $ref: Schema@nlweb.org/TYPES
 