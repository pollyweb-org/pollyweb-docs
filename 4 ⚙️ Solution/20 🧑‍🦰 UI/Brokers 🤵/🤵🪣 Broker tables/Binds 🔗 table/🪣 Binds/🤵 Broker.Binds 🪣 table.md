# 🤵🪣 Binds @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Stores [Binds 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
# Binds.yaml
Prefix: Broker
Table: Binds
Key: Vault, Wallet, Schema

Parents:
    Wallet: { Wallets.ID: Binds.Wallet }
    Vault: { Domains.Name: Binds.Vault }

Propagate:
    - Vault

Handlers:

    OnBindAltered: 
        Events: ALTERED

    OnBindGiven:
        Events: INSERTED, UPDATED
        Assert: New.Hook

    OnBindRemoved: 
        Events: DELETED
```

## Links

| Link | Table | Contains
|-|-|-
| Parent    | [`Wallets` 🪣](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) | [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|| [`Domains` 🪣](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) | [domains 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)


## Handlers

| Handler | [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | Events
|-|-|-
| [`OnBindChanges` 📃](<../🪣🔔 0 Altered/🤵 OnBindAltered 📃 handler.md>) | [`Update@Notifier` 🅰️](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>) | `ALTERED`


## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|Binds@Broker|<bind-id>
ID: <bind-id>
Wallet: <wallet-uuid>
Vault: any-vault.dom
VaultTitle: Any Vault
Schema: any-authority.dom/ANY-SCHEMA:1.0
SchemaTitle: Any Schema
```