# 🤵⏩🗄️ Update binds @ Broker

> Updates the list of [Binds 🔗](<../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>) on the Wallet app.

> Used in:
> <br/>• [🤵⏩🗄️ Bind vault @ Broker](<🤵⏩🗄️ Bind vault.md>) to add a [Bind 🔗](<../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>) to the list
> <br>•  [🧑‍🦰👉🗄️ Unbind @ Wallet](<../../1 🧑‍🦰 Wallets/🧑‍🦰👉 Wallet flows/30 👉🔗 Binds/03 🧑‍🦰👉🗄️ Unbind.md>) to remove a [Bind 🔗](<../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>) from the list

<br/>

## Flow diagram

![Update binds](<../.📎 Assets/⚙️🔗 Update binds.png>)



## Steps

| # | Call | Notes |
|-|-|-
| 1 | [🤵🐌📣 `Updated@Notifier`](<../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>)| The [Broker 🤵](<../🤵🤲 Broker helper.md>) tells the [Notifier 📣](<../../2 📣 Notifiers/📣👥 Notifier domain.md>) to update the [Wallet 🧑‍🦰](<../../1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| 2 | [🧑‍🦰🚀🤵 `Binds@Broker`](<../🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🧑‍🦰🚀🤵 Binds.md>) | The [Wallet 🧑‍🦰](<../../1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) gets the [Binds 🔗](<../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>) from the [Broker 🤵](<../🤵🤲 Broker helper.md>)
||