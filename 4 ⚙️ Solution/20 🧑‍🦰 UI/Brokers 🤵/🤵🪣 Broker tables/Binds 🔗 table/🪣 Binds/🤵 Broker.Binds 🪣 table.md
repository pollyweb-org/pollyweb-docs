# 🤵 Broker.Binds 🪣 table

> About
* Implements the [Broker 🤵 domain](<../../../🤵/🤵 Broker 🤲 helper.md>)
* Stores [Binds 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)

<br/>

## State Transitions

| Flow | [State 🛢](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 State.md>) | Description | Blame | Next action
|-|-|-|-|-
| [`Bind`](<../🪣🧱 10 Bind ⏩ flow/🤵 Broker.Binds.Bind ⏩ flow.md>) | [`OFFERED`](<../🪣🧱 11 Offered 🔔 event/🤵 OnBindOffered 🔔 handler.md>) | Offered by a [Vault 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) | [`Bind@Broker` 🐌](<../../../🤵📨 Broker msgs/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>) | [`TRANSLATE` 🈯](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
| | [`DETAILED`](<../🪣🧱 12 Detailed 🔔 event/🤵 OnBindDetailed 🔔 handler.md>) | Localization done | [`OnOffered` 🔔](<../🪣🧱 11 Offered 🔔 event/🤵 OnBindOffered 🔔 handler.md>) | [`CONFIRM` 👍](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>)
| | [`ACTIVE`](<../🪣🧱 13 Bound 🔔 event/🤵 OnBindBound 🔔 handler.md>) | The user accepted it | [`OnDetailed` 🔔](<../🪣🧱 12 Detailed 🔔 event/🤵 OnBindDetailed 🔔 handler.md>) | [`Bound@Vault` 🐌](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️📨 Vault msgs/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
| | [`REJECTED`](<../🪣🧱 14 Rejected 🔔 event/🤵 OnBindRejected 🔔 handler.md>) | The user rejected it | [`OnDetailed` 🔔](<../🪣🧱 12 Detailed 🔔 event/🤵 OnBindDetailed 🔔 handler.md>) |[`Bound@Vault` 🐌](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️📨 Vault msgs/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|[`Remove`](<../🪣🧱 60 Remove ⏩ flow/🤵 Broker.Binds.Remove ⏩ flow.md>) | [`REMOVED`](<../🪣🧱 61 Removed 🔔 event/🤵 OnBindRemoved 🔔 handler.md>) | The user removed it | Pop 🎈 | [`Unbound@Vault`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️📨 Vault msgs/Unbound 🤵🐌🗄️/🗄️ Unbound 🐌 msg.md>)
||

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
Prefix: Broker
Table: Binds
Item: Bind
Key: 
    - Vault  # The Vault that offered the Bind
    - Bind   # The Bind ID in the Vault 
```

<br/>

The [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are: [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) [`Domains`](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) [`Schemas`](<../../Schemas 🧩 table/🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>)

```yaml
Parents:

    Chat:    # Chat where the Bind was offered
    
    Wallet:  # Wallet that owns the Bind
    
    Vault:   # Vault that offered the Bind
        Domains.Name: Binds.Vault
        Domains.Wallet: Binds.Wallet

    Schema:  # Schema that defines the Bind
        Schemas.Code: Binds.Schema
        Schemas.Wallet: Binds.Wallet
```

<br/>

Here's the [Item 🛢 Propagate](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Propagate.md>) definition.

```yaml
Propagate:
    - Vault   # Auto-create Domains from Bind.Vault
    - Schema  # Auto-create Schemas from Binds.Schema
```

<br/>

Here's the [`Item Handlers`](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) definition.

```yaml
Handlers:

    # Frontend update
    ALTERED   >> OnBindAltered: 

    # Bind flow
    OFFERED   >> OnBindOffered:
    DETAILED  >> OnBindDetailed:
    ACTIVE    >> OnBindBound:

    # Localize flow
    UPDATED   >> OnBindLocalized:
        Assert: New.Language

    # Remove flow
    REMOVED   >> OnBindRemoved:
```

<br/>

Here's the [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Assert:

    # Bulk assertions
    AllOf: Chat, Bind, Wallet, Vault, Schema, Language
    UUIDs: Chat, Bind, Wallet

    # Field assertions
    .State.IsIn: OFFERED, DETAILED, REJECTED, ACTIVE, REMOVED
    Vault.IsDomain:
    Schema.IsSchema:
    Language.IsLanguage:
```

Uses: [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) [`.IsDomain`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsSchema`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>) [`.IsLanguage`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsLanguage ⓕ.md>)

<br/>


Here's the [Item 🛢 Views](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Views.md>) definition.

```yaml
Views:
    
    FRONTEND: # Filter for Frontend@ 
        .State.IsIn: ACTIVE # From the Bind lifecycle

    QUERY: # Filter for Query@ 
        .State.IsIn: ACTIVE # From the Bind lifecycle
```

Uses: [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>)

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# From Bind@Broker
Chat: <chat-uuid>
Bind: <bind-uuid>
Vault: any-vault.dom
Schema: any-authority.dom/ANY-SCHEMA:1.0
Wallet: <wallet-uuid>
Language: en-US

# From OnBindOffered
VaultTitle: Any Vault
SchemaTitle: Any Schema
```