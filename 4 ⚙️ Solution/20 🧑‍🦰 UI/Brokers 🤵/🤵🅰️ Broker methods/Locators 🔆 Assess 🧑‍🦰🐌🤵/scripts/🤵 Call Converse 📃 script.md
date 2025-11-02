# 🤵📃 Converse 💬

> Part of the [`Assess@Broker` 📃 script](<../🤵 Assess 📃 handler.md>)


## Script

```yaml
📃 Call-Converse:

# Assert the inputs
- ASSERT|.Inputs:
    AllOf: chat

# Open the Chat in the Wallet app
- SEND:
    Header:
        To: $:chat.Wallet.Notifier
        Subject: Converse@Notifier
    Body:
        Wallet: $:chat.Wallet
        Hook: $.Msg.Hook
        Chat: $:chat.ID
        PrivateKey: $:chat.PrivateKey
        Host: $:chat.Host.Name
        Host$: $:chat.Host.Title
        SmallIcon: $:chat.Host.SmallIcon
        BigIcon: $:chat.Host.BigIcon

# Update the Chats
- RUN|Update-Chats:
    wallet: $:chat.Wallet
```

|Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`GET`](<../../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`KEYS`](<../../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/KEYS 🔑/🔑 KEYS ⌘ cmd.md>) [`SAVE`](<../../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`RUN`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Converse@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>) <br/>  [`Identity@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)  <br/> [`Translate@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>) | [`$.Hosted`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
|