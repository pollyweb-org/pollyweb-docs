# 🪣 Tokens

> Stores the content of [`Accepted@Issuer`](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/🤵🐌🎴 Accepted.md>) 

<br/>

## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET ⏬ item.md>) result.

```yaml
# GET|Tokens|<broker>,<token>
Broker: any-broker.dom
Token: <token-uuid>
User: <internal-reference>
Schema: airlines.any-igo.dom/SSR/WCH:1 
...
```

| Property | Type | Details
|-|-|-
| `Broker` | string | From [`Accepted@Issuer`](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/🤵🐌🎴 Accepted.md>) 
| `Token`| uuid | From [`Accepted@Issuer`](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/🤵🐌🎴 Accepted.md>) 
| `User` | any | Internal anchor
| `Schema` | string | From [`Issued@Issuer`](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/🧑‍🦰🚀🎴 Issued.md>)
| 

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
# Tokens.yaml
Key: Broker, Token
```
