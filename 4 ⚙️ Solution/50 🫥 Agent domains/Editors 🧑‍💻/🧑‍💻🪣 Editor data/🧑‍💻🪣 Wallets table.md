# 🪣 Wallets

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Wallets.yaml
Key: ID
Children:
    Tokens: Wallet
    Issuers: Tokens.Issuer
    Binds: Wallet
    Vaults: Binds.Vaults
```

## Example

Here's the [`GET` command](<../../../35 💬 Chats/Scripts 📃/📃 for datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) result.

```yaml
# GET|Wallets|<wallet-uuid>
ID: <wallet-uuid>
PublicKey: <public-key>
Notifier: any-notifier.dom
```