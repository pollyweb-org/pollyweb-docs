```yaml
# Verify the message
- VERIFY|$.Msg

# Assert the message
- ASSERT|$.Msg:
    AllOf: Chat, Emoji
    UUIDs: Chat
    Texts: Emoji
    Emoji.Length.IsAtMost: 1

# Get the Chatter
- READ:
    Set: Broker.Chatters
    Key:
        Chat: $.Msg.Chat
        Domain: $.Msg.From

# Assert the Chatter role
- ASSERT|$chatter:
    Role.In(HOST, HELPER)

# Assert the Chat is active
- ASSERT|$chatter.Chat:
    .State: ACTIVE

# Update the Chat emoji
- SAVE|$chatter.Chat:
    Emoji: $.Msg.Emoji
```