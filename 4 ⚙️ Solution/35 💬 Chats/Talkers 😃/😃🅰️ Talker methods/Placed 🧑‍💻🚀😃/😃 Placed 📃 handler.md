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
    AllOf: Chat, Holder
    UUIDs: Chat
    Texts: Holder

# Get the holder
- GET >> $holder:
    Set: TalkerHolders
    Key: 
        Chat: $.Msg.Chat
        Holder: $.Msg.Holder

# Return the value
- RETURN:
    $holder.Value
```

Needs||
|-|-
| [Commands ⌘](<../../../Scripts 📃/📃 basics/Command ⌘/⌘ Command.md>) | [`GET`](<../../../Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`RETURN`](<../../../Scripts 📃/📃 control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`TalkerHolders` 🪣 table](<../../😃🪣 Talker tables/😃🪣 TalkerHolders 🧠 table.md>)
| [Holders 🧠](<../../../Scripts 📃/📃 holders 🧠/$Holder 🧠.md>) | [`$.Msg`](<../../../Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|