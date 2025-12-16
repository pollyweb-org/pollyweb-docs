# 🤵 OnChatResolved 🔔 handler

> Part of the [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 OnChatResolved ⚙️ uml.png>)

## Script 

```yaml
📃 OnChatResolved:

# Assert the Chat
- ASSERT $Chat:
    AllOf: Host

# Get the Host details from the Graph
- GRAPH About >> $domain:
    Domain: $Chat.Host.Require
    Language: $Chat.Wallet.Language.Require

# Save the Host info
- SAVE $Chat:
    STATE: DETAILED
    Language: $Chat.Wallet.Language.Require
    HostTitle: $domain.Title
    Description: $domain.Description
    SmallIcon: $domain.SmallIcon
    BigIcon: $domain.BigIcon
    HostEmoji: $domain.Emoji
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`GRAPH`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/GRAPH 🕸/🕸 GRAPH ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Require`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Require ⓕ.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`About@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 About/🕸 About 🚀 call.md>) 
|