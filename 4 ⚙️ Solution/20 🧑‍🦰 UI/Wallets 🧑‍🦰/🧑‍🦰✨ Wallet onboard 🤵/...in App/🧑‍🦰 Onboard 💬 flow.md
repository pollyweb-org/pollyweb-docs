# 🧑‍🦰💬🤵 Onboard @ Wallet

> Implements a [Wallet 🧑‍🦰 app](<../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)

* Registers a [Wallet 🧑‍🦰 app](<../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) on a [Broker 🤵 domain](<../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>).

<br/>

## Chat

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| | | Install [🧑‍🦰 Wallet](<../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) |
| 🤵 [Broker](<../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 😃 Hi! What's your region? <br/> - [ 🇬🇧 ] United Kingdom <br> - ...  | > 🇬🇧 
| 🤵 [Broker](<../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | ℹ️ I'll speak in British English 🇬🇧 [+]
| 🤵 [Broker](<../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | ℹ️ Default agents set [+]
| 🤵 [Broker](<../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | ✅ You are ready to go. 
||

<br/>

## Flow diagram

![Onboard](<🧑‍🦰 Onboard ⚙️ uml.png>)


| # | Call | Notes
|-|-|-
| 1 | [🧑‍🦰🚀📣 `Onboard@Notifier`](<../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>) | Register the [Wallet 🧑‍🦰](<../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) on the [Notifier 📣](<../../../Notifiers 📣/📣/📣 Notifier 👥 domain.md>)
| 2 | [📣🚀🤵 `Onboard@Broker`](<../../../Brokers 🤵/🤵📨 Broker msgs/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 call.md>) | Register a wallet ID on the [Broker 🤵](<../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>)
| 3 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | Ask for the user's region/country.
| 4 | [🤵⏩🗄️ Bind Vault 🔗](<../../../Brokers 🤵/🤵⏩ Broker flows/Bind vault 🗄️⏩🤵/Bind vault ⏩ flow.md>) | Bind to the default [Vaults 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>)
||
