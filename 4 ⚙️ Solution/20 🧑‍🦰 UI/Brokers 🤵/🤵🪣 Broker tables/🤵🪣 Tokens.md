# 🪣 Tokens

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).

```yaml
# Tokens.yaml
Key: Issuer, TokenID
Parents:
    Wallet: WalletID >> Wallets
    Issuer: Issuer >> Issuers
```

## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET 🗺️ item.md>) result.

```yaml
# GET|Tokens|any-issuer.dom,<token-uuid>
Issuer: any-issuer.dom
TokenID: <token-uuid>
WalletID: <wallet-uuid>
Path: /path/file
```