# 🤵 OnBindDetailed 🔔 handler

> About
* Part of the [`Broker.Binds` 🪣 table](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
* Confirms if a user accepts a [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>).

<br/>

## Flow

![alt text](<🤵 OnBindDetailed ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnBindDetailed:

# Rename for readability
- PUT|$Item >> $Bind
    
# Set the Chat context
- CHAT:
    Broker: $.Hosted.Domain
    Chat: $Bind.Chat

# Ask for confirmation
- CONFIRM >> $accepted: 
    Text: |
        Accept bind? 
        - Schema: ´$Bind.SchemaTitle´
        - Vault: ´$Bind.VaultTitle´ 
    Details:
        $Bind.Description

# Save the bind
- IF|$accepted:
    Then: 
        SAVE|$Bind:
            .State: BOUND
    Else:
        SAVE|$Bind:
            .State: REJECTED
```

Uses||
|-|-
[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |  [`CHAT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) [`CONFIRM`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>)  [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds` 🪣 table](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Hosted`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
|

