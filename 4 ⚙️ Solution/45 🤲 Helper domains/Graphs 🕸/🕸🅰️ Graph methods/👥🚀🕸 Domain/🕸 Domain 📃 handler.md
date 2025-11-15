# 🕸 Domain 📃 handler

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Domain@Graph` 🅰️ method](<🕸 Domain 📃 handler.md>)

## Script

```yaml
📃 Domain@Graph:

# Assert the message
- ASSERT|$.Msg:
    AllOf: Domain
    Texts: Domain

# Verify the message
- VERIFY|$.Msg

# Read the domain
- READ >> $domain:
    Set: Graph.Domains
    Key: $.Msg.Domain
    Get: 
        Domain, Feedback, 
        Title, Description, 
        SmallIcon, BigIcon

# Return the output
- RETURN:
    $domain
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)| [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PUT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|[Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>)|[`Graph.Domains`](<../../🕸🪣 Graph tables/Domains 👥/🕸 Graph.Domains 🪣 table.md>)
|[Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)|[`$.Msg` 🧠 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|