<!-- https://quip.com/hgz4A3clvOes#temp:C:bDA44399e7e0bfc4609a560d6c4a -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/a60df25a0f652b24793d9d0a3099aaa19bbcdd61/python/backbone/graph/GRAPH.py#L130 -->

# 👥🚀🕸 Queryable @ Graph

> ⚠️ This method doesn’t look at the header nor the signature of the request.

* From the given list of and domain-and-code pairs, 
  * returns only the ones that can answer the given query;
  * i.e., that there’s a trust path that allows for the first to query the others, 
  * and a trust path that allows the others to provide a response to a query.
* Used by:
  * [🧑‍🦰👉💼 Share Bind 🔗 flow](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind 🔗.md>) 

<br/> 

## Synchronous Request 🚀

```yaml
Header:
    From: any-domain.com
    To: any-graph.com
    Subject: Queryable@Graph

Body: 
    Consumer: any-consumer.org
    Binds: 
      - Vault: ec.europa.eu
        Code: airlines.any-igo.org/SSR/WCHR/CRED
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) asking
|       | `To`      | string | [Graph 🕸 domain](<../../4 ⚙️ Solution/42 Backbone/20 🕸 Graphs/$ 🕸🛠️ Graph helper.md>) name
|       | `Subject` | string | `Queryable@Graph`
| Body  | `Consumer`| string | [Consumer 💼 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) name
|       | `Binds`   | object[]   | List of [Bind 🔗](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/01 🔗 Bind.md>) objects
| Bind  | `Vault`   | string | The [Vault 🗄️ domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vault/$ 🗄️🎭 Vault role.md>) name to assess
|       | `Code`    | string | The [Schema Code 🧩](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>) to assess
|

<br/>


## Synchronous Response

```yaml
Binds: 
  - Vault: ec.europa.eu
    Code: airlines.any-igo.org/SSR/WCHR/CRED
    Paths: 
      - [<vault>, <consumer>]
```

|Object|Property|Type|Description
|-|-|-|-
|Top    | `Binds`   | list      | List of queryable [Binds 🔗](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/01 🔗 Bind.md>)
|Bind   | `Vault`   | string    | Queryable [Vault 🗄️ domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vault/$ 🗄️🎭 Vault role.md>) name
|       | `Code`    | string    | Queryable [Schema Code 🧩](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>)
|       | `Paths`   | string[][]| The chain of [Trusts 👍](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>)
|

<br/>

