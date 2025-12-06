# 🤵 Broker.Invites 🪣 table

> About
* Part of the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) role

<br/>

## Lifecycle 

![alt text](<🤵 Broker.Invites ⚙️ uml.png>)

<br/>

## State Transitions

| Blame | OnSuccess ✅ | OnFailure ❌ | Next state
|-|-|-|-
| [`Invite@Broker` 🐌](<../../../🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>) | [`INVITED`](<../🪣🧱 1 Invited 🔔/🤵 OnInviteInvited 🔔 handler.md>)  | `INVALID` `UNTRUSTED` | [`TRUSTED`](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼🪣 Consumer tables/Invites 🗄️ table/🪣🧱 12 Trusted 🔔 event/💼 OnInviteTrusted 🔔 handler.md>) 
|| [`TRUSTED`](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼🪣 Consumer tables/Invites 🗄️ table/🪣🧱 12 Trusted 🔔 event/💼 OnInviteTrusted 🔔 handler.md>) || [`VERIFIED`](<../🪣🧱 3 Verified 🔔/🤵 OnInviteVerified 🔔 handler.md>) [`ADDED`](<../🪣🧱 4 Added 🔔/🤵 OnInviteAdded 🔔 handler.md>)
|| [`VERIFIED`](<../🪣🧱 3 Verified 🔔/🤵 OnInviteVerified 🔔 handler.md>) |  `REJECTED` | [`ADDED`](<../🪣🧱 4 Added 🔔/🤵 OnInviteAdded 🔔 handler.md>) 
|| [`ADDED`](<../🪣🧱 4 Added 🔔/🤵 OnInviteAdded 🔔 handler.md>) | | `DONE`

<br/>

## Schema

```yaml
Prefix: Broker
Table: Invites
Item: Invite
Key: Inviter, Invite 
```

The [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are: [`Broker.Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

```yaml
Parents: Chat
```

The [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) are: [`OnInvited`](<../🪣🧱 1 Invited 🔔/🤵 OnInviteInvited 🔔 handler.md>) [`OnVerified`](<../🪣🧱 3 Verified 🔔/🤵 OnInviteVerified 🔔 handler.md>) [`OnConfirmed`](<../🪣🧱 4 Added 🔔/🤵 OnInviteAdded 🔔 handler.md>).

```yaml
Handlers:
    INVITED: OnInvited
    VERIFIED: OnVerified
    CONFIRMED: OnConfirmed
```

Here's the [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Assert:
    # Group assertions
    AllOf: Chat, Schema, Helper, Inviter
    UUIDs: Chat
    
    # Field assertions
    Inviter.IsDomain:
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
Helper: any-helper.dom
Schema: any-authority.dom/ANY-SCHEMA
Inviter: any-host.dom
```