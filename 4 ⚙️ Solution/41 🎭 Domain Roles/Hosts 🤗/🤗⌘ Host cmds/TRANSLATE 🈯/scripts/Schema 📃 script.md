# 🈯 TRANSLATE-SCHEMA 📃 script

> About
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that translates the [Schema Code 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) info to a specified language
* Part of the [`TRANSLATE` 📃 script](<../🈯 TRANSLATE 📃 script.md>)
* Implements the [`TRANSLATE` 🈯 command](<../🈯 TRANSLATE ⌘ cmd.md>)

<br/>

## Script

```yaml
📃 .TRANSLATE-SCHEMA:

# Get the schema info
- GRAPH Schema >> $schema:
    Schema: $Schema

# Find a matching translation
- SELECT >> $translation:
    First: .Value
    From: $schema.Translations
    Where: .Key.Is($To)
    
# Prepare the response
- SET $return.Domain:
    Title: $schema.Title
    Description: $schema.Title
    Translation: $translation.Default(
        $schema.Title.Translate($To))

# Return the domain translation
- RETURN: $return
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`GRAPH`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/GRAPH 🕸/🕸 GRAPH ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SELECT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>) [`SET`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Default`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Default ⓕ.md>)  [`.Is`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>)  [`.Key`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Key ⓕ.md>)  [`.Translate`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Translate ⓕ.md>) [`.Value`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Value ⓕ.md>)