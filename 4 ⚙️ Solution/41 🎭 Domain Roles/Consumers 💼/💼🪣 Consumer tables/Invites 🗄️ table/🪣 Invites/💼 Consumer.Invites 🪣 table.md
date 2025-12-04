# 💼 Consumer.Invites 🪣 table

> About
* Part of the [Consumer 💼 domain](<../../../💼 Consumer/💼🎭 Consumer role.md>) role

<br/>

## Lifecycle

![alt text](<💼 Consumer.Invites ⚙️ uml.png>)

<br/>

## State Transitions

| Blame | States ✅ | Exits ❌ | 
|-|-|-
|[`INVITE` ⌘](<../../../💼⌘ Consumer cmds/INVITE 🤲/🤲 INVITE ⌘ cmd.md>)| [`INVITED`](<../🪣🧱 11 Invited 🔔 event/💼 OnInviteInvited 🔔 handler.md>)
|[`Consume@` 🐌](<../../../💼📨 Consumer msgs/Consume 🗄️🐌💼/💼 Consume 📃 handler.md>)| [`CONSUME`](<../../Queries 🗄️ table/🪣🧱 21 Consume 🔔 event/💼 OnQueryConsume 🔔 handler.md>) [`TRUSTED`](<../../Queries 🗄️ table/🪣🧱 22 Trusted 🔔 event/💼 OnQueryTrusted 🔔 handler.md>) [`COLLECTED`](<../../Queries 🗄️ table/🪣🧱 23 Collected 🔔 event/💼 OnQueryCollected 🔔 handler.md>) | `INVALID` `UNTRUSTED`
|[`Receive@` 🐌](<../../../💼📨 Consumer msgs/Receive 🧑‍🦰🐌💼/💼 Receive 📃 handler.md>)| [`RECEIVED`](<../../Queries 🗄️ table/🪣🧱 31 Received 🔔 event/💼 OnQueryReceived 🔔 handler.md>) [`TOKENED`](<../../Queries 🗄️ table/🪣🧱 32 Tokened 🔔 event/💼 OnQueryTokened 🔔 handler.md>) | `INVALID` `CORRUPTED` `UNTRUSTED`


<br/>

## Schema

Here's the [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Assert:

    # Group assertions
    AllOf: Broker, Chat, Schema, Helper
    UUIDs: Chat
    
    # Field assertions
    Broker.IsDomain:
    Helper.IsDomain:
    Schema.IsSchema:    
```

Uses:  [`.IsDomain`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsSchema`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>)

<br/>

## Example

From [`INVITE` ⌘ command](<../../../💼⌘ Consumer cmds/INVITE 🤲/🤲 INVITE 📃 script.md>) command

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

From [`OnQueryCollected` 🔔 handler](<../../Queries 🗄️ table/🪣🧱 23 Collected 🔔 event/💼 OnQueryCollected 🔔 handler.md>)

```yaml
Collected: {...}
```