# 🤵📃 Onboard script

> [Script 📃](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Onboard@Broker` 🅰️ method](<../📣🚀🤵 Onboard.md>)

<br/>

## Script

<!-- TODO: Charge the Notifier -->

```yaml
📃 Onboard:

# Get the Notifier
# GET|Notifiers@Broker|$.Msg.From >> $notifier

# Generate a new Wallet ID
- EVAL|.UUID >> $wallet

# Save the Wallet
- SAVE|Wallets@Broker:
    Wallet: $wallet
    Notifier: $.Msg.From
    PublicKey: $.Msg.PublicKey
    Language: $.Msg.Language

# Return the ID
- REEL:
    $wallet
```

Commands: [`$.Msg`](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Msg 📨.md>) [`EVAL`](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/EVAL ⬇️ flow.md>) [`REEL`](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/REEL 🎣/REEL 🎣.md>)

| [Command ⌘](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | Purpose
|-|-
| ⏬ [`GET`](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) | Get the hook from the [`Bindable@Broker` 🅰️ method](<../../../4 ...for Binds 🔗/Bindable 🐌/🗄️🐌🤵 Bindable.md>) 
| 💾 [`SAVE`](<../../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE/SAVE 💾 item.md>) | Save the [Bind 🔗](<../../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) to the [Wallets 🪣](<../../../../🤵🪣 Broker tables/🤵🪣 Wallets table.md>) table
|
