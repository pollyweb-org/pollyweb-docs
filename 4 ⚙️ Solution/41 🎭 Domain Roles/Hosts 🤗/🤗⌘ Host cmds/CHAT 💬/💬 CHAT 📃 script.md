<!-- TODO -->

# 😃📃 .CHAT 💬 script

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    * that implements the [`CHAT` 💬 command](<💬 CHAT ⌘ cmd.md>) 
    * by setting the [`$.Chat` 💬 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>).

# Diagram

![alt text](<💬 CHAT ⚙️ uml.png>)

## How to run

```yaml
# Existing chat
RUN|.CHAT:
    Broker: any-broker.dom
    Chat: <chat-uuid>
```

## Script

```yaml
📃 .CHAT:

# Assert the required fields
- ASSERT|$.Inputs:
    AllOf: Broker, Chat
    Texts: Broker
    UUIDs: Chat

# Get the details from the Broker
- SEND >> $details:
    Header:
        To: $Broker
        Subject: Chat@Broker
    Body:
        Chat: $Chat

# Get the Chat item, if exists
- READ >> $chat:
    Set: Host.Chats
    Key: 
        Broker: $Broker
        Chat: $Chat
    Default: 

# Update the item details
- SAVE|$chat >> $chat:
    $details

# Update the system holder
- SET|$.Chat:
    $chat
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SET`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>)
|[Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`HostChats`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🪣 Host tables/Chats 💬 table/🪣 Chats/🤗 Host.Chats 🪣 table.md>)
[Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) [`$.Inputs`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
|

## FAQ

1. **Why update instead of overwriting?**

    There's an `Emoji` property managed by the [`EMOJI`](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/😶⌘ EMOJI cmd.md>) command that needs to survive concurrent changes.

    ---
    <br/>