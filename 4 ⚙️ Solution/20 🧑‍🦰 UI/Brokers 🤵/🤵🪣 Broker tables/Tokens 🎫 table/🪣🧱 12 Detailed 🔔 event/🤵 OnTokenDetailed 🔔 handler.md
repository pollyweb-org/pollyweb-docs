# 🤵 OnTokenDetailed 📃 handler

> Part of the [`Broker.Tokens` 🪣 table](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that asks the user to confirm or decline a newly issued [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>).
* Part of the [🤵 Broker.Tokens.Insert ⏩ flow](<../🪣🧱 10 Issue ⏩ flow/🤵 Broker.Tokens.Issue ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 OnTokenDetailed ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnTokenDetailed:

# Assert the inputs
- ASSERT $Token:
    AllOf: Chat

# Load the chat
- CHAT $Token.Chat

# Ask for confirmation
- CONFIRM >> $accepted:
    Text: > 
        Accept token?
        - `{$Token.Title}`

# Update with the answer
- SAVE $Token:
    State: OFFERED
    Accepted: $accepted
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CHAT`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Tokens`](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
|