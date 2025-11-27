# 🤵🪣 Binds @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Stores [Binds 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
# Binds.yaml
Prefix: Broker
Table: Binds
Item: Bind
Key: Vault, Wallet, Schema
```

<br/>

Here's the {{Item Parents}} definition.

```yaml
Parents:

    Chat: # Chat where the Bind was offered
        Chats.ID: Binds.Chat

    Wallet: # Wallet that owns the Bind
        Wallets.ID: Binds.Wallet
    
    Vault: # Vault that offered the Bind
        Domains.Name: Binds.Vault
        Domains.Wallet: Binds.Wallet

    Schema: # Schema that defines the Bind
        Schemas.Code: Binds.Schema
        Schemas.Wallet: Binds.Wallet

```

<br/>

Here's the {{Item Propagate}} definition.

```yaml
Propagate:
    - Vault
    - Schema
```

<br/>

Here's the {{Item Handlers}} definition.

```yaml
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

# Automatic
ID: <bind-id>

# From Bind@Broker
Hook: <hook-uuid>
Chat: <chat-uuid>
Vault: any-vault.dom
Schema: any-authority.dom/ANY-SCHEMA:1.0
Wallet: <wallet-uuid>
Language: en-US

# From OnBindOffered
VaultTitle: Any Vault
SchemaTitle: Any Schema
```