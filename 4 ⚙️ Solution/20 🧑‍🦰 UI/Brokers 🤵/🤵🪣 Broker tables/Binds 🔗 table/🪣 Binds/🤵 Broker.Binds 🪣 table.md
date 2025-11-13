# 🤵🪣 Binds @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Stores [Binds 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
# Binds.yaml
Prefix: Broker
Table: Binds
Key: ID

Parents:
    Wallet: { Wallets.ID: Binds.Wallet }
    Vault: { Domains.Name: Binds.Vault }

Triggers:
    OnBindChanges: ADDED, CHANGED, DELETED
```

## Links

| Link | Table | Contains
|-|-|-
| Parent    | [`Wallets` 🪣](<../../Wallets 🧑‍🦰 table/🤵 Broker.Wallets 🪣 table.md>) | [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|| [`Domains` 🪣](<../../Domains 👥 table/🤵 Broker.Domains 🪣 table.md>) | [domains 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)


## Triggers



## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|Binds@Broker|<bind-id>
ID: <bind-id>
Vault: any-vault.dom
Wallet: <wallet-uuid>
Schema: any-authority.dom/ANY-SCHEMA:1.0
```