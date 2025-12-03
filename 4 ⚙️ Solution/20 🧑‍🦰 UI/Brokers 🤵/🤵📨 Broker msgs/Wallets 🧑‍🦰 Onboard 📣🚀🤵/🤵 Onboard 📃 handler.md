# 🤵 Onboard@Broker 📃 handler

> About
* Part of [Broker 🤵 domains](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Onboard@Broker` 📨 msg](<🤵 Onboard 🚀 call.md>)

<br/>

## Diagram

![alt text](<🤵 Onboard ⚙️ uml.png>)

<br/>

## Script

<!-- TODO: Charge the Notifier -->

```yaml
📃 Onboard@Broker:

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: PublicKey, Language
    Texts: PublicKey, Language

# Verify the Message
- VERIFY|$.Msg

# Verify the Notifier as a client
- READ >> $notifier:
    Set: Broker.Notifiers
    Key: $.Msg.From
    Assert: 
        .State: ACTIVE

# Save the Wallet
- SAVE|Broker.Wallets >> $wallet:
    Notifier: $.Msg.From
    PublicKey: $.Msg.PublicKey
    Language: $.Msg.Language

# Return the ID
- RETURN:
    $wallet.ID
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |  [`CALL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Notifiers`](<../../🤵🪣 Broker tables/Notifiers 📣 table/🪣 Notifiers/🤵 Broker.Notifiers 🪣 table.md>) [`Broker.Wallets`](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|
