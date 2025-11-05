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
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`RETURN`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerBinds`](<../../../🤵🪣 Broker tables/Binds 🔗 table/🤵 BrokerBinds 🪣 table.md>) [`BrokerTokens`](<../../../🤵🪣 Broker tables/Tokens 🎫 table/🤵 BrokerTokens 🪣 table.md>)
| [Holder 🧠](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>)  | [`$.Msg`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|