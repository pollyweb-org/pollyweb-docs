# 🈯 TRANSLATE DOMAIN 📃 script


## Script

```yaml
📃 .TRANSLATE-DOMAIN:

# Get the Identity
- SEND >> $identity:
    Header:
        To: $.Hosted.Graph
        Subject: About@Graph
    Body:
        Domain: $Domain

# Find a matching translation
- SELECT >> $translation:
    First: .Value
    From: $identity.Translations
    Where: .Key.Is($To)
    
# Prepare the response
- SET $return.Domain:
    Title: $identity.Title
    Description: $identity.Title
    Translation: $translation.Default(
        $domain.Title.Translate($To))

# Return the domain translation
- RETURN: $return
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SELECT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`SET`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) |  [`.Translate`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Translate ⓕ.md>) [`.Key`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Key ⓕ.md>) [`.Value`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Value ⓕ.md>) [`.Default`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Default ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`About@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 About/🕸 About 🚀 call.md>) [`Schema@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Schema/🕸 Schema 🚀 call.md>)
|