<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDAacb56742c6a342a8a3494587d -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L316 -->

# 👥🚀🕸 Identity @ Graph

> Return the content of [`nlweb.org/MANIFEST/IDENTITY 🧩`](<../../{codes}/MANIFEST/🧩 ManifestIdentity.md>)

> Used by [🤵⏩🧑‍🦰 Assessed @ Broker](<../../5 ⏩ Flows/10 🤵⏩ Brokers/01 🤵⏩🧑‍🦰 Assessed.md>) 

> ⚠️ This method doesn’t look at the header nor the signature of the request.

<br/>

## Synchronous Request 🚀

```yaml
Header: 
    From: any-domain.com
    To: any-graph.com
    Subject: Identity@Graph
    
Body:
    Domain: another-domain.com
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) querying
|       | `To`      | string | [Graph 🕸 domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) name
|       | `Subject` | string | `Identity@Graph`
| Body  | `Domain`  | string | The name of another [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) to look up
|

<br/>

## Synchronous Response 


```yaml
Domain: another-domain.com
Feedback: any-buffer.com
Name: Any Other Domain, Inc.
SmallIcon: 
BigIcon: https://another-domain.com/big-icon.png
Translations: 
  - Language: en-us
    Translation: Any Other Domain, Inc.
```

|Object|Property|Type|Description
|-|-|-|-
|Top        |`Domain`       | string | URL name of the [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>)
|           |`Feedback`     | string | [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) name
|           |`Name`         | string | Friendly name of the [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>)
|           |`SmallIcon`    | URL    | Location of the small icon
|           |`BigIcon`      | URL    | Location of the big icon
|           |`Translations` | object[]| List of Translation objects
|Translation|`Language`     | enum   | ISO language code
|           |`Translation`  | string | Translated text
|
