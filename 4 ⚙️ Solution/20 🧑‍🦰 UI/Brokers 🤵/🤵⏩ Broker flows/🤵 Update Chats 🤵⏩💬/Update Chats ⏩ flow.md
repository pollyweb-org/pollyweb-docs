# 🤵⏩🗄️ Update chats @ Broker

> Implemented by the [`UpdateChats` 📃 script](<Update Chats 📃 script.md>)

> Purpose

* Updates the list of [Chats 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) on a [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).

> Used in
* [🧑‍🦰👉🤵 Abandon chat @ Wallet](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Chats 💬/💬🤵 Abandon 💬.md>)
* [🤵⏩🧑‍🦰 Converse @ Broker](<../🤵 Converse 🤵⏩💬/Converse ⏩ flow.md>)

<br/>

## Flow diagram

![Update chats](<Update chats ⚙️ uml.png>)


| # | Call | Notes |
|-|-|-
| 1 | [🤵🐌📣 `Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/📣 Onboard 🤵 Updated 🤵🐌📣/Updated 🐌 msg.md>)| [Brokers 🤵](<../../🤵🤲 Broker helper.md>) tell [Notifiers 📣](<../../../Notifiers 📣/📣👥 Notifier domain.md>) to update [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
| 2 | [🧑‍🦰🚀🤵 `Chats@Broker`](<../../🤵🅰️ Broker methods/🤵 Chats 💬 Chats 🧑‍🦰🚀🤵/🤵 Chats 🚀 request.md>) | [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) get [Chats 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) from [Brokers 🤵](<../../🤵🤲 Broker helper.md>)
||

