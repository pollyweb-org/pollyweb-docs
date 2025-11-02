# 🤵 Call Introduce 📃 script

> Part of the [`Assess@Broker` 📃 script](<🤵 Assess 📃 handler.md>)

## Script

```yaml
📃 Call-Introduce:

# Verify the required inputs
- ASSERT|$.Inputs:
    AllOf: chat

# Ask Finders to introduce Hosts
- SEND:
    Header:
        To: $:chat.Wallet.Finder
        Subject: Introduce@Finder
    Body:
        Chat: $:chat.ID
        Host: $:chat.Host
        Language: $:chat.Wallet.Language
        Reviewer: $:chat.Wallet.Reviewer
```

> Continues on the [`Introduce@Finder` 📃 handler](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Introduce 🤵🐌🔎/🔎 Introduce 📃 handler.md>)


<br/>

| Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>)  | [`ASSERT`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>) | [`$.Inputs`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Inputs ▶️/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Introduce@Finder`](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Introduce 🤵🐌🔎/🔎 Introduce 🐌 msg.md>)
| 