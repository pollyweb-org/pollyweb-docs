<!-- #TODO -->

<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDAe17e4b66e30846a7b82ecce0c -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L171 -->

# 👥🚀🕸 Public Key @ Graph

> Returns the historical public key of an [Issuer 🎴 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) in a given date.
> <br/> Allows a [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) to verify a [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) issued before a [DKIM 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) rotation.

> ⚠️ To avoid cache-hits, [Issuer 🎴 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) must upgrade the version of their [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) when rotating their [DKIM 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) public key - this allows [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) signed with deprecated public keys to continue working until expired.

> ⚠️ This method doesn’t look at the header nor the signature of the request.

<br/>

## Synchronous Request 🚀


```yaml
Header: 
    From: any-domain.com
    To: any-graph.com
    Subject: PublicKey@Graph

Body:
    Issuer: any-issuer.com
    Timestamp: 2023-04-01T05:00:30.001000Z
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) asking
|       | `To`      | string | [Graph 🕸 domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) name
|       | `Subject` | string | `PublicKey@Graph`
|Body   | `Issuer`  | string | [Issuer 🎴 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) name
|       | `Timestamp`| timestamp | Issuing date of the [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
|

<br/>

## Synchronous Response

```yaml
From: 2022-01-09T01:42:36.000000Z
To: 9999-12-31T00:00:00.000000Z
Algorithm: RSA
PublicKey: MIIBIjANBgkqhkiG9w0BAQEFAA...
```

|Property|Type|Description
|-|-|-
| `From`    | timestamp | Start of matching period
| `To`      | timestamp | End of matching period
| `Algorithm` | string | [DKIM 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) algorithm used in the period
| `PublicKey` | string | [DKIM 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) public key in the period
|