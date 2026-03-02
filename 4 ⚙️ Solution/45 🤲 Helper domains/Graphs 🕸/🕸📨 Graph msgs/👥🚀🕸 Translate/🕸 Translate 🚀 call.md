# 👥🚀🕸 Translate @ Graph


> Implementation
* Part of [Graph 🕸 domain](<../../🕸 Graph helper/🕸🤲 Graph helper.md>)

> Purpose
* [Broker 🤵 domains](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) 
    * request translation for [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) and [domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>),
    * obtained [domain Manifests 📜](<../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>).

> Used by
* [`Share Bind` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Bind 👉🔗💼/🧑‍🦰 Share Bind ⏩ flow.md>) 
* [`Share Token` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>) 


## Synchronous Call 🚀

```yaml
Header: 
    From: any-domain.dom
    To: any-graph.dom
    Subject: Translate@Graph

Body: 
    Language: pt-br

    # Translate domains
    Domain: any-domain.dom
    Domains: [any-domain.dom]
    
    # Translate schemas
    Schema: any-authority.dom/ANY/SCHEMA
    Schemas: [any-authority.dom/ANY/SCHEMA]

    # Translate text
    Text: 
        Any text to ´or not to´ translate, 
        including domain info
            like ´$Domain.Title´ 
            and ´$Domain.Description´,
        and schema info
            like ´$Schema.Title´ 
            and ´$Schema.Description´.
    
    # Text original language
    Source: en-us
```

|Object|Property|Type|Description
|-|-|-|-
| Header|`From`|text| Requester [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name
|       |`To`|text| [Graph 🕸 domain](<../../🕸 Graph helper/🕸🤲 Graph helper.md>) name
|       | `Subject` |text| `Translate@Graph`
|Body   | `Language`|text| Target language
|| `Domain`     | string  | [Domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) to translate
|| or `Domains`     | string[]  | [Domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) to translate
|| `Schema`       | string  | [Schema Code 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) to translate
|| or `Schemas`       | string[]  | [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) to translate
||`Text`|text| Free text to translate
||`Source`|text| Original text language
|

<br/>


## Synchronous Response

If the request contains `Domain` and `Language`.
```yaml
Domain: 
    Title: Any Domain       # in the target language
    Description: Bla...     # in the target language
```

If the request contains `Domains` and `Language`.
```yaml
Domains: 
    any-domain.dom:         # Identifier domain name
        Title: Any Domain   # in the target language
        Description: Bla... # in the target language
```

If the request contains `Schema` and `Language`.
```yaml
Schema: 
    Title: Any Schema       # in the target language
    Description: Bla...     # in the target language
```

If the request contains `Schemas`.
```yaml
Schemas: 
    any.dom/ANY/SCHEMA:     # Schema code
        Title: Any Schema   # in the target language
        Description: Bla... # in the target language
```

If the request contains `Text`, `Source`, and `Language`.
```yaml
Text: Bla...
```

---
<br/>