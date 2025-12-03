<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDAe24fd83cf9c244078a0f67f7f -->
<!-- Source: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L413 -->

# 👥🚀🕸 Schema @ Graph

> Part of [Graph 🕸 domain](<../../🕸 Graph helper/🕸🤲 Graph helper.md>)

> Purpose

* Gets the schema of a [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) 
    * as defined in [`.MANIFEST/CODE` 🧩](<../../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>) 
    * of [domain Manifests 📜](<../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>).
* When the schema references other schemas with `$ref`, 
    * this method returns the final merged schema for independent validation 
    * i.e., there's no need for further calls to get the referenced schemas.


## Sync Call 🚀

```yaml
Header: 
    From: any-domain.dom
    To: any-graph.dom
    Subject: Schema@Graph

Body:
    Schema: iata.org/SSR/WCHR:2.1
    Language: pt-br
```

|Object|Property|Type|Description
|-|-|-|-
| Header|`From`|text| The name of the [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) asking
|       |`To`|text| [Graph 🕸 domain](<../../🕸 Graph helper/🕸🤲 Graph helper.md>) name
|       | `Subject` |text| `Schema@Graph`
| Body  | `Schema`    |text| [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|| `Language`  |text| Translation, defaults to `en-us`



## Sync Response

```yaml
Title: Assistência para mobilidade reduzida
Description: > 
    Assistência para passageiros com mobilidade reduzida, incluindo cadeira de rodas, andadores, muletas.
Version: 2.1
Inherits: nlweb.dom/CREDENTIAL:1
Location: https://iata.org/nlweb/schemas/SSR-WCHR.json
Format: IsElectric, Size, NeedsAssistant, DateOfBirth
```

|Property|Type|Description
|-|-|-
| `Title`    |text| Translated schema title
| `Description` |text| Translated schema description
| `Version`  | text | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) version
| `Inherits` | text | The base [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>), if inherited
| `Location` |text| URL to read the Schema from, if external
| `Format`   |text| The structure of the Schema
|