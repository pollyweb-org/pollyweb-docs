# 🤵📃 Introduce@Broker


## Script

```yaml
📃 Call Introduce:

# Verify the required inputs
- ASSERT|$.Inputs:
    AllOf: locator, chat, wallet

# Ask Finders to introduce Hosts
- SEND:
    Header:
        To: $:wallet.Finder
        Subject: Introduce@Finder
    Body:
        Chat: $:chat.Chat
        Host: $:locator.Host
        Language: $:wallet.Language
        Reviewer: $:wallet.Reviewer
```

> Continues on the [`Introduce@Finder` 📃 handler](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Introduce 🤵🐌🔎/🔎 Introduce 📃 handler.md>)


<br/>

| Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>)  | [`ASSERT`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>) | [`$.Inputs`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Inputs ▶️/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Introduce@Finder`](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Introduce 🤵🐌🔎/🔎 Introduce 🐌 msg.md>)
| 