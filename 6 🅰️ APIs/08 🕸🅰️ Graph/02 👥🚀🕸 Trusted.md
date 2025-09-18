<!-- #TODO -->

<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDA0807933d618043e6b1873dc74 -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L255 -->

# 👥🚀🕸 Trusted @ Graph


## Used by

| Caller | Notes
|-|-
||

<br/>


## Synchronous Request 🚀


```yaml
Header: 
    From: any-consumer.com
    To: any-graph.com
    Subject: Trusted@Graph

Body:
    Domain: any-vault.com
    Role: VAULT
    Code: any-authority.org/CODE/SUBCODE
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the sender domain
|       | `To`      | string | [Graph 🕸 domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) name
|       | `Subject` | string | `Trusted@Graph`
| Body  | `Domain`  | string | The domain name to assess.
|       | `Role`    | enum   | The role to assess: `VAULT`, `CONSUMER`, `*`
|       | `Code`    | string | The Schema Code to assess.
|

<br/>


## Synchronous Response 


```yaml
Trusted: True
Paths:
  - [any-vault.com, any-authority.org]
  - [any-authority.org, any-consumer.com]
```

|Property|Type|Description
|-|-|-
| `Trusted` | boolean       | Trusted or not.
| `Paths`   | string[][]    | The chain of Trusts.
|

<br/>