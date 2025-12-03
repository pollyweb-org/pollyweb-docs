# 🤵 Status 📃 handler

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Status@Broker` 📨 msg](<🤵 Status 🚀 call.md>).

<br/>

## Diagram

![alt text](<🤵 Status ⚙️ uml.png>)

<br/>

## Script

```yaml
# Verify the Consumer message
- VERIFY|$.Msg

# Get the Token, if ever given to the Consumer
- READ >> $token:
    Set: Broker.Tokens
    Key: 
        Token: $.Msg.Token
        Issuer: $.Msg.Issuer
    Assert: 
        Consumers.Contains: $.Msg.From

# Check if the issuer still trusts the Consumer
- TRUSTS:
    Truster: $token.Issuer
    Trusted: $.Msg.From
    Schema: $token.Schema
    Role: CONSUMER

# Return the Status
- RETURN:
    Status: $token.Status
    Starting: $token.Starting
    Ending: $token.Ending
    Locator: $token.Locator
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`TRUSTS`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>)  [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>) |
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Tokens`](<../../🤵🪣 Broker tables/Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>) |