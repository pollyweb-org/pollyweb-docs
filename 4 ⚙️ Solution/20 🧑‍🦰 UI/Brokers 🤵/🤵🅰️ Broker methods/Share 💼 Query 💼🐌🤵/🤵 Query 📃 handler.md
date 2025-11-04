

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

# Merge schemas into {Schema, Domain}
- RUN|Merge-Schemas >> $merges:
    $chat
    
# Filter by trusts
- PARALLEL|$merges|$merge:
- SEND >> $trusted:
    Header:
        To: .Hosted.Graph
        Subject: Trusts@Graph
    Body:
        Domain: $.Msg.From
        Role: CONSUMER

    Chat: <chat-uuid>
    Hook: <hook-uuid>
    Schemas:
      # either the driver's license,
      - usa.gov/DRIVER-LICENSE:1.0
```

|Users||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`RUN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerTokens` 🪣 table](<../../🤵🪣 Broker tables/Tokens 🎫 table/🤵 BrokerTokens 🪣 table.md>)