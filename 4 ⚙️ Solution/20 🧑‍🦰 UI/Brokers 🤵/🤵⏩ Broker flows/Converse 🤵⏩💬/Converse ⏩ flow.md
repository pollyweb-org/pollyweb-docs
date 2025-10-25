# 🤵⏩🧑‍🦰 Converse @ Broker

> Part of [`Assess` ⏩ flow](<../Assess 🔆⏩🤵/Assess ⏩ flow.md>)

> Implemented by [`Converse` 📃 script](<Converse 📃 script.md>)

> Purpose

* Opens a new [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) window in the [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).

<br/>

## Flow diagram

![New chat](<Converse ⚙️ uml.png>)


| # | Call | Notes
|-|-|-|
| 1 | [👥🚀🕸 `Identity@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>) | Get the Chat's name and icon
| 2 | [👥🚀🕸 `Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | Get the Chat's title
| 3 | [🤵🐌📣 `Converse@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/2 💬 Chats/🤵🐌📣 Converse.md>) | Open a [💬 Chat](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) on the [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
| 4 | [🤵⏩🧑‍🦰 Update Chats 💬](<../Update Chats 🤵⏩💬/Update Chats ⏩ flow.md>) | [Brokers 🤵](<../../🤵🤲 Broker helper.md>) ask [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) to reload
||
