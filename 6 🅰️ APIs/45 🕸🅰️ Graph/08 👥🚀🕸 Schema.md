<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDAe24fd83cf9c244078a0f67f7f -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L413 -->

# 👥🚀🕸 Schema @ Graph

> Gets the schema of a [Schema Code 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) as defined it its [domain Manifests 📜](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>).

> ⚠️ This method doesn’t look at the header nor the signature of the request.

> When the schema references other schemas, 
> <br/>- this method returns the final merged schema for independent validation 
> <br/> - i.e., there's no need for further calls to get the referenced schemas.

<br/>

## Synchronous Request 🚀

```yaml
Header: 
    From: any-domain.com
    To: any-graph.com
    Subject: Schema@Graph

Body:
    Code: iata.org/SSR/WCHR:2.1
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) asking
|       | `To`      | string | [Graph 🕸 domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) name
|       | `Subject` | string | `Schema@Graph`
| Body  | `Code`    | string | [Schema Code 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
|


<br/>

## Synchronous Response

```yaml
Version: 2.1
Inherits: nlweb.org/CREDENTIAL:1
Location: https://iata.org/nlweb/schemas/SSR-WCHR.json
Format: IsElectric, Size, NeedsAssistant, DateOfBirth
```

|Property|Type|Description
|-|-|-
| `Version`  | timestamp | Start of matching period
| `Inherits` | timestamp | The base [Schema Code 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>), if inherited
| `Location` | string | URL to read the Schema from, if external
| `Format`   | string | The structure of the Schema
|