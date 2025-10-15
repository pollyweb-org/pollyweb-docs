<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDA0807933d618043e6b1873dc74 -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L255 -->

# 👥🚀🕸 Trusted @ Graph

> ⚠️ This method doesn’t look at the header nor the signature of the request.

* Verifies if there’s a path of [Trust 👍](<../../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) 
    * between two [domains 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>) 
    * regarding a [Schema Code 🧩](<../../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)
    * as defined in the [`.MANIFEST/TRUST` 🧩](<../../../40 👥 Domains/44 📜 Manifests/50 🧩 TRUST code.md>) part
    * of [domain Manifests 📜](<../../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>).
  
*  Similar to [`Trusted@Graph`](<👥🚀🕸 Trusts.md>), 
   *  but for verification by the sender [domain 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>).

<br/>

## Synchronous Request 🚀


```yaml
Header: 
    From: any-consumer.com
    To: any-graph.com
    Subject: Trusted@Graph

Body:
    Domain: any-vault.com
    Role: VAULT
    Code: any-authority.org/CODE/SUBCODE
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the sender [domain 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>)
|       | `To`      | string | [Graph 🕸 domain](<../🕸🛠️ Graph helper.md>) name
|       | `Subject` | string | `Trusted@Graph`
| Body  | `Domain`  | string | The [domain 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>) name to assess.
|       | `Role`    | enum   | The domain role to assess: `VAULT`, `CONSUMER`, `*`
|       | `Code`    | string | The [Schema Code 🧩](<../../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) to assess.
|

<br/>


## Synchronous Response 


```yaml
Trusted: True
Paths:
  - [any-vault.com, any-authority.org]
  - [any-authority.org, any-consumer.com]
```

|Property|Type|Description
|-|-|-
| `Trusted` | boolean       | [Trusted 👍](<../../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) or not.
| `Paths`   | string[][]    | The chain of [Trusts 👍](<../../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>).
|

<br/>