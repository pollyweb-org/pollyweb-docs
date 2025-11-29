<!-- TODO 

[`Reply handler`](<🤗 Reply 📃 handler.md>)
[`Reply@Host` 🅰️ method](<🤗 Reply 🐌 msg.md>)
[`Prompt@Host`](<../../🤗🧩 Host schemas/🧩 HOST.md>)
-->

# 🤗 Reply@Host 📃 handler

> About
* Part of the [Host 🤗 domain](<../../🤗 Host role/🤗🎭 Host role.md>) role
* Implements the [`Reply@Host` 🅰️ method](<🤗 Reply 🐌 msg.md>)
* Triggers the [`OnHostPromptReplied` 📃 handler](<../../🤗🪣 Host tables/Prompts 🤔 table/🪣🔔 14 Replied/🤗 OnHostPromptReplied 🔔 handler.md>)

<br/>

## Diagrams

![alt text](<🤗 Reply ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Reply@Host:

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Prompt, Result 
    UUIDs: Prompt
    # Answer may be empty
    # Answer has any structure

# Get the prompt
- READ >> $prompt:
    Set: Host.Prompts
    Key: $.Msg.Prompt

# Verify the message
- VERIFY|$.Msg:
    Key: $prompt.Chat.PublicKey

# Set the result
- SAVE|$prompt:
    $.Msg.Result
    $.Msg.Answer 
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Host.Prompts`](<../../🤗🪣 Host tables/Prompts 🤔 table/🪣 Prompts/🤗 Host.Prompts 🪣 table.md>) [`Host.Chats`](<../../🤗🪣 Host tables/Chats 💬 table/🪣 Chats/🤗 Host.Chats 🪣 table.md>)
|