# 🤵⏩🗄️ Update chats @ Broker

> Updates the list of [Chats 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) on a [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).

> Implemented by the [`UpdateChats` 📃 script](<.📎 Assets/🤵📃 Update Chats 💬.md>)

> Used in:
* [🧑‍🦰👉🤵 Abandon chat @ Wallet](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Chats 💬/💬🤵 Abandon 💬.md>)
* [🤵⏩🧑‍🦰 Converse @ Broker](<../Converse 💬/🤵⏩🧑‍🦰 Converse 💬.md>)

<br/>

## Flow diagram

![Update chats](<../../.📎 Assets/⚙️💬 Update chats.png>)


| # | Call | Notes |
|-|-|-
| 1 | [🤵🐌📣 `Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>)| [Brokers 🤵](<../../🤵🤲 Broker helper.md>) tell [Notifiers 📣](<../../../Notifiers 📣/📣👥 Notifier domain.md>) to update [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
| 2 | [🧑‍🦰🚀🤵 `Chats@Broker`](<../../🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🚀🤵 Chats.md>) | [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) get [Chats 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) from [Brokers 🤵](<../../🤵🤲 Broker helper.md>)
||

