# 🤵 Broker.Invites 🪣 table

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
    AllOf: Chat, Schema, Helper
    UUIDs: Chat
    
    # Field assertions
    Helper.IsDomain:
    Schema.IsSchema:

    # Dependencies
    Chat.State: ACTIVE 
```

<br/>

## Example

From [`Invite@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)

```yaml
Chat: <chat-uuid>
Schema: any-authority.dom/ANY-SCHEMA
Helper: any-helper.dom
```