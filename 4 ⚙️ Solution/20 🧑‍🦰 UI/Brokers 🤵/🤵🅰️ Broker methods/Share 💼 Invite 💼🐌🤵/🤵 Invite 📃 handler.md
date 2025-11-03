# 🤵 Invite 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that implements the [`Invite@Broker` 🅰️ method](<🤵 Invite 🐌 msg.md>)

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
- GET >> $chat:
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