<!-- TODO: -->

# 🤗 Prompted@Host 📃 handler

> About
* Part of the [Host 🤗 domain](<../../🤗 Host role/🤗🎭 Host role.md>) role
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Prompted@Host` 🅰️ method](<🤗 Prompted 🚀 call.md>)
* Triggered by the [`Prompt@Host` 📃 script](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/PROMPT 🤔/🤔 PROMPT 📃 script.md>)
* Reads from the [`Host.Prompts` 🪣 table](<../../🤗🪣 Host tables/Prompts 🤔 table/🪣 Prompts/🤗 Host.Prompts 🪣 table.md>)


<br/>

## Diagram

![alt text](<🤗 Prompted ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Prompted@Host: 

# Assert inputs
- ASSERT|$.Msg:
    AllOf: Prompt
    UUIDs: Prompt

# Get the prompt
- READ >> $prompt:
    Set: Host.Prompts
    Key: $.Msg.Prompt
    Assert:
        Expires.IsFuture

# Verify the message
- VERIFY|$.Msg:
    Key: $prompt.Chat.PublicKey

# Returned the prompt details
- RETURN|$prompt:
    Text
    MinValue
    MaxValue
    Appendix
    Details
    Options
    Default
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Host.Prompts`](<../../🤗🪣 Host tables/Prompts 🤔 table/🪣 Prompts/🤗 Host.Prompts 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsFuture`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsFuture ⓕ.md>)
|