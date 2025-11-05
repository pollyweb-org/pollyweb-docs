# 🤵 Send Bind 📃 script

> Part of [`Query` 📃 handler](<../🤵 Query 📃 handler.md>)

## Script

```yaml
📃 Send-Bind:

# Assert the inputs
- ASSERT|.Inputs:
    AllOf: chat, Domain, Bind


# If more than one, ask for selection
- IF|$tokens.AreMany:
    - TRANSLATE
    - ONE >> $vault:
        Text: Which vault to use?
        Options: 

# Send the message to the vault
- SEND:
    Header:
        From: $Domain
        Subject: Disclose@Vault
        
    Body:
        Chat: $chat.ID
        Consumer: $.Msg.From
        Language: $chat.Language
        Bind: $Bind
```

Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)| [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
|[{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Inputs`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Inputs}.md>)
|[Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|[Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)| [`Disclose@Vault`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>)
|