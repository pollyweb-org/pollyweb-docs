# 🤵📃 Onboard script

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Onboard@Broker` 🅰️ method](<🤵 Onboard 🚀 request.md>)

<br/>

## Script

<!-- TODO: Charge the Notifier -->

```yaml
📃 Onboard:

# Verify the Notifier as a client
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
- RETURN:
    $wallet
```

Needs||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) |  [`EVAL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/EVAL ⬇️ flow.md>) [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE/SAVE 💾 item.md>) [`RETURN`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RETURN ⤴️/RETURN ⤴️.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Wallets` 🪣 table](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Msg 📨.md>)
|
