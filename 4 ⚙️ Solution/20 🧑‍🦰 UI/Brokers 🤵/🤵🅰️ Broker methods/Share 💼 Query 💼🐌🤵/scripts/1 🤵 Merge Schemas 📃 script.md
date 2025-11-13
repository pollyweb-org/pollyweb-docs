# 🤵 Merge Schemas 📃 script

> Part of the [`Query` 📃 handler](<../🤵 Query 📃 handler.md>)

> Returns `{Schema, Domain}[]`

## Script 

```yaml
📃 Merge-Schemas:

# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: chat

# Get the tokens for the schema
- SELECT >> $tokens:
    All: 
        ID:
        Schema:
        Schema$:
        Domain: Issuer
        Type: SCHEMA
    From: $chat.Wallet.Tokens
    Where: Schema.IsIn($.Msg.Schemas)
    
# Get the binds for the schema
- SELECT >> $binds:
    All: 
        ID:
        Schema: 
        Schema$:
        Domain: Vault
        Type: BIND
    From: $chat.Wallet.Binds
    Where: Schema.IsIn($.Msg.Schemas)

# Match with Tokens and Binds
- DISTINCT >> $merges:
    $binds
    $tokens

# Return the merges
- RETURN|$merges
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CALL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerBinds`](<../../../🤵🪣 Broker tables/Binds 🔗 table/🤵 Broker.Binds 🪣 table.md>) [`BrokerTokens`](<../../../🤵🪣 Broker tables/Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
| [Holder 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)  | [`$.Msg`](<../../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|