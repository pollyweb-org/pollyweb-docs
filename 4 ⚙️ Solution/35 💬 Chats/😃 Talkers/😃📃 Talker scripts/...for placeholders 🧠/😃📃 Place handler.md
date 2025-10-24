# 😃📃 Place handler

> Implements the [`Place@Talker` 🅰️ method](<../../😃🅰️ Talker methods/🧑‍💻🚀😃 Place.md>)

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