# 🤵📃 Chats 🚀 Broker

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements the [`Chats@Broker` 🅰️ method](<../../🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🚀🤵 Chats.md>)


<br/>

## Script

```yaml
📃 Chats@Broker:

# Get the wallet item
- GET >> $wallet:
    Pool: Wallets@Broker
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
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) [`EVAL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/EVAL ⬇️ flow.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) [`REEL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/REEL 🎣.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>)
|  [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../🤵🪣 Broker tables/🤵🪣 Chats table.md>) [`Wallets`](<../../🤵🪣 Broker tables/🤵🪣 Wallets table.md>)
|