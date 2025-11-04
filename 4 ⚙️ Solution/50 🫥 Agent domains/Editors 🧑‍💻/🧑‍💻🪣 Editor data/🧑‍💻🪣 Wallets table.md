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

Here's the [`READ` command](<../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|Wallets|<wallet-uuid>
ID: <wallet-uuid>
PublicKey: <public-key>
Notifier: any-notifier.dom
```