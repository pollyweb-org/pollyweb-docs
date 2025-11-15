<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDA0807933d618043e6b1873dc74 -->
<!-- Source: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L255 -->

# 👥🚀🕸 Trusted @ Graph

> Part of [Graph 🕸 domain](<../../🕸 Graph/🕸🤲 Graph helper.md>)


* Verifies if there’s a path of [Trust 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) 
    * between two [domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) 
    * regarding a [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
    * as defined in the [`.MANIFEST/TRUST` 🧩](<../../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 TRUST.md>) part
    * of [domain Manifests 📜](<../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>).
  
*  Similar to [`Trusted@Graph`](<../👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>), 
   *  but for verification by the sender [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>).

<br/>

## Synchronous Request 🚀


```yaml
Header: 
    From: any-consumer.dom
    To: any-graph.dom
    Subject: Trusted@Graph

Body:
    Domain: any-vault.dom
    Role: VAULT
    Schema: any-authority.org/CODE/SUBCODE
```

|Object|Property|Type|Description
|-|-|-|-
| Header|`From`|string| The name of the sender [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|       |`To`|string| [Graph 🕸 domain](<../../🕸 Graph/🕸🤲 Graph helper.md>) name
|       | `Subject` | string | `Trusted@Graph`
| Body  | `Domain`  | string | The [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name to assess.
|       | `Role`    | enum   | The domain role to assess: `VAULT`, `CONSUMER`, `*`
|       | `Schema`    | string | The [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) to assess.
|

<br/>


## Synchronous Response 


```yaml
Trusted: True
Paths:
  - [any-vault.dom, any-authority.org]
  - [any-authority.org, any-consumer.dom]
```

|Property|Type|Description
|-|-|-
| `Trusted` | boolean       | [Trusted 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) or not.
| `Paths`   | string[][]    | The chain of [Trusts 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>).
|

<br/>