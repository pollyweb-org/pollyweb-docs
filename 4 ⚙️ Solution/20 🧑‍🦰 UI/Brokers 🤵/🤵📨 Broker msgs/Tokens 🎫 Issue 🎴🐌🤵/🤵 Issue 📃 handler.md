# 🤵 Issue 📃 handler

> About
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Issue@Broker` 🐌 msg](<🤵 Issue 🐌 msg.md>)
* Part of the [🧑‍🦰 `Save Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>).
* Part of the [🤵 `Broker.Tokens.Issue` ⏩ flow](<../../🤵🪣 Broker tables/Tokens 🎫 table/🪣🧱 10 Issue ⏩ flow/🤵 Broker.Tokens.Issue ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 Issue ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 Issue@Broker:

# Verify the Issuer's message
- VERIFY|$.Msg

# Assert the required inputs
- ASSERT|$.Msg:
    AllOf: Chat, Token, Schema
    UUIDs: Chat, Token
    Texts: Schema
    Times: Starts, Expires
    Starts.IsBefore: Expires
    Expires.IsAfter: .Now

# Get the Chat
- READ >> $chat:
    Set: Broker.Chats
    Key: $.Msg.Chat
    Assert:
        .State: ACTIVE

# Only allow offers from the Host
- ASSERT|$.Msg:
    From: $chat.Host

# Save the Offer
- SAVE|Broker.Tokens:
    .State: OFFERED
    Status: ACTIVE
    Token: $.Msg.Token
    Issuer: $.Msg.From
    Schema: $.Msg.Schema
    Starts: $.Msg.Starts
    Expires: $.Msg.Expires
    Wallet: $chat.Wallet.ID
    Chat: $chat.ID
    
    # Set the cache expiration
    .Delete: 
        .Lower:
            $.Msg.Expires,
            Now.Add(30 days)
```

Uses||
-|-
[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Tokens`](<../../🤵🪣 Broker tables/Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Add`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ.md>) [`.IsBefore`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsBefore ⓕ.md>) [`.IsAfter`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsAfter ⓕ.md>) [`.Lower`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Lower ⓕ.md>) [`.Now`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Now ⓕ.md>) 
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>) 
|