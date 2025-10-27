# 😃📃 Place handler

> Implements the [`Place@Talker` 🅰️ method](<😃 Place 🚀 request.md>)

## Flow

![alt text](<😃 Place ⚙️ uml.png>)

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
    
# Verify if the Chat exists
- GET|Chats@Host|$.Msg.Chat >> $chat

# Save the placeholder
- SAVE|Placeholders@Talker:
    Chat: $.Msg.Chat
    Placeholder: $.Msg.Placeholder.Remove($)
    Value: $.Msg.Value
    Reason: $.Msg.Reason
```

Needs||
|-|-
| [Commands ⌘](<../../😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`DIFF`](<../../😃⚙️ Talker cmds/...functions 🐍/🔩 {.Diff}.md>) [`GET`](<../../😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) [`SAVE`](<../../😃⚙️ Talker cmds/...datasets 🪣/SAVE/SAVE 💾 item.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Placeholders` 🪣 table](<../../😃🪣 Talker tables/😃🪣 Holders 🧠 table.md>)
| [{Functions} 🐍](<../../😃⚙️ Talker cmds/...functions 🐍/{Function} 🐍.md>) | [`{.Diff}`](<../../😃⚙️ Talker cmds/...functions 🐍/🔩 {.Diff}.md>)
| 