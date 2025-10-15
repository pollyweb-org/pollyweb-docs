# 🤵⏩🗄️ Bind vault @ [Broker](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>)

> Steps to create a [Bind 🔗](<../../4 ⚙️ Solution/30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>).


> Used in:
> <br/>• [🧑‍🦰👉🤵 Onboard @ Wallet](<../90 🧑‍🦰👉 Wallets/10 👉🤵 Set-up/11 🧑‍🦰👉🤵 Onboard.md>) when setting the default [Vaults 🗄️](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) upon install.
> <br/>•  [🧑‍🦰👉🗄️ Bind @ Wallet](<../90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind 🔗.md>) when the user binds to to a [Vault 🗄️](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) in a chat.




## Flow diagram

![Bind vault](<.📎 Assets/⚙️🗄️ Bind vault.png>)


## Steps

| # | API | Description |
|-|-|-
| 1 | [👥🚀🕸 `Translate@Graph`](<../../6 🅰️ APIs/45 🕸🅰️ Graph/06 👥🚀🕸 Translate.md>) | The [Broker 🤵](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) translates into the user's language
| 2 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔 flow.md>) | The [Broker 🤵](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) informs the user about the [Bind 🔗](<../../4 ⚙️ Solution/30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>)
| 3 | [🤵🐌🗄️ `Bound@Vault`](<../../6 🅰️ APIs/95 🗄️🅰️ Vault/02 🤵🐌🗄️ Bound.md>)| Tell [Vaults 🗄️](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) about each bound [Schema Code 🧩](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>)
| 4 | [🤵⏩🧑‍🦰 Update Binds 🔗](<06 🤵⏩🧑‍🦰 Update Binds 🔗.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) asks [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) to update the [Binds 🔗](<../../4 ⚙️ Solution/30 🧩 Data/20 🔗 Binds/$ 🔗 Bind.md>)
||