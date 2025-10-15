# 🤵⏩🧑‍🦰 Converse @ Broker

> Part of [🤵⏩🧑‍🦰 Assess @ Broker](<01 🤵⏩🧑‍🦰 Assess 🔆.md>)

* Opens a new chat window in the app.


<br/>

## Flow diagram

![New chat](<.📎 Assets/⚙️💬 Converse.png>)


| # | Call | Notes
|-|-|-|
| 1 | [👥🚀🕸 `Identity@Graph`](<../../6 🅰️ APIs/45 🕸🅰️ Graph/04 👥🚀🕸 Identity.md>) | Get the Chat's name and icon
| 2 | [👥🚀🕸 `Translate@Graph`](<../../6 🅰️ APIs/45 🕸🅰️ Graph/06 👥🚀🕸 Translate.md>) | Get the Chat's title
| 3 | [🤵🐌📣 `Converse@Notifier`](<../../6 🅰️ APIs/65 📣🅰️ Notifier/02 📣💬🅰️ Chats/21 🤵🐌📣 Converse.md>) | Open a [💬 Chat](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) on the [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
| 4 | [🤵⏩🧑‍🦰 Update Chats 💬](<04 🤵⏩🧑‍🦰 Update Chats 💬.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) ask [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) to reload
||
