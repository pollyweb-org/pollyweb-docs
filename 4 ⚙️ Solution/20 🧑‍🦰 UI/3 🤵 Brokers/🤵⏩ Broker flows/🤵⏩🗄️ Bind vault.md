# 🤵⏩🗄️ Bind vault @ [Broker](<../🤵🤲 Broker helper.md>)

> Steps to create a [Bind 🔗](<../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>).


> Used in:
> <br/>• [🧑‍🦰👉🤵 Onboard @ Wallet](<../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet chats/in 🏠 Home/🧑‍🦰💬🤵 Onboard.md>) when setting the default [Vaults 🗄️](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) upon install.
> <br/>•  [🧑‍🦰👉🗄️ Bind @ Wallet](<../../1 🧑‍🦰 Wallets/🧑‍🦰⏩ Wallet flows/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind 🔗.md>) when the user binds to to a [Vault 🗄️](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) in a chat.




## Flow diagram

![Bind vault](<../.📎 Assets/⚙️🗄️ Bind vault.png>)


## Steps

| # | API | Description |
|-|-|-
| 1 | [👥🚀🕸 `Translate@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | The [Broker 🤵](<../🤵🤲 Broker helper.md>) translates into the user's language
| 2 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | The [Broker 🤵](<../🤵🤲 Broker helper.md>) informs the user about the [Bind 🔗](<../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>)
| 3 | [🤵🐌🗄️ `Bound@Vault`](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/🤵🐌🗄️ Bound.md>)| Tell [Vaults 🗄️](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) about each bound [Schema Code 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)
| 4 | [🤵⏩🧑‍🦰 Update Binds 🔗](<🤵⏩🧑‍🦰 Update Binds 🔗.md>) | [Brokers 🤵](<../🤵🤲 Broker helper.md>) asks [Wallets 🧑‍🦰](<../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>) to update the [Binds 🔗](<../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>)
||