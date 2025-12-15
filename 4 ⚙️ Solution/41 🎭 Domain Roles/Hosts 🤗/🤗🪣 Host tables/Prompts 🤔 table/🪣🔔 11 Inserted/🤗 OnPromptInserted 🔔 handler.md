# 🤗 OnPromptInserted 🔔 handler

> About
* Part of the [Host 🤗 domain](<../../../🤗 Host role/🤗🎭 Host role.md>) role
* Part of the [`Host.Prompts` 🪣 table](<../🪣 Prompts/🤗 Host.Prompts 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤗 OnPromptInserted ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnInserted:

# Assert the Prompt
- ASSERT $Prompt:
    AllOf: Language, Chat, Chat.Language
    UUIDs: Chat
    Texts: Language, Chat.Language, Text, Details
    Lists: Options

# Assert the options
- ASSERT $Prompt.Options:
    AllOf: Title
    Texts: Title

# Translate only if languages differ
- IF $Prompt.Language.Differs($Prompt.Chat.Language):
    TRANSLATE|$Prompt:
        From: Chat.Language
        To: Language
        All: Text, Details, Options.Title

# Progress the state
- SAVE $Prompt:
    State: TRANSLATED
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`TRANSLATE`](<../../../🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) |
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Host.Prompts`](<../🪣 Prompts/🤗 Host.Prompts 🪣 table.md>) [`Host.Chats`](<../../Chats 💬 table/🪣 Chats/🤗 Host.Chats 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Differs`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Differs ⓕ.md>)
|