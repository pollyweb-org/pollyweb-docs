# 🈯 TRANSLATE DOMAIN 📃 script


## Script

```yaml
📃 .TRANSLATE-DOMAIN:

# Get the Identity
- SEND >> $identity:
    Header:
        To: $.Hosted.Graph
        Subject: Identity@Graph
    Body:
        Domain: $Domain

# Find a matching translation
- SELECT >> $translation:
    First: .Value
    From: $identity.Translations
    Where: .Key.Is($To)
    
# Prepare the response
- SET|$return.Domain:
    Title: $identity.Title
    Description: $identity.Title
    Translation: $translation.Default(
        $domain.Title.Translate($To))

# Return the domain translation
- RETURN: $return
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`RETURN`](<../../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SELECT`](<../../../⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>) [`SEND`](<../../../⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`SET`](<../../../⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) |  [`.Translate`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Translate}.md>) [`.Key`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Key}.md>) [`.Value`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Value}.md>) [`.Default`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Default}.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Identity@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity/👥🚀🕸 Identity.md>) [`Schema@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Schema/👥🚀🕸 Schema.md>)
|