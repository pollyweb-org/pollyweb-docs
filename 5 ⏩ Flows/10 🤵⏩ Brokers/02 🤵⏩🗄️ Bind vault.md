# 🤵⏩🗄️ Bind vault @ [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)

> Steps to create a [Bind 🔗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>).


> Used in:
> <br/>• [🧑‍🦰👉🤵 Onboard @ Wallet](<../90 🧑‍🦰👉 Wallets/10 👉🤵 Set-up/11 🧑‍🦰👉🤵 Onboard.md>) when setting the default [Vaults 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) upon install.
> <br/>•  [🧑‍🦰👉🗄️ Bind @ Wallet](<../80 🗄️⏩ Vaults/01 🗄️⏩🧑‍🦰 Bind.md>) when the user binds to to a [Vault 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) in a chat.




## Flow diagram

![Bind vault](<.📎 Assets/⚙️ Bind vault.png>)


## Steps

| # | API | Description |
|-|-|-
| 1 | [👥🚀🕸 Translate @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/06 👥🚀🕸 Translate.md>) | The [Broker 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) translates into the user's language
| 2 | [🤗⏩🧑‍🦰 Prompt @ Host](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | The [Broker 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) informs the user about the [Bind 🔗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>)
| 3 | [🤵🐌🗄️ Bound @ Vault](<../../6 🅰️ APIs/95 🗄️🅰️ Vault/02 🤵🐌🗄️ Bound.md>)| Informs the [Vault 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) about each bound [Schema Code 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
| 4 | [🤵⏩🧑‍🦰 Update Binds @ Broker](<03 🤵⏩🧑‍🦰 Update binds.md>) | The [Broker 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) asks the [Wallet 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to update the [Binds 🔗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>)
||