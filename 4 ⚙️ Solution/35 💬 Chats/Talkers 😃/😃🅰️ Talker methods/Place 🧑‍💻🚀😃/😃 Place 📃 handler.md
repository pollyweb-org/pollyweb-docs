<!-- TODO: Review the code, now with Hook instead of chat -->
# 😃📃 Place handler

> Implements the [`Place@Talker` 🅰️ method](<😃 Place 🚀 call.md>)

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
- READ >> $chat:
    Set: Host.Chats
    Key: $.Msg.Chat

# Save the holder
- SAVE|Talker.Holders:
    Chat: $.Msg.Chat
    Holder: $.Msg.Holder.Diff($)
    Value: $.Msg.Value
    Reason: $.Msg.Reason
```

Uses||
|-|-
| [Commands ⌘](<../../../Scripts 📃/Command ⌘.md>) | [`DIFF`](<../../../../37 Scripts 📃/📃 Holders 🧠/Any 📚 holders/Diff ⓕ.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`HostChats` 🪣 table](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🪣 Host tables/Chats 💬 table/🤗 Host.Chats 🪣 table.md>) [`TalkerHolders` 🪣 table](<../../😃🪣 Talker tables/😃 Talker.Holders 🪣 table.md>)
| [{Functions} 🐍](<../../../Scripts 📃/Function 🐍.md>) | [`{.Diff}`](<../../../../37 Scripts 📃/📃 Holders 🧠/Any 📚 holders/Diff ⓕ.md>)
| 