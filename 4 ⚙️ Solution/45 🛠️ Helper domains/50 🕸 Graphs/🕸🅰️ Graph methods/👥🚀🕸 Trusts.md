
<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDA71b470c7a4c446e5b43adea7e -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L279 -->

# 👥🚀🕸 Trusts @ [Graph](<../🕸🛠️ Graph helper.md>)

> ⚠️ This method doesn’t look at the header nor the signature of the request.


* Verifies if there’s a path of [Trust 👍](<../../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) 
  * between two [domains 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>) 
  * regarding a [Schema Code 🧩](<../../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)
  * as defined in the [`.MANIFEST/TRUST` 🧩](<../../../40 👥 Domains/44 📜 Manifests/🧩 Manifest schemas/🧩 TRUST.md>) part
  * of [domain Manifests 📜](<../../../40 👥 Domains/44 📜 Manifests/📜 Manifest.md>).

* Similar to [`Trusted@Graph`](<👥🚀🕸 Trusted.md>), 
  * but for verification by another [domain 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>).
  
* Used in:
  * [🧑‍🦰👉💼 Share Token 🎫 flow](<../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token 🎫.md>) 
  * [🧑‍🦰👉💼 Share Bind 🔗 flow](<../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind 🔗.md>) 


<br/>

## Synchronous Request 🚀


```yaml
Header: 
    From: any-domain.com
    To: any-graph.com
    Subject: Trusted@Graph

Body:
    Truster: any-vault.com
    Trusted: any-consumer.com
    Role: CONSUMER
    Code: any-authority.org/CODE/SUBCODE
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the sender [domain 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>)
|       | `To`      | string | [Graph 🕸 domain](<../🕸🛠️ Graph helper.md>) name
|       | `Subject` | string | `Trusts@Graph`
| Body  | `Truster` | string | The name of the [domain 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>) trusting
|       | `Trusted` | string | The name of the [domain 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>) to be trusted
|       | `Role`    | enum   | The role to assess: `VAULT`, `CONSUMER`, `*`
|       | `Code`    | string | The [Schema Code 🧩](<../../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) to assess
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
| `Trusted` | boolean       | [Trusted 👍](<../../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) or not
| `Paths`   | string[][]    | The chain of [Trusts 👍](<../../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>)
|


<br/>