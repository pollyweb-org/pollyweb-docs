# 🤵 Save Host 📃 script

> Part of the [`Assess@Broker` 📃 script](<../🤵 Assess 📃 handler.md>)

## Diagram

![alt text](<🤵 Save Host ⚙️ uml.png>)

## Script 

```yaml
📃 Save-Host:

# Verify the required inputs
- ASSERT|$.Inputs:
    AllOf: locator

# Get the Host details from the Graph
- SEND >> $domain:
    Header:
        To: $.Hosted.Graph
        Subject: Identity@Graph
    Body:
        Domain: $locator.Host

# Save the Host info
- SAVE|Broker.Domains:
    Domain: $domain.Domain
    Domain$: $domain.Name
    SmallIcon: $domain.SmallIcon
    BigIcon: $domain.BigIcon
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Domains`](<../../../🤵🪣 Broker tables/Domains 👥 table/🤵 Broker.Domains 🪣 table.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>) [`$.Hosted`](<../../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Identity@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>) 
|