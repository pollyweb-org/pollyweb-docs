# 🤵📃 Update chats @ Broker

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that 
    * updates the translated [domains 👥](<../../../../../40 👥 Domains/👥 Domain.md>)
    * for [Chats 💬](<../../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) in the [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    * and notifies the [Notifier 📣 domain](<../../../../Notifiers 📣/📣👥 Notifier domain.md>) about the changes.

> Continues from the [`Converse` 📃 script](<../../Converse 💬/.📎 Assets/Converse 📃 script.md>)


<br/>

## How to call
```yaml
RUN|UpdateChats@Broker:
    Wallet: <wallet-uuid>
```

## Script

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
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Updated@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/🤵🐌📣 Updated.md>)
|