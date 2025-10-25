# 🤵📃 Update chats @ Broker


## Script

> Assumes `$wallet` from the [`Assess@Broker` 📃 script](<../../Assess 🔆/.📎 Assets/Assess 📃 handler.md>).

> Continues from the [`Converse` 📃 script](<../../Converse 💬/.📎 Assets/Converse 📃 script.md>)

```yaml
📃 UpdateChats:

# Verify required inputs
- ASSERT:
    - !wallet
    - !wallet.Notifier
    - !wallet.Wallet

# Notify Wallets to update Chats
- SEND:
    Header:
        To: !wallet.Notifier
        Subject: Updated@Notifier
    Body:
        Wallet: !wallet.Wallet
        Updates: [ CHATS ]
```

Needs ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`SEND`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg.md>) |
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Updated@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>)
|