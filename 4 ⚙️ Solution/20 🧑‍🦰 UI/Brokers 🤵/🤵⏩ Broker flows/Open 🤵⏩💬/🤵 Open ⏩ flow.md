# 🤵⏩🧑‍🦰 Open @ Broker

> Flow
* Part of the [`Locate` ⏩ flow](<../Locate 🔆⏩🤵/🤵 Locate ⏩ flow.md>)

> Purpose

* Opens a new [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) window in the [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).

<br/>

## Flow diagram

![New chat](<🤵 Open ⚙️ uml.png>)


| # | Call | Notes
|-|-|-|
| 1 | [👥🚀🕸 `Domain@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Domain/🕸 Domain 🚀 call.md>) | Get the Chat's name and icon
| 2 | [👥🚀🕸 `Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>) | Get the Chat's title
| 3 | [🤵🐌📣 `Open@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>) | Open a [💬 Chat](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) on the [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
||
