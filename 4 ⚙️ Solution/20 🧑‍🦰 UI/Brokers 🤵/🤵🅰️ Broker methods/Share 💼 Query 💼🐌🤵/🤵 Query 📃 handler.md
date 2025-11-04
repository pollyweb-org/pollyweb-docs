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
- READ >> $chat:
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
    - EVAL >> $candidates:
        FROM $trusted
        WHERE Schema.Is($schema)

    # Get the tokens first
    - EVAL >> $tokens:
        FROM $candidates
        WHERE Type.Is(TOKEN)

    # Send if it's the only one.
    - IF|$tokens.IsOne:
        - BREAK


    # If more than one, ask for selection
    - IF|$trusts.AreMany:
        - ONE >> $vault:
            Text: Which vault to use?
            Options: 



```

|Users||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`RUN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerTokens` 🪣 table](<../../🤵🪣 Broker tables/Tokens 🎫 table/🤵 BrokerTokens 🪣 table.md>)