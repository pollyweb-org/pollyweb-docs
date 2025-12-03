# 🤵 OnDomainInserted 📃 handler

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to the insertion of a new [`Domain`](<../🪣 Domains/🤵 Broker.Domains 🪣 table.md>) item.

<br/>

## Diagram

![alt text](<🤵 OnDomainInserted ⚙️ uml.png>)

<br/>

## Script 

```yaml
📃 OnDomainInserted:

# Assert the Domain
- ASSERT|$Domain:
    AllOf: Name, Wallet
    Texts: Name
    UUIDs: Wallet

# Get the Domain details from the Graph
- TRANSLATE >> $domain:
    Domain: $Domain.Name
    To: $Domain.Wallet.Language

# Save the Domain info
- SAVE|$Domain:
    Language: $Domain.Wallet.Language
    HostTitle: $domain.Title
    Description: $domain.Description
    SmallIcon: $domain.SmallIcon
    BigIcon: $domain.BigIcon
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Domains`](<../🪣 Domains/🤵 Broker.Domains 🪣 table.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) |  [`$.Hosted`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`About@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 About/🕸 About 🚀 call.md>) 
|