<!-- #TODO -->

<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDAacb56742c6a342a8a3494587d -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L316 -->

# 👥🚀🕸 Identity @ Graph


## Used by 

| Caller | Notes
|-|-
| [🤵⏩🧑‍🦰 Assessed @ Broker](<../../5 ⏩ Flows/08 🤵⏩ Brokers/01 🤵⏩🧑‍🦰 Assessed.md>) | 
||

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
| Header| `From`    | string | The name of the domain querying.
|       | `To`      | string | [Graph 🕸 domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) name
|       | `Subject` | string | `Identity@Graph`
| Body  | `Domain`  | string | The name of another domain to look up.
|

<br/>

## Synchronous Response 


```yaml
Domain: another-domain.com
Name: Any Other Domain, Inc.
SmallIcon: 
BigIcon: https://another-domain.com/big-icon.png
Translations: 
  - Language: en-us
    Translation: Any Other Domain, Inc.
```

|Object|Property|Type|Description
|-|-|-|-
|Top|`Domain`   | string | URL name of the domain.
||`Name`     | string | Friendly name of the domain.
||`SmallIcon`| URL    | Location of the icon.
||`BigIcon`  | URL    | Location of the icon.
||`Translations`| list | List of Translation objects
|Translation|`Language`| enum | ISO language code
|           |`Translation`| string | Translated text
|
