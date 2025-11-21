# 👥🚀🕸 Domain @ Graph

> Implementation
* Part of [Graph 🕸 domain](<../../🕸 Graph/🕸🤲 Graph helper.md>)
* Implemented by the [`Domain` 📃 handler](<🕸 About 📃 handler.md>)

> Purpose

* Given a domain, 
    * returns the content of [`.MANIFEST/ABOUT 🧩`](<../../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 ABOUT.md>)
    * from its [domain Manifest 📜](<../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) 



## Synchronous Call 🚀

```yaml
Header: 
    From: any-domain.dom
    To: any-graph.dom
    Subject: About@Graph
    
Body:
    Domain: another-domain.dom
    Language: pt-br
```

|Object|Property|Type|Description
|-|-|-|-
| Header|`From`|text| The name of the [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) querying
|       |`To`|text| [Graph 🕸 domain](<../../🕸 Graph/🕸🤲 Graph helper.md>) name
|       | `Subject` |text| `About@Graph`
| Body  | `Domain`  |text| The name of another [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) to look up
|       | `Language`|text| Language to translate, defaults to `en-us`
|


## Synchronous Response 


```yaml
Title: Any Other Domain, Inc.
Description: bla bla...
SmallIcon: <base64>
BigIcon: <base64>
```

||Property|Type|Description
|-|-|-|-
|           |`Title`         |text| Friendly name of the [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|           |`Description`   | string  | Description of the [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|           |`SmallIcon`    | string  | Small icon in Base64 PNG
|           |`BigIcon`      | string  | Big icon in Base64 PNG
|