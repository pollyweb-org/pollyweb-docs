# 🎴 OnTokenOffered 📃 handler

> Part of the [`Issuer.Tokens` 🪣 table](<../🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>)

<br/>

## Diagram

![alt text](<🎴 OnTokenOffered ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnTokenOffered:

# Assert the Token
- ASSERT $Token:
    AllOf: Token, Answer
    UUIDs: Token
    Answer.IsIn: ACCEPTED, DECLINED

# Continue the Talker
- REEL|$Token.Token:
    $Token.Answer.Is(ACCEPTED)
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`REEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Issuer.Tokens`](<../🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Is`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>) [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>)
|
