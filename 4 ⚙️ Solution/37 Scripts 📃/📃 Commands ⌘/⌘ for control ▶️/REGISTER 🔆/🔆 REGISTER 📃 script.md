# 😃 .REGISTER 📃 script

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`REGISTER`](<🔆 REGISTER ⌘ cmd.md>) command.


## Diagram

![alt text](<🔆 REGISTER ⚙️ uml.png>)

## Script

```yaml
📃 .REGISTER:

# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: Script
    Texts: Script

# Save the temporary talker
- SAVE|Host.Talkers >> $talker:
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
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Host.Talkers` 🪣 table](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🪣 Host tables/Talkers 😃 table/Talkers 🪣/😃 Host.Talkers 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) |  [`$.Hosted`](<../../../📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>) [`$.Inputs`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
|

## FAQ

1. **Isn't there a security issue with multiple domains on the same table?**

    No. 
    * [Domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) cannot access this table.
    * It's abstracted by [Talker 😃 helper domains](<../../../../35 💬 Chats/Talkers 😃/😃 Talker/😃🤲 Talker helper.md>). 

    ---
    <br/>