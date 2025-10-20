# 🤵🪣 Tokens

> Stores [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).

```yaml
# Tokens.yaml
Name: Tokens
Key: Token
Parents:
    Wallet: { Wallets.Wallet: Tokens.Wallet }
    Issuer: { Issuers.Issuer: Tokens.Issuer }
```


| Link | Table | Stores
|-|-|-
| Parent    | [`Wallets` 🪣](<🤵🪣 Wallets.md>) | [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
|

<br/>

## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) result.


|Property|Type|Description
|-|-|-
| `Issuer` | string | [Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)
| `Token`| uuid | [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) ID on the [Broker 🤵](<../🤵🤲 Broker helper.md>)

```yaml
# GET|Tokens|<token-uuid>
Issuer: any-issuer.dom
Key: <any-key>
Path: /storage/nlweb/tokens/any-issuer.dom/<token-uuid>
Schema: any-authority.dom/ANY-SCHEMA:1.0
Status: REVOKED
Token: <token-uuid>
Wallet: <wallet-uuid>
```