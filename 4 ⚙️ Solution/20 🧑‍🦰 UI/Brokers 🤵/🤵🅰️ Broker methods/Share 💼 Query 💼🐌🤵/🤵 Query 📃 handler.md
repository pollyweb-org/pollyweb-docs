# 🤵 Query 📃 handler

> Implementation
* Part of the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* Implements both the:
    * [`Share Bind` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Bind 👉🔗💼/🧑‍🦰 Share Bind ⏩ flow.md>) 
    * [`Share Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>)
    * [`Share Token+ID` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token+ID 👉🆔💼/🧑‍🦰 Share Token+ID ⏩ flow.md>)

## Script

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

# Loop the requested schemas.
- FOR|$.Msg.Schemas|$schema:

    # Find a matching Bind or Token
    - EVAL >> $trust:
        FROM $trusted
        MATCH Schema.Is($schema)

    - IF|$trust.AreMany:
    
    Which vault to use?

    # If more than one, ask for selection
    - IF|$trust.AreMany:
        - ONE >> $vault:



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