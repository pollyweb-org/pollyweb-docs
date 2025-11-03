

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

# Merge all
- EVAL|$tokens +> $merges:
    Schema: Schema
    Domain: Issuers
- EVAL|$binds +> $merges:
    Schema: Schema
    Domain: Vault
    
# Filter by trusts
- PARALLEL|$merges
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
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerTokens` 🪣 table](<../../🤵🪣 Broker tables/Tokens 🎫 table/🤵 BrokerTokens 🪣 table.md>)