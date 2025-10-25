# 🤵🪣 Tokens @ Broker table

> Purpose:
* Stores [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
    * initially stored in [`Offers` 🪣 table](<../Offers 🎫 table/🤵🪣 Offers table.md>)
    * by the [`Offer@Broker`](<../../🤵🅰️ Broker methods/...for Tokens 🎫/Offer 🎴🐌🤵/Offer 🐌 msg.md>) method
    * then later saved by the [`Saved@Broker`](<../../🤵🅰️ Broker methods/...for Tokens 🎫/Saved 🧑‍🦰🐌🤵/Saved 🐌 msg.md>) method

> Read by: 
* [`Tokens@Broker` 🅰️](<../../🤵🅰️ Broker methods/...for Tokens 🎫/Tokens 🧑‍🦰🚀🤵/Tokens 🚀 request.md>) method

> Written by:
* [`Saved@Broker`](<../../🤵🅰️ Broker methods/...for Tokens 🎫/Saved 🧑‍🦰🐌🤵/Saved 🐌 msg.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Tokens.yaml
Table: Tokens
Key: Token
Parents:
    Wallet: { Wallets.Wallet: Tokens.Wallet }
    Issuer: { Domains.Domain: Tokens.Issuer }
```


| Link | Table | Stores
|-|-|-
| Parent    | [`Wallets` 🪣](<../Wallets 🧑‍🦰 table/🤵🪣 Wallets table.md>) | [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) |
|           | [`Domains` 🪣](<../Domains table/🤵🪣 Domains table.md>) | [domains 👥](<../../../../40 👥 Domains/👥 Domain.md>)
|

<br/>

## Example

Here's the [`GET` command](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) result.


```yaml
# GET|Tokens|<token-uuid>
Token: <token-uuid>
Wallet: <wallet-uuid>
Issuer: any-issuer.dom
Issuer$: Any Issuer
Key: <any-key>
Path: /storage/nlweb/tokens/any-issuer.dom/<token-uuid>
Schema: any-authority.dom/ANY-SCHEMA:1.0
Status: REVOKED
```


|Property|Type|Description
|-|-|-
| `Issuer` | string | [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)  from [`Offer@Broker`](<../../🤵🅰️ Broker methods/...for Tokens 🎫/Offer 🎴🐌🤵/Offer 🐌 msg.md>)
| `Path` | string | Path from [`Saved@Broker`](<../../🤵🅰️ Broker methods/...for Tokens 🎫/Saved 🧑‍🦰🐌🤵/Saved 🐌 msg.md>)
| `Status`| string | Status from [`Revise@Broker`](<../../🤵🅰️ Broker methods/...for Tokens 🎫/Revise 🎴🐌🤵/Revise 🐌 msg.md>)
| `Token`| uuid |  [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) from [`Offer@Broker`](<../../🤵🅰️ Broker methods/...for Tokens 🎫/Offer 🎴🐌🤵/Offer 🐌 msg.md>)
||