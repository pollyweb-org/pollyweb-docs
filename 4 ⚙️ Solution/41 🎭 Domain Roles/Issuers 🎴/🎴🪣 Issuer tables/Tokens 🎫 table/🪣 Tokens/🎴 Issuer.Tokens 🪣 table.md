# 🪣 Tokens

> Purpose
* Stores [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) issued by an [Issuer 🎴 domain](<../../../🎴 Issuer/🎴🎭 Issuer role.md>).
* Mirrors the [`Broker.Tokens` 🪣 table](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>) on [Broker 🤵 domains](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>).

<br/>


## Insert Diagram

![alt text](<../🪣⏩ Issued flow/🎴 Issuer.Tokens.Issued ⚙️ uml.png>)

<br/>


## Updates Diagram

![alt text](<../🪣⏩ Revised flow/🎴 Issuer.Tokens.Revised ⚙️ uml.png>)

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
        - Expires.IsEmpty.Or.IsFuture
```
Uses: [`.Is`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>) [`.IsEmpty`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsEmpty ⓕ.md>) [`.IsFuture`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsFuture ⓕ.md>) [`.Or`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Or ⓕ.md>)

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
| `Token`| uuid | From [`Offered@Issuer`](<../../../🎴📨 Issuer msgs/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>) 
| `User` | any | Internal anchor
| `Broker` |text| From [`Offered@Issuer`](<../../../🎴📨 Issuer msgs/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>) 
| `Schema` |text| From [`Issued@Issuer`](<../../../🎴📨 Issuer msgs/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 call.md>)
| 
