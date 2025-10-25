# 🤵📃 Update Tokens

[Script 📃](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that calls [`Updated@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/🤵🐌📣 Updated.md>) for `TOKENS`.

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
    Header:
        To: !wallet.Notifier
        Subject: Updated@Notifier
    Body:
        Wallet: !wallet.Wallet
        Updates: [ TOKENS ]
```

Needs||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`SEND`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Updated@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/🤵🐌📣 Updated.md>)
|