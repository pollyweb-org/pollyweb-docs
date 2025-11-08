# 🤵📃 Onboard script

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Onboard@Broker` 🅰️ method](<🤵 Onboard 🚀 request.md>)

<br/>

## Script

<!-- TODO: Charge the Notifier -->

```yaml
📃 Onboard:

# Verify the Notifier as a client
# READ|Notifiers@Broker|$.Msg.From >> $notifier

# Generate a new Wallet ID
- PUT|.UUID >> $wallet

# Save the Wallet
- SAVE|BrokerWallets:
    Wallet: $wallet
    Notifier: $.Msg.From
    PublicKey: $.Msg.PublicKey
    Language: $.Msg.Language

# Return the ID
- RETURN:
    $wallet
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |  [`EVAL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Wallets` 🪣 table](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 BrokerWallets 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|
