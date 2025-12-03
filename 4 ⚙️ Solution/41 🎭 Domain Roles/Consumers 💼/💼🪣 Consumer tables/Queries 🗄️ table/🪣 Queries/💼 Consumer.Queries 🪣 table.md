# 💼 Consumer.Queries 🪣 table


# State Transitions

| Blame | States | Exits
|-|-|-
|[`SHARE` ⌘](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/SHARE 💼/💼 SHARE ⌘ cmd.md>)| `QUERIED`
|[`Consume@` 🐌](<../../../💼🅰️ Consumer methods/Consume 🗄️🐌💼/💼 Consume 📃 handler.md>)| `CONSUME` `TRUSTED` `COLLECTED` | `INVALID` `UNTRUSTED`
|[`Receive@` 🐌](<../../../💼🅰️ Consumer methods/Receive 🧑‍🦰🐌💼/💼 Receive 📃 handler.md>)| `RECEIVED` `TOKENED` | `INVALID` `UNTRUSTED`


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
```
Uses: [`.AllOf`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/AllOf ⓕ.md>) [`.Lists`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Lists ⓕ.md>) [`.UUIDs`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/UUIDs ⓕ.md>) [`.Each`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Each ⓕ.md>) [`.IsDomain`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsSchema`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>)

<br/>

## Example

From [`SHARE` ⌘ command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/SHARE 💼/💼 SHARE 📃 script.md>) command

```yaml
Broker: any-broker.dom
Chat: <chat-uuid>
Schemas: 
  - any-authority.dom/ANY-SCHEMA
```

From [`Consume@Consumer` 🐌 handler](<../../../💼🅰️ Consumer methods/Consume 🗄️🐌💼/💼 Consume 📃 handler.md>)

```yaml
Vault: any-vault.dom
Schema: any-authority.dom/ANY-SCHEMA
Collect: <collect-uuid>
```

From [`OnQueryCollected` 🔔 handler](<../🪣🧱 23 Collected 🔔 event/💼 OnQueryCollected 🔔 handler.md>)

```yaml
Collected: {...}
```