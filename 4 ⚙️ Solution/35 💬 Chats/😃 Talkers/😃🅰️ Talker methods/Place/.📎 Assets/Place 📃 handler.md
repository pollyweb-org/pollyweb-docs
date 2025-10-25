# 😃📃 Place handler

> Implements the [`Place@Talker` 🅰️ method](<../🧑‍💻🚀😃 Place.md>)

## Script

```yaml
📃 Place@Talker:

# Verify the domain signature
- VERIFY|$.Msg

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Placeholder, Reason, Chat, Value
    Texts: Placeholder, Reason
    UUIDs: Chat

# Remove the $ from the placeholder
- DIFF >> $placeholder:
    From: $.Msg.Placeholder
    To: $
    
# Verify if the Chat exists
- GET|Chats@Host|$.Msg.Chat >> $chat

# Save the placeholder
- SAVE|Placeholders@Talker:
    Chat: $.Msg.Chat
    Placeholder: $placeholder
    Value: $.Msg.Value
    Reason: $.Msg.Reason
```

Needs||
|-|-
| [Commands ⌘](<../../../😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`DIFF`](<../../../😃⚙️ Talker cmds/...placeholders 🧠/DIFF/DIFF 🆚.md>) [`GET`](<../../../😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) [`SAVE`](<../../../😃⚙️ Talker cmds/...datasets 🪣/SAVE/SAVE 💾 item.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Placeholders` 🪣 table](<../../../😃🪣 Talker tables/😃🪣 Placeholders 🧠 table.md>)
| 