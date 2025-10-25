# 🤵📃 Chats 🚀 Broker

> [Script 📃](<Chats 🚀 request.md>)


<br/>

## Script

```yaml
📃 Chats@Broker:

# Get the wallet item
- GET >> $wallet:
    Set: Wallets@Broker
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Prepare the response
- EVAL|$wallet.Chats >> $chats
    Chat: Chat
    Host: Host
    Host$: Host$
    SmallIcon: Host.SmallIcon
    BigIcon: Host.BigIcon

# Respond
- REEL:
    Chats: $chats
```

Needs ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | [`$.Msg`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Msg 📨.md>) [`EVAL`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/EVAL ⬇️ flow.md>) [`GET`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) [`REEL`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/REEL 🎣/REEL 🎣.md>) [`VERIFY`](<../../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐 msg.md>)
|  [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../../🤵🪣 Broker tables/Chats 💬/🤵🪣 Chats table.md>) [`Wallets`](<../../../🤵🪣 Broker tables/Wallets/🤵🪣 Wallets table.md>)
|