# 🤵📃 Chats 🚀 Broker

> [Script 📃](<🤵 Chats 🚀 request.md>)


<br/>

## Flow

![alt text](<🤵 Chats ⚙️ uml.png>)

## Script

```yaml
📃 Chats@Broker:

# Get the wallet item
- READ >> $wallet:
    Set: BrokerWallets
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
- RETURN:
    Chats: $chats
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`EVAL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
|  [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🤵 BrokerChats 🪣 table.md>) [`Wallets`](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 BrokerWallets 🪣 table.md>)
|