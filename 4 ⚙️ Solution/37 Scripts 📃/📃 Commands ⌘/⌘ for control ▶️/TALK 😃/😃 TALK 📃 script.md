# 😃 TALK 📃 script

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`TALK`](<😃 TALK ⌘ cmd.md>) command.
* Requires a previous invocation of the [`CHAT`](<../../⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) command.


## Diagram

![alt text](<😃 TALK ⚙️ uml.png>)

## Script

```yaml
📃 .TALK:

# Get the handler
- READ >> $talker:
    Set: Talker.Handlers
    Key: 
        Domain: $.Hosted.Domain
        Schema: $.Chat.Schema

# Run the script
- RUN:
    $talker.Script
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`READ`](<../../⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RUN`](<../RUN 🏃/🏃 RUN ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../📃 Holders 🧠/🧠 System holders/$.Chat 💬/💬 $.Chat 🧠 holder.md>) [`$.Hosted`](<../../../📃 Holders 🧠/🧠 System holders/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
|

## FAQ

1. **Isn't there a security issue with multiple domains on the same table?**

    No. 
    * [Domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) cannot access this table.
    * It's abstracted by [Talker 😃 helper domains](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>). 

    ---
    <br/>