<!-- #TODO -->

<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDA71b470c7a4c446e5b43adea7e -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L279 -->

# 👥🚀🕸 Trusts @ [Graph](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>)


## Used by

| Caller | Notes
|-|-
||

<br/>

## Synchronous Request 🚀


```yaml
Header: 
    From: any-domain.com
    To: any-graph.com
    Subject: Trusted@Graph

Body:
    Truster: any-vault.com
    Trusted: any-consumer.com
    Role: CONSUMER
    Code: any-authority.org/CODE/SUBCODE
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the sender domain
|       | `To`      | string | [Graph 🕸 domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) name
|       | `Subject` | string | `Trusts@Graph`
| Body  | `Truster` | string | The name of the domain trusting.
|       | `Trusted` | string | The name of the domain to be trusted.
|       | `Role`    | enum   | The role to assess: `VAULT`, `CONSUMER`, `*`
|       | `Code`    | string | The Schema Code to assess.

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


<br/>