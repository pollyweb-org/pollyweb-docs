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

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET 🗺️ item.md>) result.

```yaml
# GET|Binds|<bind-id>
ID: <bind-id>
Vault: any-vault.dom
Wallet: <wallet-uuid>
Code: .BIND
```