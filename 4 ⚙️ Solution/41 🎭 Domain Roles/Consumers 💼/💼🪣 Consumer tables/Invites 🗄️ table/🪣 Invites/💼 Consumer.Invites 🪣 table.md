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
|[`INVITE` ⌘](<../../../💼⌘ Consumer cmds/INVITE 🤲/🤲 INVITE ⌘ cmd.md>)| [`INVITED`](<../🪣🔔 11 Invited/💼 OnInvited 🔔 handler.md>) [`TRUSTED`](<../🪣🔔 12 Trusted/💼 OnTrusted 🔔 handler.md>) | `UNTRUSTED`
|[`Helped@` 🐌](<../../../💼📨 Consumer msgs/Helped 🤲🐌💼/💼 Helped 📃 handler.md>)| [`HELPED`](<../🪣🔔 21 Helped/💼 OnHelped 🔔 handler.md>)  [`VALID`](<../🪣🔔 22 Valid/💼 OnValid 🔔 handler.md>) | `INVALID` 



<br/>

## Schema

```yaml
Prefix: Consumer
Table: Invites
Item: Invite
```

<br/>

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
Helper: any-helper.dom
Schema: any-authority.dom/ANY-SCHEMA
Context: {...}
```

From [`Helped@Consumer` 🐌 handler](<../../../💼📨 Consumer msgs/Helped 🤲🐌💼/💼 Helped 📃 handler.md>)

```yaml
Help: {...}
```