# 🤵📃 Update Tokens

[Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that calls [`Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🤵 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>) for `TOKENS`.

<br/>


## Script

```yaml
📃 UpdateTokens@Broker:

# Verify required inputs
- ASSERT:
    AllOf: $:Wallet
    UUIDs: $:Wallet

# Notify Wallets to update Binds
- RUN|Updated@Notifier:
    Wallet: $:Wallet
    Updates: [TOKENS]
```


Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg.md>)
| [Scripts 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) | [`Update Notifier` 📃 script](<../../.📎 Assets/Update Notifier 📃 script.md>)
|
