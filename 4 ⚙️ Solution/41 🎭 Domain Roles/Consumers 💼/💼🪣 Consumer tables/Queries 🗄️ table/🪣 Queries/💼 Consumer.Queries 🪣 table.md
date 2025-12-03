# 💼 Consumer.Queries 🪣 table

> About
* Part of the [Consumer 💼 domain](<../../../💼 Consumer/💼🎭 Consumer role.md>) role

<br/>

## State Transitions

| Blame | States ✅ | Exits ❌ | 
|-|-|-
|[`SHARE` ⌘](<../../../💼⌘ Consumer cmds/SHARE 💼/💼 SHARE ⌘ cmd.md>)| [`QUERIED`](<../🪣🧱 11 Queried 🔔 event/💼 OnQueryQueried 🔔 handler.md>)
|[`Consume@` 🐌](<../../../💼📨 Consumer msgs/Consume 🗄️🐌💼/💼 Consume 📃 handler.md>)| [`CONSUME`](<../🪣🧱 21 Consume 🔔 event/💼 OnQueryConsume 🔔 handler.md>) [`TRUSTED`](<../🪣🧱 22 Trusted 🔔 event/💼 OnQueryTrusted 🔔 handler.md>) [`COLLECTED`](<../🪣🧱 23 Collected 🔔 event/💼 OnQueryCollected 🔔 handler.md>) | `INVALID` `UNTRUSTED`
|[`Receive@` 🐌](<../../../💼📨 Consumer msgs/Receive 🧑‍🦰🐌💼/💼 Receive 📃 handler.md>)| [`RECEIVED`](<../🪣🧱 31 Received 🔔 event/💼 OnQueryReceived 🔔 handler.md>) [`TOKENED`](<../🪣🧱 32 Tokened 🔔 event/💼 OnQueryTokened 🔔 handler.md>) | `INVALID` `CORRUPTED` `UNTRUSTED`


<br/>

## Schema

Here's the [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Assert:

    # Group assertions
    AllOf: Broker, Chat, Schemas
    UUIDs: Chat, Collect
    Lists: Schemas
    
    # Field assertions
    Broker.IsDomain:
    Schemas.Each.IsSchema:
    
    # From Consume@Broker
    Vault.IsDomain:
    Schema.IsSchema:
    Schema.IsIn: Schemas
```
Uses: [`.AllOf`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/AllOf ⓕ.md>) [`.Lists`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Lists ⓕ.md>) [`.UUIDs`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/UUIDs ⓕ.md>) [`.Each`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Each ⓕ.md>) [`.IsDomain`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsSchema`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>)

<br/>

## Example

From [`SHARE` ⌘ command](<../../../💼⌘ Consumer cmds/SHARE 💼/💼 SHARE 📃 script.md>) command

```yaml
Broker: any-broker.dom
Chat: <chat-uuid>
Context: {...}
Schemas: 
  - any-authority.dom/ANY-SCHEMA
```

From [`Consume@Consumer` 🐌 handler](<../../../💼📨 Consumer msgs/Consume 🗄️🐌💼/💼 Consume 📃 handler.md>)

```yaml
Vault: any-vault.dom
Schema: any-authority.dom/ANY-SCHEMA
Collect: <collect-uuid>
```

From [`OnQueryCollected` 🔔 handler](<../🪣🧱 23 Collected 🔔 event/💼 OnQueryCollected 🔔 handler.md>)

```yaml
Collected: {...}
```