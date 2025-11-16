# 🕸 About 📃 handler

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`About@Graph` 🅰️ method](<🕸 About 📃 handler.md>)

## Script

```yaml
📃 About@Graph:

# Verify the message
- VERIFY|$.Msg

# Assert the message
- ASSERT|$.Msg:
    AllOf: Domain
    Texts: Domain, Language

# Default the language
- DEFAULT|$.Msg:
    Language: en-us

# Read the domain
- READ >> $about:
    Set: Graph.Abouts
    Key: $.Msg.Domain
    Get: 
        SmallIcon, BigIcon,
        Title, Description, 
        Translations, Language.Default(en-us)

# Translate if languages differ
- IF|$about.Language.IsNot($.Msg.Language):
    
    # Try to get an existing translation
    - PUT >> $translation:
        $about.Translations.First({Language: $.Msg.Language}) 
    
    # If found, use it
    - IF|$translation:
        SET|$about:
            Title: $translation.Title
            Description: $translation.Description
    
    # If not found, translate it on the fly
    - IF|$translation.IsEmpty:
        SET|$about:
            Title.Translate(Language, $.Msg.Language),
            Description.Translate(Language, $.Msg.Language)

# Return the output
- RETURN:
    $about.Remove(Translations)
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)| [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PUT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SET`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|[Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>)|[`Graph.Abouts`](<../../🕸🪣 Graph tables/Abouts 👥/🕸 Graph.Abouts 🪣 table.md>)
|[{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.First`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.First}.md>) [`.IsNot`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsNot}.md>) [`.Remove`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Remove}.md>) [`.Translate`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Translate}.md>) 
|[Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)|[`$.Msg` 🧠 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|[Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`ABOUT`](<../../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 ABOUT.md>)
|