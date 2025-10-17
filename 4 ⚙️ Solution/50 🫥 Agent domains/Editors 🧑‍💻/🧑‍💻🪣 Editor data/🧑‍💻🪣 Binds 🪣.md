# 🪣 Binds

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).


```yaml
# Binds.yaml
Key: ID
Parents:
    Wallet: WalletID >> Wallets
    Vault: Vault >> Vaults
```

## Example

Here's the [`MAP` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/MAP 🗺️ item.md>) result.

```yaml
# MAP|Binds|<bind-id>
ID: <bind-id>
Vault: any-vault.dom
WalletID: <wallet-uuid>
Code: .BIND
```