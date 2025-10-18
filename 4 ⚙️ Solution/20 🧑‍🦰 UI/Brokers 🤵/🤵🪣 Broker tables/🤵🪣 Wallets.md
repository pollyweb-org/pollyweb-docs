# 🪣 Wallets

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).

```yaml
# Wallets.yaml
Key: Wallet
Children:
    Tokens: Tokens|Wallet
    Issuers: .Tokens|Issuers|Issuer
    Binds: Binds|Wallet
    Vaults: .Binds|Vaults|Vault
```

## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET 🗺️ item.md>) result.

```yaml
# GET|Wallets|<wallet-uuid>
Wallet: <wallet-uuid>
PublicKey: <public-key>
Notifier: any-notifier.dom
```