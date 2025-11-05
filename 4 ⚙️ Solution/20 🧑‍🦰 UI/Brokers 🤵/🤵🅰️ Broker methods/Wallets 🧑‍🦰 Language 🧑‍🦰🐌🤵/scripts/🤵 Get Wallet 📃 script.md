# 🤵 Get Wallet 📃 script

> Part of the [`Language` 📃 handler](<../🤵 Language 📃 handler.md>)


## Script

```yaml
📃 Get-Wallet:

# Get the wallet
- READ >> $wallet:
    Set: BrokerWallets
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

- RETURN:
    $wallet
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) |  [`READ`](<../../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerWallets`](<../../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 BrokerWallets 🪣 table.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>)   |  [`$.Msg`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|