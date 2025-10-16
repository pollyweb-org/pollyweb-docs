# 🪣 Wallets

## Schema

Here's the [Tables 🪣 folder file](<../../../55 👷 Build domains/📦 Hosteds/📦📄 Hosted files/🪣📂 Tables folder.md>).

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

Here's the [`MAP` command](<../../../35 💬 Chats/😃 Talkers/😃💾 Talker data/61 🪣 MAP item.md>) result.

```yaml
# MAP|Wallets|<wallet-uuid>
ID: <wallet-uuid>
PublicKey: <public-key>
Notifier: any-notifier.dom
```