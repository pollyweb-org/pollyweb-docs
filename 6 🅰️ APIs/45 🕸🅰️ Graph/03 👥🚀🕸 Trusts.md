
<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDA71b470c7a4c446e5b43adea7e -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L279 -->

# 👥🚀🕸 Trusts @ [Graph](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>)

> Verifies if there’s a path of [Trust 👍](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>) between two [domains 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) regarding a [Schema Code 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>).
> <br/> • Similar as [Trusted@Graph](<02 👥🚀🕸 Trusted.md>), but for verification by another [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).

> Used in:
> <br/> • [💼⏩🧑‍🦰 Share Token @ Consumer](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/03 🧑‍🦰👉💼 Share Token.md>)
> <br/> • [💼⏩🧑‍🦰 Query Vault @ Consumer](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind.md>)

> ⚠️ This method doesn’t look at the header nor the signature of the request.


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
| Header| `From`    | string | The name of the sender [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>)
|       | `To`      | string | [Graph 🕸 domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) name
|       | `Subject` | string | `Trusts@Graph`
| Body  | `Truster` | string | The name of the [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) trusting
|       | `Trusted` | string | The name of the [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) to be trusted
|       | `Role`    | enum   | The role to assess: `VAULT`, `CONSUMER`, `*`
|       | `Code`    | string | The [Schema Code 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) to assess
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
| `Trusted` | boolean       | [Trusted 👍](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>) or not
| `Paths`   | string[][]    | The chain of [Trusts 👍](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>)
|


<br/>