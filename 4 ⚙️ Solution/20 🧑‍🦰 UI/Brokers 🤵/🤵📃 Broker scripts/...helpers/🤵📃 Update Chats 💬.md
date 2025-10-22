# 🤵📃 Update chats @ Broker


## Script

> Assumes `$wallet` from the [`Assess@Broker` 📃 script](<../...handlers/🤵📃 Assess 🔆 handler.md>).

> Continues from the [`Converse` 📃 script](<🤵📃 Converse ⏩.md>)

```yaml
📃 UpdateChats:

# Verify required inputs
- ASSERT:
    - !wallet
    - !wallet.Notifier
    - !wallet.Wallet

# Notify Wallets to update Chats
- SEND:
    To: !wallet.Notifier
    Subject: Updated@Notifier
    Wallet: !wallet.Wallet
    Updates: [ CHATS ]
```

Needs ||
|-|-
| Commands | [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/.SEND 📬 msg.md>) |
| Methods | [`Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>)
|