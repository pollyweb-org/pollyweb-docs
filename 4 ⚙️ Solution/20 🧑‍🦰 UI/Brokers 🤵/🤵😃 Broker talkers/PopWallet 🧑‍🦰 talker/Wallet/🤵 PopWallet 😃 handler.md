# 🤵 PopWallet 🔆 handler

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to a Pop in a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).

<br/>

## Diagram

![alt text](<🤵 PopWallet ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 PopWallet:

# Assert the inputs
- ASSERT:
    $.Chat.Wallet: 

# Get the Wallet
- SELECT >> $wallet:
    From: Broker.Wallets
    Key: $.Chat.Wallet

# Show the options
- ONE:
    Title: What do you need?
    Options: 
        - /Localize

# Handle the selection
- CASE >> $handler:
    Localize: PopWalletLocalize

# Handle the selection
- RUN $handler: $wallet
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>)  [`ONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/1️⃣ ONE ⌘ cmd.md>)  [`RUN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`SELECT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Wallets`](<../../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) 
