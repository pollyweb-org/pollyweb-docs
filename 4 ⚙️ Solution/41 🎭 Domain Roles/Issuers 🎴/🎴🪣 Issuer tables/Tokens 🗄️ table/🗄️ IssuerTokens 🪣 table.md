# 🪣 Tokens

> Stores the content of [`Accepted@Issuer`](<../../🎴🅰️ Issuer methods/Accepted 🤵🐌🎴/🎴 Accepted 🐌 msg.md>) 

<br/>

## Example

Here's the [`GET` command](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET ⏬/GET ⏬ item.md>) result.

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
| `Broker` | string | From [`Accepted@Issuer`](<../../🎴🅰️ Issuer methods/Accepted 🤵🐌🎴/🎴 Accepted 🐌 msg.md>) 
| `Token`| uuid | From [`Accepted@Issuer`](<../../🎴🅰️ Issuer methods/Accepted 🤵🐌🎴/🎴 Accepted 🐌 msg.md>) 
| `User` | any | Internal anchor
| `Schema` | string | From [`Issued@Issuer`](<../../🎴🅰️ Issuer methods/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 request.md>)
| 

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
# Tokens.yaml
Key: Broker, Token
```
