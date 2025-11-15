# 👥🚀🕸 Identity @ Graph

> Part of [Graph 🕸 domain](<../../🕸 Graph/🕸🤲 Graph helper.md>)

> Purpose

* Given a domain, 
    * returns the content of [`.MANIFEST/ABOUT 🧩`](<../../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 ABOUT.md>)
    * from its [domain Manifest 📜](<../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) 

> Used by
* [🤵⏩🧑‍🦰 Open 💬 flow](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵⏩ Broker flows/Open 🤵⏩💬/🤵 Open ⏩ flow.md>) 


## Synchronous Call 🚀

```yaml
Header: 
    From: any-domain.dom
    To: any-graph.dom
    Subject: Domain@Graph
    
Body:
    Domain: another-domain.dom
```

|Object|Property|Type|Description
|-|-|-|-
| Header|`From`|string| The name of the [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) querying
|       |`To`|string| [Graph 🕸 domain](<../../🕸 Graph/🕸🤲 Graph helper.md>) name
|       | `Subject` | string | `Domain@Graph`
| Body  | `Domain`  | string | The name of another [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) to look up




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
|Top        |`Domain`       | string | URL name of the [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|           |`Feedback`     | string | [Buffer ⏳ helper domain](<../../../Buffers ⏳/⏳🤲 Buffer helper.md>) name
|           |`Title`         | string | Friendly name of the [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|           |`SmallIcon`    | string  | Small icon in Base64 PNG
|           |`BigIcon`      | string  | Big icon in Base64 PNG
