# 🤵⏩🗄️ Update chats @ [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)

> Updates the list of Chats on the Wallet app.

> Used by [🧑‍🦰👉🤵 Abandon chat @ Wallet](<../02 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>)
> <br/>Used by [🤵⏩🧑‍🦰 New chat @ Broker](<01 🤵⏩🧑‍🦰 Assessed.md>)


## Flow diagram

![Update chats](<.📎 Assets/⚙️ Update chats.png>)


| # | Call | Notes |
|-|-|-
| 1 | [🤵🐌📣 Updated @ Notifier](<../../6 🅰️ APIs/12 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/23 🤵🐌📣 Updated.md>)| The [Broker 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) tells the [Notifier 📣](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) to update the [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
| 2 | [🧑‍🦰🚀🤵 Chats @ Broker](<../../6 🅰️ APIs/02 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/02 🧑‍🦰🚀🤵 Chats.md>) | The [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) gets the [Chats 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) from the [Broker 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>).
||
