# 🤵 Revise📃 handler

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Revise@Broker` 🐌 msg](<🤵 Revise 🐌 msg.md>)

<br/>

## Diagram

![alt text](<🤵 Revise ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Revise@Broker:

# Verify the Issuer's message
- VERIFY $.Msg

# Assert the required inputs
- ASSERT $.Msg:
    AllOf: Token, Status, Starts
    UUIDs: Token
    Texts: Status, Locator
    Times: Starts, Expires
    Expires.IsAfter: Starts
    Status.In: ACTIVE, REVOKED, SUSPENDED, EXPIRED

# Get the Token
- READ >> $token:
    Set: Broker.Tokens
    Key: 
        Issuer: $.Msg.From
        Token: $.Msg.Token

# Save the revision
- SAVE Broker.Tokens:
    Status: $.Msg.Status
    Starts: $.Msg.Starts
    Expires: $.Msg.Expires
    Locator: $.Msg.Locator
```

Uses||
-|-
[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Tokens`](<../../🤵🪣 Broker tables/Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) |  [`.IsAfter`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsAfter ⓕ.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) |  [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>) 
|