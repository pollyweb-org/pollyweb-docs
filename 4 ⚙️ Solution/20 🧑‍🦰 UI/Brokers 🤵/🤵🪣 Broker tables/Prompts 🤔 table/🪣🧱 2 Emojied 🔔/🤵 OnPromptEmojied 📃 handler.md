# 🤵 OnPromptEmojied 📃 handler


## Script

```yaml
📃 OnPromptEmojied:

# Assert the prompt
- ASSERT|$Prompt:
    AllOf: Hook, Chat, Wallet, Sender, Notifier
    UUIDs: Hook, Chat, Wallet
    Texts: Format, Emoji, Sender, Notifier
    Emoji.Length.IsAtMost: 1

# Forward to the notifier
- SEND: 
    Header:
        To: $Prompt.Notifier
        Subject: Prompt@Notifier    
    Body:
        Chat: $Prompt.Chat
        Hook: $Prompt.Hook
        Emoji: $Prompt.Emoji
        Format: $Prompt.Format
        Wallet: $Prompt.Wallet
        Sender: $Prompt.Sender
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Prompts` 🪣 table](<../🪣 Prompts/🤵 Broker.Prompts 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Length`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Length ⓕ.md>) [`.IsAtMost`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsAtMost ⓕ.md>)
|
