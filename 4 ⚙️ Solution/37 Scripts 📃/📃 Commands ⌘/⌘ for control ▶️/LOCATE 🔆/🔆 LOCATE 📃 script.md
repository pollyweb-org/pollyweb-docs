# 😃 .LOCATE 📃 script

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`LOCATE`](<🔆 LOCATE ⌘ cmd.md>) command.


## Diagram

![alt text](<🔆 LOCATE ⚙️ uml.png>)

## Script

```yaml
📃 .LOCATE:

# Assert the inputs
- ASSERT|.Inputs:
    AllOf: Script
    Texts: Script

# Save the temporary talker
- SAVE|Talker.Talkers >> $talker:
    Domain: $.Hosted.Domain
    Key: .UUID
    Script: $Script
    Inputs: $Inputs
    .Delete: 1 minute

# Return the locator
- RETURN: 
    .HOST,
    {$talker.Domain},
    {$talker.Key}
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Talker.Talkers` 🪣 table](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃 Talker.Talkers 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) |  [`$.Hosted`](<../../../📃 Holders 🧠/🧠 System holders/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
|

## FAQ

1. **Isn't there a security issue with multiple domains on the same table?**

    No. 
    * [Domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) cannot access this table.
    * It's abstracted by [Talker 😃 helper domains](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>). 

    ---
    <br/>