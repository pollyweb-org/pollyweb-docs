# [🧩](<../../Codes 🧩/🧩 Schema Code.md>) [`.MANIFEST`](<🧩 MANIFEST.md>) `/OFFER`

> Part of [`.MANIFEST` 🧩](<🧩 MANIFEST.md>)

> Implements [domain Manifest 📜](<../📜 Manifest.md>) 


<br/>

## Properties

| Property | Type | Notes
|-|-|-
| `Dataset` | string | Reference to a [Schema 🧩](<../../Codes 🧩/🧩 Schema Code.md>) that defines the dataset being offered
| `Requires` | map | List of properties required as arguments to query the dataset 
|

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<🧩 CODE.md>)

```yaml
Path: /MANIFEST/OFFER
Name: Domain service offer

Blueprint: 

  Example: 
    Dataset: Code@standards.any-igo.dom/639-1
    Requires:
      Language: nlweb.dom/LOCALE/LANGUAGE:1.0

  Format: 
    type: object
    required: [Dataset, Requires]
    properties: 

      Dataset:
        $ref: Schema@nlweb.dom/TYPES
        example: nlweb.dom/LOCALE/COUNTRY:1.0
 
      Requires:
        type: object
        additionalProperties:
          $ref: Schema@nlweb.dom/TYPES
 