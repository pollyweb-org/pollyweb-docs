# 🤵📃 Binds 🔗

> [Script 📃](<🤵 Binds 🚀 request.md>) that handles the [`Binds@Broker` 🅰️ method](<🤵 Binds 🚀 request.md>)

<br/>

## Script

```yaml
📃 Binds@Broker:

# Get the wallet item
- GET >> $wallet:
    Set: Wallets@Broker
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Prepare the response
- EVAL|$wallet.Binds >> $binds:
    - Bind
    - Vault
    - Vault$
    - Schema
    - Schema$

# Respond
- RETURN:
    Binds: $binds
```

|Needs ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`EVAL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/EVAL ⬇️ flow.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET ⏬/GET ⏬ item.md>) [`RETURN`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RETURN ⤴️/RETURN ⤴️.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐 msg.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Wallets` 🪣 table](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>) <br/> [`Binds` 🪣 table](<../../🤵🪣 Broker tables/Binds 🔗 table/🤵 BrokerBinds 🪣 table.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Msg 📨.md>) 
|