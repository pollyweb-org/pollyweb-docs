# 🗄️ Vault.Binds 🪣 table

> About
* Stores [Binds 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) in a [Vault 🗄️ domain](<../../../🗄️ Vault/🗄️🎭 Vault role.md>)

<br/>

## State Transitions

| Flow | [State 🛢](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 State.md>) | Blame | Description |
|-|-|-|-
| [`Bind`](<../🪣🧱 10 Bind ⏩ flow/🗄️ Vault.Binds.Bind ⏩ flow.md>) | [`OFFERED`](<../🪣🧱 11 Offered 🔔 event/🗄️ OnBindOffered 🔔 handler.md>) |[`BIND` ⌘](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND 📃 script.md>)| Created but not yet accepted by the user |
|| [`DECLINED`](<../🪣🧱 12 Declined 🔔 event/🗄️ OnBindDeclined 🔔 handler.md>) |[`Bound` 🐌 ](<../../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 📃 handler.md>)| Offered but the user declined it |
|| [`BOUND`](<../🪣🧱 12 Bound 🔔 event/🗄️ OnBindBound 🔔 handler.md>) |[`Bound` 🐌 ](<../../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 📃 handler.md>)| Active, with the [Vault 🗄️ domain](<../../../🗄️ Vault/🗄️🎭 Vault role.md>) holding it |
|[`Unbound`](<../🪣🧱 20 Unbind ⏩ flow/🗄️ Vault.Binds.Unbound ⏩ flow.md>)| [`UNBOUND`](<../🪣🧱 21 Unbound 🔔 event/🗄️ OnBindUnbound 🔔 handler.md>) |[`Unbound` 🐌](<../../../🗄️🅰️ Vault methods/Unbound 🤵🐌🗄️/🗄️ Unbound 📃 handler.md>)| Removed from the [Wallet 🧑‍🦰 app](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) |
|


<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
Prefix: Vault
Table: Binds
Item: Bind
```

The [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) are: [`OnOffered`](<../🪣🧱 11 Offered 🔔 event/🗄️ OnBindOffered 🔔 handler.md>) [`OnBound`](<../🪣🧱 12 Bound 🔔 event/🗄️ OnBindBound 🔔 handler.md>) [`OnDeclined`](<../🪣🧱 12 Declined 🔔 event/🗄️ OnBindDeclined 🔔 handler.md>) [`OnUnbound`](<../🪣🧱 21 Unbound 🔔 event/🗄️ OnBindUnbound 🔔 handler.md>)

```yaml
Handlers:
    OFFERED  >> OnBindOffered:   # Calls Bind@Broker
    BOUND    >> OnBindBound:     # Returns the Bind to BIND ⌘
    DECLINED >> OnBindDeclined:  # Returns empty to BIND ⌘
    UNBOUND  >> OnBindUnbound:   # Calls Hosted.Handle(unbound)
```

The [Item 🛢 Asserts](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) are:

```yaml
Asserts:
    
    # Group assertions
    AllOf: Chat, Broker, Schema
    UUIDs: Chat
    Texts: Broker, Schema, Reference
    
    # Field assertions
    Broker.IsDomain:
    Schema.IsSchema:
    
    # State transitions
    .State.IsIn: OFFERED, DECLINED, BOUND, UNBOUND
```

Uses: [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) [`.IsDomain`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsSchema`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>)


<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# Automatic
ID: <bind-id>

# From BIND command
Chat: <chat-id>             # Chat where the Bind was offered
Broker: any-broker.dom      # Broker owning the Chat
Schema: .BIND               # Schema offered
Reference: <reference>      # Hosted domain internal anchor 
Internals: {...}            # Hosted domain internal data 
```

| Property | Type | Details | From | Purpose |
|-|-|-|-|-
| `ID` | uuid | [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) ID |  | [`Bind@Broker`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>) |
| `Chat` | uuid | [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`$.Chat`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) | [`Bind@Broker`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>)
| `Broker` |text| [Broker 🤵 domain](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`$.Chat`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) | [`Bind@Broker`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>)
| `Schema` |text| [Schema Code 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`BIND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>) | [`Bind@Broker`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>)
| `Reference` | text | [Hosted 📦](<../../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>) internal anchor | [`BIND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>) | [`ASYNC`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/ASYNC 👷🏼/👷🏼 ASYNC ⌘ cmd.md>)
| `Internals` | map | [Hosted 📦](<../../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>) internal data | [`BIND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>) | [`ASYNC`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/ASYNC 👷🏼/👷🏼 ASYNC ⌘ cmd.md>)
| `Answer` | enum | `ACCEPTED` `DECLINED` | [`Bound@`](<../../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>) | 
|