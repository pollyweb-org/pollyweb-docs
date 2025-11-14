# 🤵 Call Introduce 📃 script

> Part of the [`Locate@Broker` 📃 script](<../🤵 Locate 📃 handler.md>)

## Diagram

![alt text](<🤵 Call Introduce ⚙️ uml.png>)

## Script

```yaml
📃 Call-Introduce:

# Verify the required inputs
- ASSERT|$.Inputs:
    AllOf: chat

# Ask Finders to introduce Hosts
- SEND:
    Header:
        To: $chat.Wallet.Finder
        Subject: Introduce@Finder
    Body:
        Chat: $chat.ID
        Host: $chat.Host
        Language: $chat.Wallet.Language
        Reviewer: $chat.Wallet.Reviewer
```

> Continues on the [`Introduce@Finder` 📃 handler](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 📃 handler.md>)


<br/>

| Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Introduce@Finder`](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>)
| 