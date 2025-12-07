# 🤵 Broker.Invites 🪣 table


## Diagram

![alt text](<🤲 Helper.Helps ⚙️ uml.png>)

<br/>

## Schema

```yaml
Prefix: Broker
Table: Invites
Item: Invite
```

Here's the [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Assert:
    # Group assertions
    AllOf: Broker, Chat, Schema, Consumer, Invite
    UUIDs: Chat, Invite
    Texts: Schema, Consumer, Broker
    
    # Field assertions
    Broker.IsDomain:
    Helper.IsDomain:
    Schema.IsSchema:
```
Uses: [`.IsDomain`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsSchema`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>)

<br/>

## Example

From [`Invite@Broker` 🐌 msg](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)

```yaml
# Data info
Schema: any-authority.dom/ANY-SCHEMA

# Consumer info
Consumer: any-consumer.dom
Invite: <invite-uuid>

# Broker info
Broker: any-broker.dom
Chat: <chat-uuid>
```