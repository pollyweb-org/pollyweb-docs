# 🤵 Disclose Bind 📃 script

> Part of [`Query` 📃 handler](<../🤵 Query 📃 handler.md>)

## Script

```yaml
📃 Disclose-Bind:

# Assert the inputs
- ASSERT|.Inputs:
    AllOf: chat, Domain, Bind

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
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>)| [`ASSERT`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
|[{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Function 🐍.md>) | [`.Inputs`](<../../../../../35 💬 Chats/Scripts 📃/📃 functions 🐍/🔩 {.Inputs}.md>)
|[Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>) | [`$.Msg`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|[Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)| [`Disclose@Vault`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>)
|