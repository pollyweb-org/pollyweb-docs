# 🤗 Hello 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Hello@Host` 🅰️ method](<🤗 Hello 🐌 msg.md>)

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

| [Command ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/⌘ Command.md>) | Purpose
|-|-
| 📨 [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>) | Read the incoming [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| 💾 [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | Save the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) into the [Chats 🪣 table](<../../🤗🪣 Host tables/Chats 💬 table/🤗 HostChats 🪣 table.md>)
| 😃 [`TALK`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/TALK 😃/😃 TALK ⌘ cmd.md>) | Start a [Talker 😃](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>)
| 🫡 [`TRUSTS`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>) | Assert a [Trust 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) on 
|