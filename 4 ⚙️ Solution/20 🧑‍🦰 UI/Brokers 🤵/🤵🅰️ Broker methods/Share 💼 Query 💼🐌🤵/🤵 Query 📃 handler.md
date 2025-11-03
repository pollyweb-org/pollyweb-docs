

```yaml
📃 Query@Handler:

# Verify the message
- VERIFY|$.Msg

# Assert the message
- ASSERT|$.Msg:
    AllOf: Chat, Hook, Schemas
    UUIDs: Chat, Hook
    Lists: Schemas

# Get the Chat
- GET >> $chat:
    Set: BrokerChats
    Key: $.Msg.Chat

# Match with Tokens
- EVAL|.Diff >> $tokens:
    Schema, Issuer
    FROM $chat.Wallet.Tokens
    MATCH Schema.In($.Msg.Schemas)

# Match with Binds
- EVAL|.Diff >> $binds:
    Schema, Vault
    FROM $chat.Wallet.Binds
    MATCH Schema.In($.Msg.Schemas)

Chat: <chat-uuid>
    Hook: <hook-uuid>
    Schemas:
      # either the driver's license,
      - usa.gov/DRIVER-LICENSE:1.0
```