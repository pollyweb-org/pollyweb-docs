# 🤵📃 Update Tokens

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 commands ⌘/Script 📃/📃 Script.md>) that calls [`Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>) for `TOKENS`.

<br/>


## Script

```yaml
📃 UpdateTokens@Broker:

# Verify required inputs
- ASSERT|$.Inputs:
    AllOf: Wallet
    UUIDs: Wallet

# Notify Wallets to update Binds
- RUN|Updated@Notifier:
    Wallet: $:Wallet
    Updates: [TOKENS]
```


Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/📃 commands ⌘/Script 📃/📃 Script.md>) | [`Update Notifier` 📃 script](<../Update Notifier 🤵⏩📣/🤵 Update Notifier 📃 script.md>)
|
