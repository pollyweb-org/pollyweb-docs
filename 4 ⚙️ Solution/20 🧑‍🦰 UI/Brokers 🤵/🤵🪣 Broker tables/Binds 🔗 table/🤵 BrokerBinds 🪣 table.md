# 🤵🪣 Binds @ Broker table

> Implements the [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>)

> Stores [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
# Binds.yaml
Prefix: Broker
Table: Binds
Key: Bind
Parents:
    Wallet: { Wallets.Wallet: Binds.Wallet }
    Vault: { Domains.Domain: Binds.Vault }
```


| Link | Table | Contains
|-|-|-
| Parent    | [`Wallets` 🪣](<../Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>) | [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
|| [`Domains` 🪣](<../Domains 👥 table/🤵 BrokerDomains 🪣 table.md>) | 
|

<br/>

## Example

Here's the [`GET` command](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) result.

```yaml
# GET|Binds@Broker|<bind-id>
Bind: <bind-id>
Vault: any-vault.dom
Wallet: <wallet-uuid>
Schema: any-authority.dom/ANY-SCHEMA:1.0
```