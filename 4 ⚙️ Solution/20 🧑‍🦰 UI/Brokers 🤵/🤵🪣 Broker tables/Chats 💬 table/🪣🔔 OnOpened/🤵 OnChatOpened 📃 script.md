# 🤵 OnChatOpened 📃 script

> Part of the [`Locate@Broker` 📃 script](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 📃 handler.md>)

## Diagram

![alt text](<🤵 OnChatOpened ⚙️ uml.png>)

## Script

```yaml
📃 OnChatOpened:

# Rename for legibility
- PUT|$Item >> $chat

# Ask Finders to introduce Hosts
- SEND:
    Header:
        To: $chat.Wallet.Finder
        Subject: Present@Finder
    Body:
        Chat: $chat.ID
        Host: $chat.Host
        Language: $chat.Wallet.Language
        Reviewer: $chat.Wallet.Reviewer
```


| Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  | [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Present@Finder`](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>)
| 