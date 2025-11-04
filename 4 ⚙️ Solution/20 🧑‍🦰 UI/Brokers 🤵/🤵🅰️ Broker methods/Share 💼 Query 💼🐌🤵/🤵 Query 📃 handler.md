

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

# Get the requested schemas from Tokens+Binds
#   and merge them into {Schema, Domain}
- RUN|Merge-Schemas >> $merges:
    $chat
    
# Check for the trusted Schema+Domains
#   and return only the trusted {Schema, Domain}
- RUN|Filter-Schemas >> $trusted:
    $merges

# Prefer to return Tokens if any
- FOR|$trusted|$trust|+Type:

    - EVAL >> $tokens:
        FROM $trusted
        MATCH Type.Is(TOKEN)
    - EVAL >> $binds:
        FROM $trusted
        MATCH Type.Is(TOKEN)

Header:
    From: any-broker.dom
    To: any-broker.dom
    Subject: Disclose@Vault
    
Body:
    Chat: <chat-uuid>
    Consumer: any-coffee-shop.dom
    Language: en-us
    Bind: <bind-uuid>
```

|Users||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`RUN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerTokens` 🪣 table](<../../🤵🪣 Broker tables/Tokens 🎫 table/🤵 BrokerTokens 🪣 table.md>)