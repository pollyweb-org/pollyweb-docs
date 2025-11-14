# 🤵📃 Converse 💬

> Part of the [`Assess@Broker` 📃 script](<../🤵 Locate 📃 handler.md>)

## Diagram

![alt text](<🤵 Call Converse ⚙️ uml.png>)

## Script

```yaml
📃 Call-Converse:

# Assert the inputs
- ASSERT|.Inputs:
    AllOf: chat

# Open the Chat in the Wallet app
- SEND:
    Header:
        To: $chat.Wallet.Notifier
        Subject: Converse@Notifier
    Body:
        Wallet: $chat.Wallet
        Hook: $.Msg.Hook
        Chat: $chat.ID
        PrivateKey: $chat.PrivateKey
        Host: $chat.Host.Name
        Host$: $chat.Host.Title
        SmallIcon: $chat.Host.SmallIcon
        BigIcon: $chat.Host.BigIcon

# Update the Chats
- RUN|Update-Chats:
    wallet: $chat.Wallet
```

|Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`KEYS`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/KEYS 🔑/🔑 KEYS ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`RUN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Converse@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>) <br/>  [`Identity@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)  <br/> [`Translate@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Hosted`](<../../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
|