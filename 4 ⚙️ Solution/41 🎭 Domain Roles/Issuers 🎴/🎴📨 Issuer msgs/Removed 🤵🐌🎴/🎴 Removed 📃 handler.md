# 🎴 Removed 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Removed@Issuer` 🐌 msg](<🎴 Removed 🐌 msg.md>)

<br/>

## Script

```yaml
📃 Removed@Issuer:

# Assert the message
- ASSERT $.Msg:
    AllOf: Token
    UUIDs: Token

# Verify the message
- VERIFY $.Msg

# Get the Token
- READ >> $token:
    Set: Issuer.Tokens
    Key: $.Msg.Token
    Assert: 
        Broker: $.Msg.From

# Save the Token
- SAVE $token:
    STATE: REMOVED
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)  [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>) 
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) |  [`Issuer.Tokens`](<../../🎴🪣 Issuer tables/Tokens 🎫 table/🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|
