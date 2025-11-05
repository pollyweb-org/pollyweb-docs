# 🤵 Invite 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Invite@Broker` 🅰️ method](<🤵 Invite 🐌 msg.md>)

## Flow

![alt text](<🤵 Invite ⚙️ uml.png>)

## Script

```yaml
📃 Invite@Broker:

# Verify the message
- VERIFY|$.Msg

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Host, Chat, Helper
    Texts: Host
    UUIDs: Chat, Helper

# Get the chat
- READ >> $chat:
    Set: BrokerChats
    Key: $.Msg.Chat

# Assert it's the host
- ASSERT|$chat:
    Host: $.Msg.From

# Get the Helper title
- SEND >> $translation:
    Header:
        To: $.Hosted.Graph
        Subject: Translate@Graph
    Body:
        Language: $chat.Wallet.Language
        Domain: $.Msg.Helper

# Confirm with the Wallet
- CONFIRM:
    Text: Allow {$translation.Domain}?

# Add the participant to the chat
- SAVE|BrokerChatters:
    Chat: $.Msg.Chat
    Domain: $.Msg.Helper
    Role: HELPER

# Send the Invite to the Helper
- SEND:
    Header:
        To: $.Msg.Helper
        Subject: Invited@Helper
    Body:
        Chat: $.Msg.Chat
        Inviter: $.Msg.From
        Schema: $.Msg.Schema
        Hook: $.Msg.Hook
        Parameters: $.Msg.Parameters        
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CONFIRM`](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ 📃 script.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|[Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerChats` 🪣 table](<../../🤵🪣 Broker tables/Chats 💬 table/🤵 BrokerChats 🪣 table.md>) <br/> [`BrokerChatters` 🪣 table](<../../🤵🪣 Broker tables/Chatters 👥 table/🤵 BrokerChatters 🪣 table.md>)
|[Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Invited@Helper` 🅰️ method](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>) <br/> [`Translate@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|