# 🤗 OnHostPromptTranslated 🔔 handler

> About
* Part of the [Host 🤗 domain](<../../../🤗 Host role/🤗🎭 Host role.md>) role
* Part of the [`Host.Prompts` 🪣 table](<../🪣 Prompts/🤗 Host.Prompts 🪣 table.md>)
* Asserts if the [Prompt 🤔](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) can be served by the [`Prompted@Host` 📨 msg](<../../../🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 📃 handler.md>)

<br/>

## Diagram

![alt text](<🤗 OnPromptTranslated ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnTranslated:

# Assert readiness for Prompted@Host
- ASSERT|$Prompt:
    AllOf: Text
    Nums: MinValue, MaxValue
    UUIDs: Appendix
    Texts: Text, Details, Default
    Lists: Options
    Options.Length: 250
    MinValue.IsBelow: MaxValue
    Text.Length.IsBelow: 250
    Details.Length.IsBelow: 2500
    
# Assert the option items
- ASSERT|$Prompt.Options:
    AllOf: ID, Title
    Texts: ID, Title, Locator
    ID.Length.IsBelow: 250
    Title.Length.IsBelow: 250

# Progress the state
- SAVE|$Prompt:
    .State: ASSERTED
    Expires: .Now.Add(5 minutes)
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Host.Prompts`](<../🪣 Prompts/🤗 Host.Prompts 🪣 table.md>) 
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Add`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ.md>) [`.IsBelow`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsBelow ⓕ.md>) [`.Length`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Length ⓕ.md>) [`.Now`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Now ⓕ.md>) 
|