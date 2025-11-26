# 🪣 Tokens

> Purpose
* Stores [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) issued by an [Issuer 🎴 domain](<../../../🎴 Issuer/🎴🎭 Issuer role.md>).
* Mirrors the [`Broker.Tokens` 🪣 table](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>) on [Broker 🤵 domains](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>).

<br/>


## Insert Diagram

![alt text](<🎴 Issuer.Tokens.Insert ⚙️ uml.png>)

<br/>


## Updates Diagram

![alt text](<🎴 Issuer.Tokens.Updates ⚙️ uml.png>)

<br/>


## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
Table: Tokens
Item: Token

Views:
    ACTIVE: # Just for reference, not used
        - .State.Is(OFFERED)
        - Status.Is(ACTIVE)
        - Expires.IsFutureOrEmpty
```
Uses: [`.Is`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>) {{.IsFutureOrEmpty}}

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# Automatic
ID: <token-uuid>

# From the ISSUE command
User: <internal-reference>
Broker: any-broker.dom
Schema: airlines.any-igo.dom/SSR/WCH:1 
...
```

| Property | Type | Details
|-|-|-
| `Token`| uuid | From [`Offered@Issuer`](<../../../🎴🅰️ Issuer methods/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>) 
| `User` | any | Internal anchor
| `Broker` |text| From [`Offered@Issuer`](<../../../🎴🅰️ Issuer methods/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>) 
| `Schema` |text| From [`Issued@Issuer`](<../../../🎴🅰️ Issuer methods/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 call.md>)
| 
