# 🤗 Hello 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Hello@Host` 🅰️ method](<🤗 Hello 🐌 msg.md>)

## Handler

```yaml
📃 Hello@Host:

# Verify the message
- VERIFY|$.Msg

# Check if the Broker is trustworthy
- TRUSTS|$.Msg.From:
    Schema: .HOST/HELLO

# Save the data
- SAVE|HostChats:
    Broker: $.Msg.From
    
    # It's safe to save the Body, 
    #   it's already schema-validated.
    :$.Msg.Body:  

# Start a Chat for the locator
- TALK|$.Msg.Chat|$.Msg.Locator
```

| [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
|-|-
| 📨 [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>) | Read the incoming [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)
| 💾 [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | Save the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) into the [Chats 🪣 table](<../../🤗🪣 Host tables/Chats 💬 table/🤗 HostChats 🪣 table.md>)
| 😃 [`TALK`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/TALK 😃/😃 TALK ⌘ cmd.md>) | Start a [Talker 😃](<../../../../35 💬 Chats/Talkers 😃/😃🤲 Talker helper.md>)
| 🫡 [`TRUSTS`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>) | Assert a [Trust 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) on 
|