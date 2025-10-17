# 🪣 Binds

## Schema

Here's the [Tables 🪣 folder file](<../../../55 👷 Build domains/Hosteds 📦/📦📄 Hosted files/🪣📂 Tables folder.md>).


```yaml
# Binds.yaml
Key: ID
Parents:
    Wallet: WalletID >> Wallets
    Vault: Vault >> Vaults
```

## Example

Here's the [`MAP` command](<../../../35 💬 Chats/😃 Talkers/😃💾 Talker data/MAP 🗺️ item.md>) result.

```yaml
# MAP|Binds|<bind-id>
ID: <bind-id>
Vault: any-vault.dom
WalletID: <wallet-uuid>
Code: .BIND
```