# 🪣 Tokens

> Stores [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).

```yaml
# Tokens.yaml
Key: Issuer, Token
Parents:
    Wallet: Wallets|Wallet
    Issuer: Issuers|Issuer
```


| Link | Table | Stores
|-|-|-
| Parent    | [`Wallets` 🪣](<🤵🪣 Wallets.md>) | [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
|           | [`Issuers` 🪣](<🤵🪣 Issuers.md>) | [Issuer 🎴 domains](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)
|


## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET 🗺️ item.md>) result.

```yaml
# GET|Tokens|any-issuer.dom,<token-uuid>
Issuer: any-issuer.dom
Token: <token-uuid>
Wallet: <wallet-uuid>
Path: /path/file
```