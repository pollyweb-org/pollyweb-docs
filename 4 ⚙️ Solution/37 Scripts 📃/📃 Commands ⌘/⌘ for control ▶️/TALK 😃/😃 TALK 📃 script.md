# 😃 .TALK 📃 script

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`TALK`](<😃 TALK ⌘ cmd.md>) command.
* Requires a previous invocation of the [`CHAT`](<../../⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) command.


## Diagram

![alt text](<😃 TALK ⚙️ uml.png>)

## How to call

```yaml
- RUN|.TALK
```

## Script

```yaml
📃 .TALK:

# Get the talker
- READ >> $talker:
    Set: Talker.Talkers
    Key: 
        Domain: $.Hosted.Domain
        Key: $.Chat.Key

# Run the script
- RUN|$talker.Script:
    $talker.Inputs:
    $.Chat.Inputs:
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`READ`](<../../⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RUN`](<../RUN 🏃/🏃 RUN ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Talker.Talkers` 🪣 table](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃 Talker.Talkers 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../📃 Holders 🧠/🧠 System holders/$.Chat 💬/💬 $.Chat 🧠 holder.md>) [`$.Hosted`](<../../../📃 Holders 🧠/🧠 System holders/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
|

## FAQ

1. **Isn't there a security issue with multiple domains on the same table?**

    No. 
    * [Domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) cannot access this table.
    * It's abstracted by [Talker 😃 helper domains](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>). 

    ---
    <br/>