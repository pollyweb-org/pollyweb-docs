# 🤵 OnChatInserted 📃 handler

> Flow
* Triggered by [`Locate@Broker` 🅰️ method](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)

## Diagram

![alt text](<🤵 OnChatInserted ⚙️ uml.png>)

## Script 

```yaml
📃 OnChatInserted:

# Get the Host details from the Graph
- SEND >> $domain:
    Header:
        To: $.Hosted.Graph
        Subject: About@Graph
    Body:
        Domain: $Chat.Host
        Language: $Chat.Language

# Save the Host info
- SAVE|$Chat:
    .State: DETAILED
    HostTitle: $domain.Title
    Description: $domain.Description
    SmallIcon: $domain.SmallIcon
    BigIcon: $domain.BigIcon
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |  [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) |  [`$.Hosted`](<../../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`About@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 About/🕸 About 🚀 call.md>) 
|