# 🤵📃 Update Binds

[Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that calls [`Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>) for the [`BINDS`](<../../🤵🅰️ Broker methods/Binds 🔗 Binds 🧑‍🦰🚀🤵/🤵 Binds 🚀 request.md>) command.

<br/>

## How to call
```yaml
RUN|UpdateBinds@Broker:
    Wallet: <wallet-uuid>
```

<br/>

## Script

```yaml
📃 UpdateBinds@Broker:

# Verify required inputs
- ASSERT:
    AllOf: $:Wallet
    UUIDs: $:Wallet

# Notify Wallets to update Binds
- RUN|Updated@Notifier:
    Wallet: $:Wallet
    Updates: [BINDS]
```


Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg ⌘ cmd.md>)
| [Scripts 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) | [`Update Notifier` 📃 script](<../Update Notifier 🤵⏩📣/🤵 Update Notifier 📃 script.md>)
|