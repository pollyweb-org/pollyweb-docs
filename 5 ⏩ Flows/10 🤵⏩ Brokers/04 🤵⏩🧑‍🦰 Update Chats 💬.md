# 🤵⏩🗄️ Update chats @ Broker

* Updates the list of [Chats 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) on a [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>).
* Used in:
    * [🧑‍🦰👉🤵 Abandon chat @ Wallet](<../90 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>)
    * [🤵⏩🧑‍🦰 Converse @ Broker](<03 🤵⏩🧑‍🦰 Converse 💬.md>)

<br/>

## Flow diagram

![Update chats](<.📎 Assets/⚙️💬 Update chats.png>)


| # | Call | Notes |
|-|-|-
| 1 | [🤵🐌📣 `Updated@Notifier`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>)| [Brokers 🤵](<../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) tell [Notifiers 📣](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/📣 Notifier domain.md>) to update [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| 2 | [🧑‍🦰🚀🤵 `Chats@Broker`](<../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/30 🤵🅰️ Chats 💬/🧑‍🦰🚀🤵 Chats.md>) | [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) get [Chats 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) from [Brokers 🤵](<../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>)
||
