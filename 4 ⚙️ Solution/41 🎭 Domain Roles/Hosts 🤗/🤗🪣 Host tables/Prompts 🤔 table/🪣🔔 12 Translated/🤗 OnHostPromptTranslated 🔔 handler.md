# 🤗 OnHostPromptTranslated 🔔 handler

> About
* Part of the [Host 🤗 domain](<../../../🤗 Host role/🤗🎭 Host role.md>) role
* Part of the [`Host.Prompts` 🪣 table](<../🪣 Prompts/🤗 Host.Prompts 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤗 OnHostPromptTranslated ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnPromptTranslated:

# Assert readiness for Prompted@Host
- ASSERT|$Prompt:
    AllOf: Text
    Nums: MinValue, MaxValue
    UUIDs: Appendix
    Texts: Text, Details, Default
    Lists: Options

# Progress the state
- SAVE|$Prompt:
    .State: ASSERTED
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Host.Prompts`](<../🪣 Prompts/🤗 Host.Prompts 🪣 table.md>) 
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | 
|