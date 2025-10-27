# 🤵📃 Update chats @ Broker

> Purpose

* [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that 
    * updates the translated [domains 👥](<../../../../40 👥 Domains/👥 Domain.md>)
    * for [Chats 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) in the [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    * and notifies the [Notifier 📣 domain](<../../../Notifiers 📣/📣👥 Notifier domain.md>) about the changes.

> Continues from the [`Converse` 📃 script](<../Converse 🤵⏩💬/🤵 Converse 📃 script.md>)


<br/>

## How to call
```yaml
RUN|UpdateChats@Broker:
    Wallet: <wallet-uuid>
```

## Script

```yaml
📃 UpdateChats@Broker:

# Verify required inputs
- ASSERT:
    AllOf: $:Wallet
    UUIDs: $:Wallet

# Notify Wallets to update Binds
- RUN|Updated@Notifier:
    Wallet: $:Wallet
    Updates: [CHATS]
```


Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg.md>)
| [Scripts 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) | [`Update Notifier` 📃 script](<../Update Notifier 🤵⏩📣/🤵 Update Notifier 📃 script.md>)
|