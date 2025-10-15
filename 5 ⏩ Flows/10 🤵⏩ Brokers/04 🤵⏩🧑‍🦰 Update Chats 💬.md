# 🤵⏩🗄️ Update chats @ Broker

* Updates the list of [Chats 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) on a [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>).
* Used in:
    * [🧑‍🦰👉🤵 Abandon chat @ Wallet](<../90 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>)
    * [🤵⏩🧑‍🦰 Converse @ Broker](<03 🤵⏩🧑‍🦰 Converse 💬.md>)

<br/>

## Flow diagram

![Update chats](<.📎 Assets/⚙️💬 Update chats.png>)


| # | Call | Notes |
|-|-|-
| 1 | [🤵🐌📣 `Updated@Notifier`](<../../6 🅰️ APIs/65 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/23 🤵🐌📣 Updated.md>)| [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) tell [Notifiers 📣](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/$ 📣 Notifier domain.md>) to update [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
| 2 | [🧑‍🦰🚀🤵 `Chats@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/02 🧑‍🦰🚀🤵 Chats.md>) | [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) get [Chats 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) from [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
||
