# 🤵🪣 Tokens @ Broker table

> Implementation
* Implements the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Purpose
* Stores [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)

> Data access
* Read by [`Tokens@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Tokens 🧑‍🦰🚀🤵/🤵 Tokens 🚀 request.md>) 
* Written by [`Offer@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) [`Saved@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>) [`Revise@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>)

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

Views:
    Offered: 
        - Status: OFFERED
    Active: 
        - .Now.In(Starts, Expires)
        - Status: ACTIVE
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
Starts: 2018-12-10T13:45:00.000Z
Expires: 2018-12-10T13:45:00.000Z
```


|Property|Type|Description | Origin
|-|-|-|-
| `ID`| uuid |  [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) | [`Offer` 📃 handler](<../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 📃 handler.md>)
| `Wallet` | uuid | [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) | [`Offer` 📃 handler](<../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 📃 handler.md>)
| `Issuer` | string | [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>)  | [`Offer@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
| `Issuer$` | string | [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) Title | [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| `Key` | string | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) Key |  [`Offer@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
| `Schema` | string | [Schema Code 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`Offer@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
| `Starts` | time | Valid from | [`Offer@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
| `Expires` | time | Valid until | [`Offer@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
| `Status`| string | `OFFERED` <br/> `ACTIVE` <br/> `SUSPENDED` <br/> `REVOKED` | [`Revise@Broker`](<../../🤵🅰️ Broker methods/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>)
||