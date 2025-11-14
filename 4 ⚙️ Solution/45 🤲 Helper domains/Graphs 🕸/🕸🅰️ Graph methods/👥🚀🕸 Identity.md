<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDAacb56742c6a342a8a3494587d -->
<!-- Source: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L316 -->

# 👥🚀🕸 Identity @ Graph

> Part of [Graph 🕸 domain](<../🕸🤲 Graph helper.md>)

> ⚠️ This method doesn’t look at the header nor the signature of the request.

* Given a domain, 
    * returns the content of [`.MANIFEST/ABOUT 🧩`](<../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 ABOUT.md>)
    * from its [domain Manifest 📜](<../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) 
* Used by:
    * [🤵⏩🧑‍🦰 Converse 💬 flow](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵⏩ Broker flows/Open 🤵⏩💬/🤵 Open ⏩ flow.md>) 

<br/>

## Synchronous Request 🚀

```yaml
Header: 
    From: any-domain.dom
    To: any-graph.dom
    Subject: Identity@Graph
    
Body:
    Domain: another-domain.dom
```

|Object|Property|Type|Description
|-|-|-|-
| Header|`From`|domain| The name of the [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) querying
|       |`To`|domain| [Graph 🕸 domain](<../🕸🤲 Graph helper.md>) name
|       | `Subject` | string | `Identity@Graph`
| Body  | `Domain`  | string | The name of another [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) to look up
|

<br/>

## Synchronous Response 


```yaml
Domain: another-domain.dom
Feedback: any-buffer.dom
Title: Any Other Domain, Inc.
Description: bla bla...
SmallIcon: <base64>
BigIcon: <base64>
```

|Object|Property|Type|Description
|-|-|-|-
|Top        |`Domain`       | string | URL name of the [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|           |`Feedback`     | string | [Buffer ⏳ helper domain](<../../Buffers ⏳/⏳🤲 Buffer helper.md>) name
|           |`Title`         | string | Friendly name of the [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|           |`SmallIcon`    | string  | Small icon in Base64 PNG
|           |`BigIcon`      | string  | Big icon in Base64 PNG
|
