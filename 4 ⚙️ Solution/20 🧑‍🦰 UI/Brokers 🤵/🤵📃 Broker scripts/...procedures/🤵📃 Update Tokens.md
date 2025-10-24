# 🤵📃 Update Tokens

[Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... ⌘ commands/📃 Script.md>) that calls [`Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>) for `TOKENS`.

<br/>

## Script

```yaml
📃 UpdateTokens: 

# Assert inputs
- ASSERT:
    - !wallet
    - !wallet.Notifier
    - !wallet.Wallet

# Update the Token 🎫 list
- SEND:
    To: !wallet.Notifier
    Subject: Updated@Notifier
    Wallet: !wallet.Wallet
    Updates: [ TOKENS ]
```

Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... ⌘ commands/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... placeholders 🧠/ASSERT 🚦.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages/SEND 📬 msg.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>)
|