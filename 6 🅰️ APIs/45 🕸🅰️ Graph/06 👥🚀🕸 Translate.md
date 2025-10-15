<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDA9d34010d13574c2f95fe4de54 -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L360 -->

# 👥🚀🕸 Translate @ Graph


> ⚠️ This method doesn’t look at the header nor the signature of the request.

* [Broker 🤵 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) 
    * request translation for [Schema Codes 🧩](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) and [domains 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>),
    * obtained from [`.MANIFEST/TRANSLATION` 🧩](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/21 🧩 TRANSLATION code.md>) parts
    * of [domain Manifests 📜](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>).
* Used by:
    * [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind 🔗.md>) flow
    * [💼⏩🧑‍🦰 Share Token @ Consumer](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token 🎫.md>) flow

<br/>

## Synchronous Request 🚀

```yaml
Header: 
    From: any-domain.com
    To: any-graph.com
    Subject: Translate@Graph

Body: 
    Language: en-us
    Domains: 
      - any-domain.com
    Codes: 
      - iata.org/SSR/WCHR
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) asking
|       | `To`      | string | [Graph 🕸 domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/40 🕸 Graphs/$ 🕸🛠️ Graph helper.md>) name
|       | `Subject` | string | `Translate@Graph`
|Body   | `Domains`     | string[]  | The [domains 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) to translate
|       | `Codes`       | string[]  | The [Schema Codes 🧩](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) to translate
|

<br/>


## Synchronous Response

```yaml
Domains: 
  - Domain: example.com
    Translation: Example Airlines
Codes: 
  - Code: iata.org/SSR/WCHR
    Translation: Wheelchair assistance required
```

|Object|Property|Type|Description
|-|-|-|-
|Top    | `Domains`     | object[]  | List of [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) objects
|       | `Codes`       | object[]  | List of [Schema Code 🧩](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) objects
|Domain | `Domain`      | string    | The [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) name
|       | `Translation` | string    | The [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) title
|Code   | `Code`        | string    | The [Schema Code 🧩](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>)
|       | `Translation` | string    | The [Schema Code 🧩](<../../4 ⚙️ Solution/25 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) title
|

<br/>