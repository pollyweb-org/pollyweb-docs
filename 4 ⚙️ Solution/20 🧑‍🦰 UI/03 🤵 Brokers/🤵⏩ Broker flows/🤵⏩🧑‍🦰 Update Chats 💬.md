# 🤵⏩🗄️ Update chats @ Broker

* Updates the list of [Chats 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>) on a [Wallet 🧑‍🦰 app](<../../01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>).
* Used in:
    * [🧑‍🦰👉🤵 Abandon chat @ Wallet](<../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>)
    * [🤵⏩🧑‍🦰 Converse @ Broker](<🤵⏩🧑‍🦰 Converse 💬.md>)

<br/>

## Flow diagram

![Update chats](<../.📎 Assets/⚙️💬 Update chats.png>)


| # | Call | Notes |
|-|-|-
| 1 | [🤵🐌📣 `Updated@Notifier`](<../../02 📣 Notifiers/🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>)| [Brokers 🤵](<../🤵🤲 Broker helper.md>) tell [Notifiers 📣](<../../02 📣 Notifiers/📣 Notifier domain.md>) to update [Wallets 🧑‍🦰](<../../01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| 2 | [🧑‍🦰🚀🤵 `Chats@Broker`](<../🤵🅰️ Broker methods/30 🤵🅰️ Chats 💬/🧑‍🦰🚀🤵 Chats.md>) | [Wallets 🧑‍🦰](<../../01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) get [Chats 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>) from [Brokers 🤵](<../🤵🤲 Broker helper.md>)
||
