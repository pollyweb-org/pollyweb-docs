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

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) result.

```yaml
# GET|Binds|<bind-id>
Bind: <bind-id>
Vault: any-vault.dom
Wallet: <wallet-uuid>
Schema: .BIND
```