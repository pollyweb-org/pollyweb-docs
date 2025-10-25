# 🤵⏩🗄️ Update binds @ Broker

> Purpose

* Updates the list of [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) on the [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)

> Used in
* [🤵⏩🗄️ Bind vault @ Broker](<../Bind vault 🗄️⏩🤵/Bind vault ⏩ flow.md>) to add a [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) to the list
*  [🧑‍🦰👉🗄️ Unbind @ Wallet](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Vaults 🗄️/💬🤵 Unbind 🗄️ chat.md>) to remove a [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) from the list

<br/>

## Flow diagram

![Update binds](<🤵 Update binds ⚙️ uml.png>)



## Steps

| # | Call | Notes |
|-|-|-
| 1 | [🤵🐌📣 `Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🤵 Updated 🤵🐌📣/Updated 🐌 msg.md>)| The [Broker 🤵](<../../🤵🤲 Broker helper.md>) tells the [Notifier 📣](<../../../Notifiers 📣/📣👥 Notifier domain.md>) to update the [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
| 2 | [🧑‍🦰🚀🤵 `Binds@Broker`](<../../🤵🅰️ Broker methods/Binds 🔗 Binds 🧑‍🦰🚀🤵/🤵 Binds 🚀 request.md>) | The [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) gets the [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) from the [Broker 🤵](<../../🤵🤲 Broker helper.md>)
||