# 🤵📃 Introduce@Broker


<br/> 

## Script

```yaml
📃 Introduced@Broker:

# Verify the required inputs
- ASSERT|$.Inputs:
    AllOf: Locator, Chat, Wallet

# Ask Finders to introduce Hosts
- SEND:
    Header:
        To: $:Wallet.Finder
        Subject: Introduce@Finder
    Body:
        Chat: $:Chat.Chat
        Host: $:Locator.Host
        Language: $:Wallet.Language
        Reviewer: $:Wallet.Reviewer
```

> Continues on the [`Introduce@Finder` 📃 handler](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Introduce 🤵🐌🔎/🔎 Introduce 📃 handler.md>)


<br/>

| Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>)  | [`ASSERT`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>) | [`$.Inputs`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Inputs ▶️/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Introduce@Finder` 🅰️ method](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Introduce 🤵🐌🔎/🔎 Introduce 🐌 msg.md>)
| 