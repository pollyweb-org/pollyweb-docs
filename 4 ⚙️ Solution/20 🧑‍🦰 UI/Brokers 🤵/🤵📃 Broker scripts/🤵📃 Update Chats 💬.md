# 🤵📃 Update chats @ Broker


## Script

> Assumes `$wallet` and `$locator` placeholders from the [`Assess@Broker` 📃 script](<🤵📃 Assess 🔆.md>).

> Continues from the [`Converse` 📃 script](<../🤵📃 Broker scripts/🤵📃 Converse ⏩.md>)

```yaml
📃 UpdateChats:

# Notify Wallets to update Chats
- SEND:
    To: $wallet.Notifier
    Subject: Updated@Notifier
    Wallet: $wallet.Wallet
    Updates: [ CHATS ]
```

Needs ||
|-|-
| Commands | [`SEND`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/.SEND 📬 msg.md>) |
| Methods | [`Updated@Notifier`](<../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>)
|