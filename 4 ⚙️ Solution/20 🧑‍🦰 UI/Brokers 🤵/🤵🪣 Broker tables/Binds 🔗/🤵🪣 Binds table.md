# 🤵🪣 Binds @ Broker table

> Stores [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
# Binds.yaml
Table: Binds
Key: Bind
Parents:
    Wallet: { Wallets.Wallet: Binds.Wallet }
    Vault: { Domains.Domain: Binds.Vault }
```


| Link | Table | Contains
|-|-|-
| Parent    | [`Wallets` 🪣](<../Wallets/🤵🪣 Wallets table.md>) | [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
|| [`Domains` 🪣](<../Domains/🤵🪣 Domains table.md>) | 
|

<br/>

## Example

Here's the [`GET` command](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) result.

```yaml
# GET|Binds@Broker|<bind-id>
Bind: <bind-id>
Vault: any-vault.dom
Wallet: <wallet-uuid>
Schema: any-authority.dom/ANY-SCHEMA:1.0
```