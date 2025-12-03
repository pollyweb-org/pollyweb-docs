# 🤵 Frontend@Broker 📃 handler

> About
* Part of [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Frontend@Broker` 📨 msg](<🤵 Frontend 🚀 call.md>).
* Reads the [`Broker.Frontend` 🪣 table](<../../🤵🪣 Broker tables/Frontend 📱 table/🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>)

<br/>

## Flow

![alt text](<🤵 Frontend ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Frontend@Broker:

# Assert the message
- ASSERT|$.Msg:
    UUIDs: From
    Lists: Chats, Binds, Tokens, Domains, Schemas
    Enums: Lists
    Lists.IsIn: Chats, Binds, Tokens, Domains, Schemas

# Get the frontend item
- READ >> $frontend:
    Set: Broker.Frontend
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $frontend.PublicKey

# Filter the items of each list
- PUT|$frontend >> $return:
    Chats: Chats.Format($.Msg.Chats) 
    Binds: Binds.Format($.Msg.Binds) 
    Tokens: Tokens.Format($.Msg.Tokens)
    Domains: Domains.Format($.Msg.Domains)
    Schemas: Schemas.Format($.Msg.Schemas)

# Filter the lists in the frontend
- PUT|$return >> $return:
    $return.Evaluate($.Msg.Lists)

# Always add the wallet data
- SET|$return:
    Wallet: 
        Language: $frontend.Wallet.Language

# Return the frontend data
- RETURN:
    $return    
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|  [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Frontend`](<../../🤵🪣 Broker tables/Frontend 📱 table/🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>)
|[Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|