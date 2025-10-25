# 🤵⏩🗄️ Update binds @ Broker

> Updates the list of [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) on the Wallet app.

> Used in:
> <br/>• [🤵⏩🗄️ Bind vault @ Broker](<../Bind vault 🗄️/🤵⏩🗄️ Bind vault.md>) to add a [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) to the list
> <br>•  [🧑‍🦰👉🗄️ Unbind @ Wallet](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Vaults 🗄️/💬🤵 Unbind 🗄️ chat.md>) to remove a [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) from the list

<br/>

## Flow diagram

![Update binds](<../../.📎 Assets/⚙️🔗 Update binds.png>)



## Steps

| # | Call | Notes |
|-|-|-
| 1 | [🤵🐌📣 `Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>)| The [Broker 🤵](<../../🤵🤲 Broker helper.md>) tells the [Notifier 📣](<../../../Notifiers 📣/📣👥 Notifier domain.md>) to update the [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
| 2 | [🧑‍🦰🚀🤵 `Binds@Broker`](<../../🤵🅰️ Broker methods/4 ...for Binds 🔗/Binds/🧑‍🦰🚀🤵 Binds.md>) | The [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) gets the [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) from the [Broker 🤵](<../../🤵🤲 Broker helper.md>)
||