# 🤵📃 Update Notifier

[Script 📃](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that calls [`Updated@Notifier`](<../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>).

<br/>

## How to call

```yaml
RUN|Updated@Notifier:
    Wallet: <wallet-uuid>
    Updates: [ CHATS, BINDS, TOKENS ]
```

## Script

```yaml
📃 Updated@Notifier:

# Assert required inputs
- ASSERT:
    OneOf: $:Wallet, Updates
    UUIDs: $:Wallet
    Lists: $:Updates

# Assert the options
- ASSERT|$:Updates:
    Enum: CHATS, BINDS, TOKENS

# Get the Wallet
- GET >> $wallet:
    Set: Wallets@Broker
    Key: $:Wallet
    
# Tell the Notifier to perform updates
- SEND:
    Header:
        To: $wallet.Notifier
        Subject: Updated@Notifier
    Body:
        Wallet: $wallet.Wallet
        Updates: $:Updates
```


Needs||
|-|-
| [Commands ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) [`SEND`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg.md>)
| [Datasets 🪣](<../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Wallets` 🪣 table](<../🤵🪣 Broker tables/Wallets/🤵🪣 Wallets table.md>)
| [Messages 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) | {{Updated@Notifier}}
|