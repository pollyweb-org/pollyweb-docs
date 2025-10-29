<!-- https://quip.com/hgz4A3clvOes#temp:C:bDA44399e7e0bfc4609a560d6c4a -->
<!-- Source: https://github.com/jorgemjfonseca/domain-trust-framework/blob/a60df25a0f652b24793d9d0a3099aaa19bbcdd61/python/backbone/graph/GRAPH.py#L130 -->

# 👥🚀🕸 Queryable @ Graph

> Part of [Graph 🕸 domain](<../🕸🤲 Graph helper.md>)

> ⚠️ This method doesn’t look at the header nor the signature of the request.

* From the given list of and domain-and-code pairs, 
  * returns only the ones that can answer the given query;
  * i.e., that there’s a trust path that allows for the first to query the others, 
  * and a trust path that allows the others to provide a response to a query.
* Used by:
  * [🧑‍🦰👉💼 Share Bind 🔗 flow](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Bind 👉🔗💼/👉💼 Share Bind 🔗.md>) 

<br/> 

## Synchronous Request 🚀

```yaml
Header:
    From: any-domain.dom
    To: any-graph.dom
    Subject: Queryable@Graph

Body: 
    Consumer: any-consumer.dom
    Binds: 
      - Vault: ec.europa.eu
        Schema: airlines.any-igo.dom/SSR/WCHR/CRED
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the [domain 👥](<../../../40 👥 Domains/👥 Domain.md>) asking
|       | `To`      | string | [Graph 🕸 domain](<../🕸🤲 Graph helper.md>) name
|       | `Subject` | string | `Queryable@Graph`
| Body  | `Consumer`| string | [Consumer 💼 domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) name
|       | `Binds`   | object[]   | List of [Bind 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) objects
| Bind  | `Vault`   | string | The [Vault 🗄️ domain](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) name to assess
|       | `Schema`    | string | The [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) to assess
|

<br/>


## Synchronous Response

```yaml
Binds: 
  - Vault: ec.europa.eu
    Schema: airlines.any-igo.dom/SSR/WCHR/CRED
    Paths: 
      - [<vault>, <consumer>]
```

|Object|Property|Type|Description
|-|-|-|-
|Top    | `Binds`   | list      | List of queryable [Binds 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
|Bind   | `Vault`   | string    | Queryable [Vault 🗄️ domain](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) name
|       | `Schema`    | string    | Queryable [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|       | `Paths`   | string[][]| The chain of [Trusts 🫡](<../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>)
|

<br/>

