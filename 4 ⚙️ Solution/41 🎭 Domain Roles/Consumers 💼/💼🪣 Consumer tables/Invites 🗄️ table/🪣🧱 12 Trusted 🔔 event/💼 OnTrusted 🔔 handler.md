# 💼 OnInviteTrusted 🔔 handler

> About
* Part of the [`Consumer.Queries` 🪣 table](<../../Queries 🗄️ table/🪣 Queries/💼 Consumer.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<💼 OnTrusted ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnInviteTrusted:

# Ask the Broker
- SEND:
    Header:
        To: $Invite.Broker
        Subject: Invite@Broker
    Body: 
        Chat: $Invite.Chat
        Helper: $Invite.Helper
        Invite: $Invite.ID
        Schema: $Invite.Schema
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Consumer.Invites`](<../🪣 Invites/💼 Consumer.Invites 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Invite@Broker` 🐌 msg](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)