# 🤵📃 Locate@Broker

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Locate@Broker` 📨 msg](<🤵 Locate 🐌 msg.md>)


## Flow

![alt text](<🤵 Locate ⚙️ uml.png>)




## Script

```yaml
📃 Locate@Broker:

# Verify the required inputs
- ASSERT|$.Msg:
    AllOf: Locator, Hook
    Texts: Locator 
    UUIDs: Hook

# Get the Wallet item
- READ >> $wallet:
    Set: Broker.Wallets
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Create a new Chat
- SAVE|Broker.Chats >> $chat:
    .State: ASKED
    Hook: $.Msg.Hook
    Origin: $.Msg.Origin
    Wallet: $wallet.ID
    Locator: $.Msg.Locator
```

| Uses | |
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>)    | [`Chats`](<../../🤵🪣 Broker tables/Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Wallets`](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
|[Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>) 
| 