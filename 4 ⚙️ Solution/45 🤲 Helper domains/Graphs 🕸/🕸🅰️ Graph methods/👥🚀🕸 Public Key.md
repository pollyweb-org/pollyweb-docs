<!-- Docs: https://quip.com/hgz4A3clvOes#temp:C:bDAe17e4b66e30846a7b82ecce0c -->
<!-- Source: https://github.com/jorgemjfonseca/domain-trust-framework/blob/9a3c5abe16dda8cbacd2529bc859fd9d708f85d9/python/backbone/graph/GRAPH.py#L171 -->

# 👥🚀🕸 Public Key @ Graph

> Part of [Graph 🕸 domain](<../🕸🤲 Graph helper.md>)

> ⚠️ This method doesn’t look at the header nor the signature of the request.

* Returns the historical public key of an [Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) by the name of the key.
    * Allows a [Consumer 💼 domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) to verify a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) issued before a [DKIM 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) rotation.
* Used by:
    * [👥🔏 Domain Signature](<../../../40 👥 Domains/👥⏩ Domain flows/👥⏩📄 Sign files 🔏.md>)
    * [💼⏩🧑‍🦰 Share Token @ Consumer](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉💼 Share Token 🎫.md>) flow

<br/>

## Synchronous Request 🚀


```yaml
Header: 
    From: any-domain.dom
    To: any-graph.dom
    Subject: PublicKey@Graph

Body:
    Issuer: any-issuer.dom
    DKIM: pk1
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | The name of the [domain 👥](<../../../40 👥 Domains/👥 Domain.md>) asking
|       | `To`      | string | [Graph 🕸 domain](<../🕸🤲 Graph helper.md>) name
|       | `Subject` | string | `PublicKey@Graph`
|Body   | `Issuer`  | string | [Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) name
|       | `DKIM`| string | [DKIM 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) name
|

<br/>

## Synchronous Response

```yaml
Algorithm: RSA
PublicKey: MIIBIjANBgkqhkiG9w0BAQEFAA...
```

|Property|Type|Description
|-|-|-
| `Algorithm` | string | [DKIM 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) algorithm used in the period
| `PublicKey` | string | [DKIM 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) public key in the period
|