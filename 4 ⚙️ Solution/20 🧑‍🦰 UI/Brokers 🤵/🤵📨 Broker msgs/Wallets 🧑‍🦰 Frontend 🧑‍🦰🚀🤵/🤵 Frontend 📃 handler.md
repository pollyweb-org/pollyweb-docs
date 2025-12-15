# 🤵 Frontend@Broker 📃 handler

> About
* Part of [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Frontend@Broker` 🚀 call](<🤵 Frontend 🚀 call.md>).
* Reads the [`Broker.Frontend` 🪣 table](<../../🤵🪣 Broker tables/Frontend 📱 table/🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>)

<br/>

## Flow

![alt text](<🤵 Frontend ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Frontend@Broker:

# Assert the message
- ASSERT $.Msg:
    UUIDs: From
    Enums: Sets
    Sets.IsIn: Chats, Binds, Tokens, Domains, Schemas

# Get the frontend item
- READ >> $frontend:
    Set: Broker.Frontend
    Key: $.Msg.From

# Verify the signature
- VERIFY $.Msg:
    Key: $frontend.PublicKey

# Filter the lists
- PUT >> $return:
    $frontend.Format: $.Msg.Sets

# Filter the fields and items of each list
- FOR $return.Keys >> $key:
    - SET $return.{$key}:
        .Format: $.Msg.Outputs.{$key}
        .Filter: $.Msg.Asserts.{$key}

# Always add the wallet data
- SET $return:
    Wallet: 
        Language: $frontend.Wallet.Language

# Return the frontend data
- RETURN:
    $return    
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)
|  [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Frontend`](<../../🤵🪣 Broker tables/Frontend 📱 table/🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`Filter`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/FILTER 🔽/🔽 FILTER 📃 script.md>) [`.Format`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Format ⓕ.md>) [`.Key`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Key ⓕ.md>) [`.Keys`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Keys ⓕ.md>) [`.StartsWith`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/StartsWith ⓕ.md>) [`.Where`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Where ⓕ.md>)
|[Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|