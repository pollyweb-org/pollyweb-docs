# 🤵 OnInviteInvited 📃 handler

> About
* Part of the [`Broker.Invites` 🪣 table](<../🪣 Invites/🤵 Broker.Invites 🪣 table.md>)
* Reacts to the [`Invite@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)


<br/>

## Diagram

![alt text](<🤵 OnInviteInvited ⚙️ uml.png>)
  
<br/>

## Script

```yaml
📃 OnInvited:

Assert: 
        Host: $.Msg.From # Only from the host
        .State: ACTIVE   # While the chat is active
```
Uses: [`RUN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
