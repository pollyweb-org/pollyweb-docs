# 🪣 Wallets

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).

```yaml
# Wallets.yaml
Key: ID
Children:
    Tokens: WalletID
    Issuers: Tokens.Issuer
    Binds: WalletID
    Vaults: Binds.Vaults
```

## Example

Here's the [`MAP` command](<../../../35 💬 Chats/😃 Talkers/😃💾 Talker data/MAP 🗺️ item.md>) result.

```yaml
# MAP|Wallets|<wallet-uuid>
ID: <wallet-uuid>
PublicKey: <public-key>
Notifier: any-notifier.dom
```