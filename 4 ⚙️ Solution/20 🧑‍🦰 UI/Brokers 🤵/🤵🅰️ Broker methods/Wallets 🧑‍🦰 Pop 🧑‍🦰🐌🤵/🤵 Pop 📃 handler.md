# 🤵📃 Pop handler

> Purpose
* [Script 📃](<🤵 Pop 🐌 msg.md>) that implements the [`Pop@Broker` 🅰️ method](<🤵 Pop 🐌 msg.md>)


## Diagram

![alt text](<🤵 Pop ⚙️ uml.png>)



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

# Assign the Hello@Host Locator key
- CASE|$.Msg.Context >> $handler:
    BIND: PopBind@Broker
    HOST: PopHost@Broker
    ISSUER: PopIssuer@Broker
    TOKEN: PopToken@Broker
    VAULT: PopVault@Broker

# Verify that a Locator key was assign
- ASSERT|$handler

# Register the handler
- LOCATE|$handler >> $locator:
    Key: $.Msg.Key

# Request the Wallet to open a chat
- SEND:
    Header:
        To: $wallet.Notifier
        Subject: Assess@Notifier
    Body:
        Hook: $.Msg.Hook
        Locator: $locator
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`LOCATE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/LOCATE 🔆/🔆 LOCATE ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds` 🪣 table](<../../🤵🪣 Broker tables/Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg` 🧠 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Assess@Notifier` 🅰️ method](<../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Assess 🤵🐌📣/📣 Assess 🐌 msg.md>)
|