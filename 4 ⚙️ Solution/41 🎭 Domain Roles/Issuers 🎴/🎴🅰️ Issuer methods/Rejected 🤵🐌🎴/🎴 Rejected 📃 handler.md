# 🎴 Rejected 📃 handler

## Script

```yaml
📃 Rejected@Issuer:

# Get the Hook
- READ >> $hook:
    Set: Talker.Hooks
    Key: $.Msg.Hook

# Assert if it's the right Broker
- ASSERT|$.Msg:
    From: $hook.Broker

# Save the Token
- SAVE|Issuer.Tokens:
    Token: $.Msg.Token
    $hook:

# Continue the Talker
- REEL|$hook:
    $token
```

| [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
|-|-
| 🧲 [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) | Get the [Hook 🪣](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃 Talker.Hooks 🪣 table.md>) from [`Offer@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
| 🚦 [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) | Assert if it's the right [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) 
| 🧮 [`CALL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CALL 🧮/🧮 CALL ⌘ cmd.md>) | Get the [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) data from the hook
| 💾 [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | Save the [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) to the [Tokens 🪣 table](<../../🎴🪣 Issuer tables/Tokens 🎫 table/🪣 Tokens/🗄️ IssuerTokens 🪣 table.md>)
| 🎣 [`REEL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>) | Continue the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
| 
