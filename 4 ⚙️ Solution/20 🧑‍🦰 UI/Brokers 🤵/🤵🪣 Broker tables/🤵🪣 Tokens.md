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

Here's the [`MAP` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/MAP 🗺️ item.md>) result.

```yaml
# MAP|Tokens|any-issuer.dom,<token-uuid>
Issuer: any-issuer.dom
TokenID: <token-uuid>
WalletID: <wallet-uuid>
Path: /path/file
```