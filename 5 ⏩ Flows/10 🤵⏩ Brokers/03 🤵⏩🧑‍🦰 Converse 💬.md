# 🤵⏩🧑‍🦰 Converse @ Broker

> Part of [🤵⏩🧑‍🦰 Assess @ Broker](<01 🤵⏩🧑‍🦰 Assess 🔆.md>)

* Opens a new chat window in the app.


<br/>

## Flow diagram

![New chat](<.📎 Assets/⚙️💬 Converse.png>)


| # | Call | Notes
|-|-|-|
| 1 | [👥🚀🕸 `Identity@Graph`](<../../4 ⚙️ Solution/45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>) | Get the Chat's name and icon
| 2 | [👥🚀🕸 `Translate@Graph`](<../../4 ⚙️ Solution/45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | Get the Chat's title
| 3 | [🤵🐌📣 `Converse@Notifier`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>) | Open a [💬 Chat](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) on the [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| 4 | [🤵⏩🧑‍🦰 Update Chats 💬](<04 🤵⏩🧑‍🦰 Update Chats 💬.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) ask [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) to reload
||
