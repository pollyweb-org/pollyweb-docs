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
- GET >> $chat:
    Set: HostChats
    Key: $.Msg.Chat

# Save the placeholder
- SAVE|TalkerHolders:
    Chat: $.Msg.Chat
    Placeholder: $.Msg.Placeholder.Diff($)
    Value: $.Msg.Value
    Reason: $.Msg.Reason
```

Needs||
|-|-
| [Commands ⌘](<../../😃⚙️ Talker cmds/...commands ⌘/Command ⌘/⌘ Command.md>) | [`DIFF`](<../../😃⚙️ Talker cmds/...functions 🐍/🔩 {.Diff}.md>) [`GET`](<../../😃⚙️ Talker cmds/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`SAVE`](<../../😃⚙️ Talker cmds/...datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`HostChats` 🪣 table](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🪣 Host tables/Chats 💬 table/🤗 HostChats 🪣 table.md>) [`TalkerHolders` 🪣 table](<../../😃🪣 Talker tables/😃🪣 TalkerHolders 🧠 table.md>)
| [{Functions} 🐍](<../../😃⚙️ Talker cmds/...functions 🐍/{Function} 🐍.md>) | [`{.Diff}`](<../../😃⚙️ Talker cmds/...functions 🐍/🔩 {.Diff}.md>)
| 