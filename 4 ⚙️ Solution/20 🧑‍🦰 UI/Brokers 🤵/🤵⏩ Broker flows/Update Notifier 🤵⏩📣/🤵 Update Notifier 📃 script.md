# 🤵📃 Update Notifier

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that calls [`Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>).

<br/>

## How to call

```yaml
RUN|Update-Notifier:
    wallet: $wallet
    updates: CHATS, BINDS, TOKENS
```

## Script

```yaml
📃 Update-Notifier:

# Assert required inputs
- ASSERT|$.Inputs:
    - OneOf: wallet, updates
    - Lists: updates
    - updates.IsIn(CHATS,BINDS,TOKENS)
    
# Tell the Notifier to perform updates
- SEND:
    Header:
        To: $wallet.Notifier
        Subject: Updated@Notifier
    Body:
        Wallet: $wallet.ID
        Updates: $updates.ToList
```


Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Wallets` 🪣 table](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 BrokerWallets 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsIn`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsIn}.md>) [`.ToList`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.ToList}.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Updated@Notifier` 🅰️ method](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|