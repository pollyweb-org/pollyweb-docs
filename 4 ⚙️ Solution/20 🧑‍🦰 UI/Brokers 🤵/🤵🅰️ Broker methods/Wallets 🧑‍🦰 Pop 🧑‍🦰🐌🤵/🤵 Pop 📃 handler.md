# 🤵📃 Pop handler

> Purpose
* [Script 📃](<🤵 Pop 🐌 msg.md>) that implements the [`Pop@Broker` 🅰️ method](<🤵 Pop 🐌 msg.md>)

<br/>

## Diagram

![alt text](<🤵 Pop ⚙️ uml.png>)

<br/>

## Script


```yaml
📃 Pop@Broker: 

# Assert $.Msg
- ASSERT|$.Msg:
    - AllOf: Hook 
    - UUIDs: Hook

# Get the Wallet
- READ >> $wallet:
    Set: Broker.Wallets
    Key: $.Msg.From

# Verify the Message
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Save the Pop
- SAVE|Broker.Pops:
    Hook: $.Msg.Hook
    Wallet: $.Msg.From
    Key: $.Msg.Key
    Context: $.Msg.Context
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Pops`](<../../🤵🪣 Broker tables/Pops 🎈 table/🪣 Pops/🤵 Broker.Pops 🪣 table.md>) [`Wallets`](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg` 🧠 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|