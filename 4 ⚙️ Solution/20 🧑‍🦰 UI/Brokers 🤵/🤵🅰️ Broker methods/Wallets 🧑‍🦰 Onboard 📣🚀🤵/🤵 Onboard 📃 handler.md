# 🤵📃 Onboard script

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that implements the [`Onboard@Broker` 🅰️ method](<🤵 Onboard 🚀 request.md>)

<br/>

## Script

<!-- TODO: Charge the Notifier -->

```yaml
📃 Onboard:

# Verify the Notifier as a client
# GET|Notifiers@Broker|$.Msg.From >> $notifier

# Generate a new Wallet ID
- EVAL|.UUID >> $wallet

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

Needs||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) |  [`EVAL`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`SAVE`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`RETURN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Wallets` 🪣 table](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
|
