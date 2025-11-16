# 🕸 Translate Domain 📃 handler


> Behavior
* Tries to use existing translations from the [domain Manifest 📜](<../../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>)
* If not found, translates on the fly using the [`.Translate` function](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Translate ⓕ.md>)

## Script

```yaml
📃 Translate-Domain:

IF|$.Msg.Domain.IsEmpty: RETURN
IF|$.Msg.Target.IsEmpty: RETURN

# Read the about item
- READ >> $item:
    Set: Graph.Abouts
    Key: $.Msg.Domain

# Translate if languages differ
- IF|$item.Language.IsNot($.Msg.Language):
    
    # Try to get an existing translation
    - PUT >> $translation:
        $item.Translations.First({Language: $.Msg.Language}) 
    
    # If found...
    - IF|$translation:

        # Use the translation
        SET|$output:
            Title: $translation.Title
            Description: $translation.Description
    
    # If not found...
    - IF|$translation.IsEmpty:

        # Translate it on the fly
        - SET|$output:
            Title.Translate(Language, $.Msg.Language),
            Description.Translate(Language, $.Msg.Language)

        # Cache the new translation
        - PUT >> $translation:
            Language: $.Msg.Language
            Title: $output.Title
            Description: $output.Description
        - SAVE|$item:
            Translations.Append($translation)

# Return the output
- RETURN:
    $output
```

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)| [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SET`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>) [`VERIFY`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>)|[`Graph.Abouts`](<../../../🕸🪣 Graph tables/Abouts 👥/🕸 Graph.Abouts 🪣 table.md>)
|[{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.First`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/First ⓕ.md>) [`.IsNot`](<../../../../../37 Scripts 📃/📃 Holders 🧠/Any 📚 holders/IsNot ⓕ any.md>) [`.Remove`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Remove ⓕ.md>) [`.Translate`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Translate ⓕ.md>) 
|[Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)|[`$.Msg` 🧠 holder](<../../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|[Schema Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`ABOUT`](<../../../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 ABOUT.md>) [`TRANSLATION`](<../../../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 TRANSLATION.md>)
|