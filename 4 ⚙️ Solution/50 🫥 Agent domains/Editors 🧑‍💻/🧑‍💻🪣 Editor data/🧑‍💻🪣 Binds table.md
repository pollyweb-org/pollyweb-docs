# 🪣 Binds

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
# Binds.yaml
Key: Bind
Parents:
    Wallet: Wallet >> Wallets
    Vault: Vault >> Vaults
```

## Example

Here's the [`READ` command](<../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|Binds|<bind-id>
Bind: <bind-id>
Vault: any-vault.dom
Wallet: <wallet-uuid>
Schema: .BIND
```