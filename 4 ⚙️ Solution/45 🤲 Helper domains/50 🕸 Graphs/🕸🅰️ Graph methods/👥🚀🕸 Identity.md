<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDAacb56742c6a342a8a3494587d -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L316 -->

# 👥🚀🕸 Identity @ Graph

> ⚠️ This method doesn’t look at the header nor the signature of the request.

* Given a domain, 
    * returns the content of [`.MANIFEST/ABOUT 🧩`](<../../../40 👥 Domains/44 📜 Manifests/🧩 Manifest schemas/🧩 ABOUT.md>)
    * from its [domain Manifest 📜](<../../../40 👥 Domains/44 📜 Manifests/📜 Manifest.md>) 
* Used by:
    * [🤵⏩🧑‍🦰 Converse 💬 flow](<../../../../5 ⏩ Flows/10 🤵⏩ Brokers/03 🤵⏩🧑‍🦰 Converse 💬.md>) 

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
| Header| `From`    | string | The name of the [domain 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>) querying
|       | `To`      | string | [Graph 🕸 domain](<../🕸🛠️ Graph helper.md>) name
|       | `Subject` | string | `Identity@Graph`
| Body  | `Domain`  | string | The name of another [domain 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>) to look up
|

<br/>

## Synchronous Response 


```yaml
Domain: another-domain.com
Feedback: any-buffer.com
Name: Any Other Domain, Inc.
SmallIcon: <base64>
BigIcon: <base64>
Translations: 
  - Language: en-us
    Translation: Any Other Domain, Inc.
```

|Object|Property|Type|Description
|-|-|-|-
|Top        |`Domain`       | string | URL name of the [domain 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>)
|           |`Feedback`     | string | [Buffer ⏳ helper domain](<../../27 ⏳ Buffers/⏳🤲 Buffer helper.md>) name
|           |`Name`         | string | Friendly name of the [domain 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>)
|           |`SmallIcon`    | string  | Small icon in Base64 PNG
|           |`BigIcon`      | string  | Big icon in Base64 PNG
|           |`Translations` | object[]| List of Translation objects
|Translation|`Language`     | enum   | ISO language code
|           |`Translation`  | string | Translated text
|
