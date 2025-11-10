# 🈯 TRANSLATE 📃 script

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`TRANSLATE`](<🈯 TRANSLATE ⌘ cmd.md>) command.

## Flow

![alt text](<🈯 TRANSLATE ⚙️ uml.png>)

## How to call

```yaml
- RUN|.TRANSLATE:
    From: en-us
    To: pt-br
    Domains: 
      - any-domain.dom
    Schemas: 
      - any-authority.dom/ANY-SCHEMA
    Text: Any ((not translatable)) text
```

## Script

```yaml
📃 .TRANSLATE:

# Assert inputs
- ASSERT|$.Inputs:
    Texts: From, To, Text
    Lists: Domains, Schemas

# Default the languages
- DEFAULT|$.Inputs:
    From: $.Script.Language
    To: $.Chat.Language, $.Msg.Language

# Get the translations from Graph, if needed
- IF|.AnyOf($Domains, $Schemas):
    SEND >> $graph-translations:
        Header:
            To: $.Hosted.Graph
            Subject: Translate@Graph
        Body:
            Language: $From
            Domains: $Domains
            Schemas: $Schemas

# Translate the text, if any
- IF|$Text:
    PUT >> $text-translation:
        Text: $Text.Translate($From, $To)

# Return the translations
- RETURN:
    $graph-translations
    $text-translation
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`DEFAULT`](<../../⌘ for holders 🧠/DEFAULT 📭/📭 DEFAULT ⌘ cmd.md>) [`IF`](<../../⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`RETURN`](<../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SEND`](<../../⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.AnyOf`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.AnyOf}.md>) [`.Translate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Translate}.md>)
|