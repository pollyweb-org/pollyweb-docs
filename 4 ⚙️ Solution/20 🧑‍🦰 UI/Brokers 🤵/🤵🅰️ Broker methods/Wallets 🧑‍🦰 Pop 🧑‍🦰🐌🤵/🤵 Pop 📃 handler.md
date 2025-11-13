# 🤵📃 Pop handler

> Purpose
* [Script 📃](<🤵 Pop 🐌 msg.md>) that implements the [`Pop@Broker` 🅰️ method](<🤵 Pop 🐌 msg.md>)


## Diagram

![alt text](<🤵 Pop ⚙️ uml.png>)

## Script

<!-- TODO: Finish the code -->

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
    BIND: PopBind
    HOST: PopHost
    ISSUER: PopIssuer
    TOKEN: PopToken
    VAULT: PopVault

# Verify that a Locator key was assign
- ASSERT: $handler

# Request the Wallet to open a chat
- SEND:
    Header:
        To: $wallet.Notifier
        Subject: Open@Notifier
    Body:
        Hook: $.Msg.Hook
        Schema: .HOST
        Host: $.Hoster.Domain
        Key: $handler
        Parameters: 
            Key: $.Msg.Key
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds` 🪣 table](<../../🤵🪣 Broker tables/Binds 🔗 table/🤵 Broker.Binds 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg` 🧠 holder](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|