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

Propagate:
    - Vault

Handlers:
    OnBindChanges: 
        Events: CHANGED
```

## Links

| Link | Table | Contains
|-|-|-
| Parent    | [`Wallets` 🪣](<../../Wallets 🧑‍🦰 table/🤵 Broker.Wallets 🪣 table.md>) | [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|| [`Domains` 🪣](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) | [domains 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)


## Handlers

| Handler | [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | Events
|-|-|-
| [`OnBindChanges` 📃](<../🪣🔔 OnBindChanges/🤵 OnBindChanges 📃 handler.md>) | [`Update@Notifier` 🅰️](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>) | `CHANGED`


## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|Binds@Broker|<bind-id>
ID: <bind-id>
Vault: any-vault.dom
Wallet: <wallet-uuid>
Schema: any-authority.dom/ANY-SCHEMA:1.0
```