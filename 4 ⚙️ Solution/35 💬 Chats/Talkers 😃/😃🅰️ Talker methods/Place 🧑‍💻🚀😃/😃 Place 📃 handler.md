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
    AllOf: Holder, Reason, Chat, Value
    Texts: Holder, Reason
    UUIDs: Chat
    
# Verify if the Chat exists
- GET >> $chat:
    Set: HostChats
    Key: $.Msg.Chat

# Save the holder
- SAVE|TalkerHolders:
    Chat: $.Msg.Chat
    Holder: $.Msg.Holder.Diff($)
    Value: $.Msg.Value
    Reason: $.Msg.Reason
```

Needs||
|-|-
| [Commands ⌘](<../../../Scripts 📃/...commands ⌘/Command ⌘/⌘ Command.md>) | [`DIFF`](<../../😃⚙️ Talker cmds/...functions 🐍/🔩 {.Diff}.md>) [`GET`](<../../../Scripts 📃/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`SAVE`](<../../../Scripts 📃/...datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`HostChats` 🪣 table](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🪣 Host tables/Chats 💬 table/🤗 HostChats 🪣 table.md>) [`TalkerHolders` 🪣 table](<../../😃🪣 Talker tables/😃🪣 TalkerHolders 🧠 table.md>)
| [{Functions} 🐍](<../../😃⚙️ Talker cmds/...functions 🐍/{Function} 🐍.md>) | [`{.Diff}`](<../../😃⚙️ Talker cmds/...functions 🐍/🔩 {.Diff}.md>)
| 