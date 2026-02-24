# 👥🚀🕸 Public Key @ Graph

> Part of [Graph 🕸 domain](<../../🕸 Graph helper/🕸🤲 Graph helper.md>)


* Returns the historical public key of an [Issuer 🎴 domain](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) by the name of the key.
    * Allows a [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) to verify a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) issued before a [DKIM 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) rotation.
* Used by:
    * [👥🔏 Domain Signature](<../../../../40 👥 Domains/👥⏩ Domain flows/Sign Files 👥🔏📄/👥 Domain Signature ⏩ flow.md>)
    * [💼⏩🧑‍🦰 Share Token @ Consumer](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>) flow

<br/>

## Synchronous Call 🚀


```yaml
Header: 
    From: any-domain.dom
    To: any-graph.dom
    Subject: PublicKey@Graph

Body:
    Domain: any-issuer.dom
    DKIM: pk1
```

|Object|Property|Type|Description
|-|-|-|-
| Header|`From`|text| The name of the [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) asking
|       |`To`|text| [Graph 🕸 domain](<../../🕸 Graph helper/🕸🤲 Graph helper.md>) name
|       | `Subject` |text| `PublicKey@Graph`
|Body   | `Domain`  |text| [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name
|       | `DKIM`|text| [DKIM 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) name
|

<br/>

## Synchronous Response

```yaml
Algorithm: RSA
PublicKey: MIIBIjANBgkqhkiG9w0BAQEFAA...
```

|Property|Type|Description
|-|-|-
| `Algorithm` |text| [DKIM 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) algorithm used in the period
| `PublicKey` |text| [DKIM 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) public key in the period
|