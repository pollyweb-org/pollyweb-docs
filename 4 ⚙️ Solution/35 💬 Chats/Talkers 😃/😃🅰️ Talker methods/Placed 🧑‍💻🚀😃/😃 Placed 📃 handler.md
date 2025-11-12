<!-- TODO: Review the code, now with Hook instead of chat -->
<!-- TODO -->

# 😃📃 Placed handler

> Implements the [`Placed@Talker` 🅰️ method](<😃 Placed 🚀 request.md>)


## Flow

![alt text](<😃 Placed ⚙️ uml.png>)

## Script

```yaml
📃 Placed@Talker:

# Verify the domain signature
- VERIFY|$.Msg

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Hook, Holder
    UUIDs: Hook
    Texts: Holder

# Get the holder
- READ >> $holder:
    Set: Talker.Holders
    Key: 
        Chat: $.Msg.Chat
        Holder: $.Msg.Holder

# Return the value
- RETURN:
    $holder.Value
```

Uses||
|-|-
| [Commands ⌘](<../../../Scripts 📃/Command ⌘.md>) | [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`TalkerHolders` 🪣 table](<../../😃🪣 Talker tables/😃 Talker.Holders 🪣 table.md>)
| [Holders 🧠](<../../../Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|