# 🤵⏩🧑‍🦰 Converse @ Broker

> Part of [🤵⏩🧑‍🦰 Assess @ Broker](<🤵⏩🧑‍🦰 Assess 🔆.md>)

* Opens a new chat window in the app.


<br/>

## Flow diagram

![New chat](<../.📎 Assets/⚙️💬 Converse.png>)


| # | Call | Notes
|-|-|-|
| 1 | [👥🚀🕸 `Identity@Graph`](<../../../45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>) | Get the Chat's name and icon
| 2 | [👥🚀🕸 `Translate@Graph`](<../../../45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | Get the Chat's title
| 3 | [🤵🐌📣 `Converse@Notifier`](<../../2 📣 Notifiers/📣🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>) | Open a [💬 Chat](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) on the [Wallet 🧑‍🦰 app](<../../1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| 4 | [🤵⏩🧑‍🦰 Update Chats 💬](<🤵⏩🧑‍🦰 Update Chats 💬.md>) | [Brokers 🤵](<../🤵🤲 Broker helper.md>) ask [Wallets 🧑‍🦰](<../../1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) to reload
||
