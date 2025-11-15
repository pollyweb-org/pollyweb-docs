# 🤵⏩🗄️ Bind vault @ [Broker](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Purpose

* Steps to create a [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>).


> Used in
* [🧑‍🦰👉🤵 Onboard @ Wallet](<../../../Wallets 🧑‍🦰/🧑‍🦰✨ Wallet onboard 🤵/...in App/🧑‍🦰 Onboard 💬 flow.md>) when setting the default [Vaults 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) upon install.
*  [🧑‍🦰👉🗄️ Bind @ Wallet](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Bind 👉🗄️🔗/🧑‍🦰 Bind vault ⏩ flow.md>) when the user binds to to a [Vault 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) in a chat.




## Flow diagram

![Bind vault](<Bind vault ⚙️ uml.png>)


## Steps

| # | API | Description |
|-|-|-
| 1 | [👥🚀🕸 `Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate/👥🚀🕸 Translate.md>) | The [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) translates into the user's language
| 2 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | The [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) informs the user about the [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
| 3 | [🤵🐌🗄️ `Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)| Tell [Vaults 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) about each bound [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
||