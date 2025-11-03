# 🤵🪣 Tokens @ Broker table

> Implements the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)


> Purpose
* Stores [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
    * initially stored in [`Offers` 🪣 table](<../Offers 🎫 table/🤵 BrokerOffers 🪣 table.md>)
    * by the [`Offer@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) method
    * then later saved by the [`Saved@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>) method

> Read by
* [`Tokens@Broker` 🅰️](<../../🤵🅰️ Broker methods/Tokens 🎫 Tokens 🧑‍🦰🚀🤵/🤵 Tokens 🚀 request.md>) method

> Written by
* [`Saved@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Tokens.yaml
Prefix: Broker
Table: Tokens
Key: ID
Parents:
    Wallet: { Wallets.ID: Tokens.Wallet }
    Issuer: { Domains.Name: Tokens.Issuer }
```


| Link | Table | Stores
|-|-|-
| Parent    | [`Wallets` 🪣](<../Wallets 🧑‍🦰 table/🤵 BrokerWallets 🪣 table.md>) | [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) |
|           | [`Domains` 🪣](<../Domains 👥 table/🤵 BrokerDomains 🪣 table.md>) | [domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|

<br/>

## Example

Here's the [`GET` command](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) result.


```yaml
# GET|Tokens|<token-uuid>
ID: <token-uuid>
Wallet: <wallet-uuid>
Issuer: any-issuer.dom
Issuer$: Any Issuer
Key: token-1234
Schema: any-authority.dom/ANY-SCHEMA:1.0
Status: REVOKED
```


|Property|Type|Description
|-|-|-
| `Issuer` | string | [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>)  from [`Offer@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
| `Status`| string | Status from [`Revise@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>)
| `ID`| uuid |  [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) from [`Offer@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
||