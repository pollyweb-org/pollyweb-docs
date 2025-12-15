# 🈯 TRANSLATE 📃 script

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`TRANSLATE`](<🈯 TRANSLATE ⌘ cmd.md>) command.

## Flow

![alt text](<🈯 TRANSLATE ⚙️ uml.png>)

## How to call

```yaml
- RUN .TRANSLATE:
    From: en-us
    To: pt-br
    Domain: any-domain.dom
    Schema: any-authority.dom/ANY-SCHEMA
    Text: Any ´not translatable´ text
```

## Script

```yaml
📃 .TRANSLATE:

# Assert inputs
- ASSERT $.Inputs:
    Texts: From, To, Text
    Lists: Domains, Schemas

# Default the languages
- DEFAULT $.Inputs:
    From: $.Script.Language
    To: $.Chat.Language, $.Msg.Language

# Get the domain info
- IF $Domain:
    RUN .TRANSLATE-DOMAIN >> $domain:
        $Domain

# Get the schema info
- IF $Domain:
    RUN .TRANSLATE-SCHEMA >> $schema:
        $Schema

# Translate the text, if any
- IF $Text:
    PUT >> $text:
        $Text.Translate: $From, $To

# Return the translations
- RETURN: 
    Domain: $domain
    Schema: $schema
    Text: $text
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`DEFAULT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/DEFAULT 📭/📭 DEFAULT ⌘ cmd.md>) [`IF`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.AnyOf`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/AnyOf ⓕ.md>) [`.Translate`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Translate ⓕ.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/🏃 $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`About@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 About/🕸 About 🚀 call.md>) [`Schema@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Schema/🕸 Schema 🚀 call.md>)
|