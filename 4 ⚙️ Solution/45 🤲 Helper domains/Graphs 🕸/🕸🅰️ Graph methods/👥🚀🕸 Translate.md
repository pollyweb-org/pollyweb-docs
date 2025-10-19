<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDA9d34010d13574c2f95fe4de54 -->
<!-- Source: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L360 -->

# 👥🚀🕸 Translate @ Graph

> Part of [Graph 🕸 domain](<../🕸🤲 Graph helper.md>)

> ⚠️ This method doesn’t look at the header nor the signature of the request.

* [Broker 🤵 domains](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) 
    * request translation for [Schema Codes 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) and [domains 👥](<../../../40 👥 Domains/👥 Domain.md>),
    * obtained [domain Manifests 📜](<../../../30 🧩 Data/Manifests 📜/📜 Manifest.md>).
* Used by:
    * [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Prompts 🤔/👉💼 Share Bind 🔗.md>) flow
    * [💼⏩🧑‍🦰 Share Token @ Consumer](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Prompts 🤔/👉💼 Share Token 🎫.md>) flow

<br/>

## Synchronous Request 🚀

```yaml
Header: 
    From: any-domain.dom
    To: any-graph.dom
    Subject: Translate@Graph

Body: 
    Language: en-us
    Domains: 
      - any-domain.dom
    Schemas: 
      - iata.org/SSR/WCHR
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the [domain 👥](<../../../40 👥 Domains/👥 Domain.md>) asking
|       | `To`      | string | [Graph 🕸 domain](<../🕸🤲 Graph helper.md>) name
|       | `Subject` | string | `Translate@Graph`
|Body   | `Domains`     | string[]  | The [domains 👥](<../../../40 👥 Domains/👥 Domain.md>) to translate
|       | `Schemas`       | string[]  | The [Schema Codes 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) to translate
|

<br/>


## Synchronous Response

```yaml
Domains: 
  - Domain: example.com
    Translation: Example Airlines
Schemas: 
  - Schema: iata.org/SSR/WCHR
    Translation: Wheelchair assistance required
```

|Object|Property|Type|Description
|-|-|-|-
|Top    | `Domains`     | object[]  | List of [domain 👥](<../../../40 👥 Domains/👥 Domain.md>) objects
|       | `Schemas`       | object[]  | List of [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) objects
|Domain | `Domain`      | string    | The [domain 👥](<../../../40 👥 Domains/👥 Domain.md>) name
|       | `Translation` | string    | The [domain 👥](<../../../40 👥 Domains/👥 Domain.md>) title
|Code   | `Schema`        | string    | The [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|       | `Translation` | string    | The [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) title
|

<br/>