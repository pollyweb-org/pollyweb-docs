# 🤵⏩🗄️ Update binds @ Broker

> Updates the list of [Binds 🔗](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/01 🔗 Bind.md>) on the Wallet app.

> Used in:
> <br/>• [🤵⏩🗄️ Bind vault @ Broker](<05 🤵⏩🗄️ Bind vault.md>) to add a [Bind 🔗](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/01 🔗 Bind.md>) to the list
> <br>•  [🧑‍🦰👉🗄️ Unbind @ Wallet](<../90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/03 🧑‍🦰👉🗄️ Unbind.md>) to remove a [Bind 🔗](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/01 🔗 Bind.md>) from the list

<br/>

## Flow diagram

![Update binds](<.📎 Assets/⚙️🔗 Update binds.png>)



## Steps

| # | Call | Notes |
|-|-|-
| 1 | [🤵🐌📣 `Updated@Notifier`](<../../6 🅰️ APIs/65 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/23 🤵🐌📣 Updated.md>)| The [Broker 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) tells the [Notifier 📣](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/$ 📣 Notifier domain.md>) to update the [Wallet 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
| 2 | [🧑‍🦰🚀🤵 `Binds@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/10 🧑‍🦰🚀🤵 Binds.md>) | The [Wallet 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) gets the [Binds 🔗](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/01 🔗 Bind.md>) from the [Broker 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>)
||