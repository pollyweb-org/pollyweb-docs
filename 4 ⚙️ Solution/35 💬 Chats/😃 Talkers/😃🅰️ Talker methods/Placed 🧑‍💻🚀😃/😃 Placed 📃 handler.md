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

# Get the placeholder
- GET >> $holder:
    Set: TalkerHolders
    Key: 
        Chat: $.Msg.Chat
        Holder: $.Msg.Holder

- RETURN:
    $holder.Value
```

Needs||
|-|-
| [Commands ⌘](<../../😃⚙️ Talker cmds/...commands ⌘/Command ⌘/⌘ Command.md>) | [`GET`](<../../😃⚙️ Talker cmds/...datasets 🪣/GET ⏬/⏬ GET ⌘ cmd.md>) [`RETURN`](<../../😃⚙️ Talker cmds/...control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../😃⚙️ Talker cmds/...datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | {{TalkerHolders}}
| [Placeholders 🧠](<../../😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Msg`](<../../😃⚙️ Talker cmds/...messages 📨/$.Msg 📨.md>)
|