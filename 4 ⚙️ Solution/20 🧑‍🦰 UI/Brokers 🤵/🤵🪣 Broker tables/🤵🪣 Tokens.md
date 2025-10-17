# 🪣 Tokens

## Schema

Here's the [Tables 🪣 folder file](<../../../55 👷 Build domains/Hosteds 📦/📦📄 Hosted files/🪣📂 Tables folder.md>).

```yaml
# Tokens.yaml
Key: Issuer, TokenID
Parents:
    Wallet: WalletID >> Wallets
    Issuer: Issuer >> Issuers
```

## Example

Here's the [`MAP` command](<../../../35 💬 Chats/😃 Talkers/😃💾 Talker data/MAP 🪣 item.md>) result.

```yaml
# MAP|Tokens|any-issuer.dom,<token-uuid>
Issuer: any-issuer.dom
TokenID: <token-uuid>
WalletID: <wallet-uuid>
Path: /path/file
```