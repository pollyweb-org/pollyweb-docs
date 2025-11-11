<!-- TODO -->

# 😃📃 .CHAT 💬 script

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    * that implements the [`CHAT` 💬 command](<💬 CHAT ⌘ cmd.md>) 
    * by setting the [`$.Chat` 💬 holder](<../../../📃 Holders 🧠/🧠 System holders/$.Chat 💬/💬 $.Chat 🧠 holder.md>).

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
    - AllOf: Broker, Chat
    - Texts: Broker
    - UUIDs: Chat

# Get the details from the Broker
- SEND >> $details:
    Header:
        To: $Broker
        Subject: Chat@Broker
    Body:
        Chat: $Chat

# Get the table item, if exists
- READ >> $chat:
    Set: HostChats
    Key: 
        Broker: $Broker
        Chat: $Chat
    Default: 

# Update the item details
- SAVE|$chat >> $chat:
    :$details:

# Update the system holder
- SET|$.Chat:
    :$chat:
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SAVE`](<../../⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SET`](<../SET ↘️/↘️ SET ⌘ cmd.md>)
|[Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`HostChats`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🪣 Host tables/Chats 💬 table/🤗 HostChats 🪣 table.md>)
[Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat` 🧠 holder](<../../../📃 Holders 🧠/🧠 System holders/$.Chat 💬/💬 $.Chat 🧠 holder.md>)
|