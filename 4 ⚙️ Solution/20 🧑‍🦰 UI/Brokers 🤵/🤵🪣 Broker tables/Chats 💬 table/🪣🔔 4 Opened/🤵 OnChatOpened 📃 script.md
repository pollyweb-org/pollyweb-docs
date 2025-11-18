# 🤵 OnChatOpened 📃 script

## Diagram

![alt text](<🤵 OnChatOpened ⚙️ uml.png>)

## Script

```yaml
📃 OnChatOpened:

# Rename for legibility
- PUT|$Item >> $chat

# Add the finder to the chat
- SAVE|Broker.Chatters:
    Chat: $chat.ID
    Domain: $chat.Wallet.Finder
```


| Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  | [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chats`](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Broker.Chatters`](<../../Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) 
|