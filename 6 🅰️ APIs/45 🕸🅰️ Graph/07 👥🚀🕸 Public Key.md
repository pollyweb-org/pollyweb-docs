<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDAe17e4b66e30846a7b82ecce0c -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L171 -->

# 👥🚀🕸 Public Key @ Graph


> ⚠️ This method doesn’t look at the header nor the signature of the request.

* Returns the historical public key of an [Issuer 🎴 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/40 🎴 Issuers/$ 🎴🎭 Issuer role.md>) by the name of the key.
    * Allows a [Consumer 💼 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) to verify a [Token 🎫](<../../4 ⚙️ Solution/25 Data/25 🎫 Tokens/$ 🎫 Token.md>) issued before a [DKIM 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>) rotation.
* Used by:
    * [👥🔏 Domain Signature](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/05 👥🔏 Domain Signature.md>)
    * [💼⏩🧑‍🦰 Share Token @ Consumer](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token 🎫.md>) flow

<br/>

## Synchronous Request 🚀


```yaml
Header: 
    From: any-domain.com
    To: any-graph.com
    Subject: PublicKey@Graph

Body:
    Issuer: any-issuer.com
    DKIM: pk1
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) asking
|       | `To`      | string | [Graph 🕸 domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/40 🕸 Graphs/$ 🕸🛠️ Graph helper.md>) name
|       | `Subject` | string | `PublicKey@Graph`
|Body   | `Issuer`  | string | [Issuer 🎴 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/40 🎴 Issuers/$ 🎴🎭 Issuer role.md>) name
|       | `DKIM`| string | [DKIM 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>) name
|

<br/>

## Synchronous Response

```yaml
Algorithm: RSA
PublicKey: MIIBIjANBgkqhkiG9w0BAQEFAA...
```

|Property|Type|Description
|-|-|-
| `Algorithm` | string | [DKIM 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>) algorithm used in the period
| `PublicKey` | string | [DKIM 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>) public key in the period
|