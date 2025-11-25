# 🎴 Accepted 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Accepted@Issuer` 🅰️ method](<🎴 Accepted 🐌 msg.md>)

## Script

```yaml
📃 Accepted@Issuer:

# Verify the message
- VERIFY|$.Msg

# Get the Hook
- READ >> $hook:
    Set: Talker.Hooks
    Key: $.Msg.Hook
    Assert:
        Broker: $.Msg.From

# Save the Token
- SAVE|Issuer.Tokens:
    $hook: # Add all token properties
    Token: $.Msg.Token
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`REEL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Talker.Hooks`](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃 Talker.Hooks 🪣 table.md>) [`Issuer.Tokens`](<../../🎴🪣 Issuer tables/Tokens 🎫 table/🪣 Tokens/🗄️ Issuer.Tokens 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg` 🧠 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|
