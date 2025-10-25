# 🤵🪣 Offers

> Purpose: 
* Stores [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
    * offered by [`Offer@Broker`](<../🤵🅰️ Broker methods/5 ...for Tokens 🎫/🎴🐌🤵 Offer.md>) 
    * but not yet saved by [`Saved@Broker`](<../🤵🅰️ Broker methods/5 ...for Tokens 🎫/🧑‍🦰🐌🤵 Saved.md>).

> Written by:
* [`Offer@Broker`](<../🤵🅰️ Broker methods/5 ...for Tokens 🎫/🎴🐌🤵 Offer.md>)
* [`Saved@Broker`](<../🤵🅰️ Broker methods/5 ...for Tokens 🎫/🧑‍🦰🐌🤵 Saved.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Offers.yaml
Table: Offers
Key: Token
```


<br/>

## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) result.


```yaml
# GET|Tokens|<token-uuid>
Token: <token-uuid>
Wallet: <wallet-uuid>
Issuer: any-issuer.dom
Issuer$: Any Issuer
Key: <any-key>
Schema: any-authority.dom/ANY-SCHEMA:1.0
```


|Property|Type|Description
|-|-|-
| `Issuer` | string | [Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)
| `Token`| uuid | [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) ID on the [Broker 🤵](<../🤵🤲 Broker helper.md>)
