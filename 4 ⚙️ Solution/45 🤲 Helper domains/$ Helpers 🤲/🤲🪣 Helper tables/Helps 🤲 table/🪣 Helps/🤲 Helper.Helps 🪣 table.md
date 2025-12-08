# 🤵 Broker.Invites 🪣 table


## Lifecycle

![alt text](<🤲 Helper.Helps ⚙️ uml.png>)



<br/>

## Schema

```yaml
Prefix: Broker
Table: Invites
Item: Invite
```

<br/>

The [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) are [`Invited`](<../🪣🔔 1 Invited/🤲 Help.OnInvited 🔔 handler.md>) [`Trusted`](<../🪣🔔 2 Trusted/🤲 Help.OnTrusted 🔔 handler.md>) [`Authorized`](<../🪣🔔 3 Authorized/🤲 Help.OnAuthorized 🔔 handler.md>) [`Valid`](<../🪣🔔 4 Valid/🤲 Help.OnValid 🔔 handler.md>) [`Helped`](<../🪣🔔 5 Helped/🤲 Help.OnHelped 🔔 handler.md>) [`Billable`](<../🪣🔔 6 Billable/🤲 Help.OnBillable 🔔 handler.md>)

```yaml
Handlers:
    INVITED     >> OnInvited:     # Calls Trusts@Graph
    TRUSTED     >> OnTrusted:     # Calls Authorized@Biller
    AUTHORIZED  >> OnAuthorized:  # Calls Consumer.Invited
    VALID       >> OnValid:       # Runs from Helper.Schemas
    HELPED      >> OnHelped:      # Calls Helped@Consumer
    BILLABLE    >> OnBillable:    # Calls Bill@Biller
```

<br/>

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