
<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDA71b470c7a4c446e5b43adea7e -->
<!-- Source: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L279 -->

# 👥🚀🕸 Trusts @ [Graph](<../../🕸 Graph/🕸🤲 Graph helper.md>)

> Part of [Graph 🕸 domain](<../../🕸 Graph/🕸🤲 Graph helper.md>)

> Purpose

* Verifies if there’s a path of [Trust 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) 
  * between two [domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) 
  * regarding a [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
  * as defined in the [`.MANIFEST/TRUST` 🧩](<../../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 TRUST.md>) part
  * of [domain Manifests 📜](<../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>).

* Similar to [`Trusted@Graph`](<../👥🚀🕸 Trusted/🕸 Trusted 🚀 call.md>), 
  * but for verification by another [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>).
  
> Used in
* [🧑‍🦰👉💼 Share Token 🎫 flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>) 
* [🧑‍🦰👉💼 Share Bind 🔗 flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Bind 👉🔗💼/🧑‍🦰 Share Bind ⏩ flow.md>) 


<br/>

## Synchronous Call 🚀


```yaml
Header: 
    From: any-domain.dom
    To: any-graph.dom
    Subject: Trusted@Graph

Body:
    Truster: any-vault.dom
    Trusted: any-consumer.dom
    Role: CONSUMER
    Schema: any-authority.org/CODE/SUBCODE
```

|Object|Property|Type|Description
|-|-|-|-
| Header|`From`|string| The name of the sender [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|       |`To`|string| [Graph 🕸 domain](<../../🕸 Graph/🕸🤲 Graph helper.md>) name
|       | `Subject` | string | `Trusts@Graph`
| Body  | `Truster` | string | The name of the [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) trusting
|       | `Trusted` | string | The name of the [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) to be trusted
|       | `Role`    | enum   | The role to assess: `VAULT`, `CONSUMER`, `*`
|       | `Schema`    | string | The [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) to assess
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
| `Trusted` | boolean       | [Trusted 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) or not
| `Paths`   | string[][]    | The chain of [Trusts 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>)
|


<br/>