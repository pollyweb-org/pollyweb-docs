<!-- https://quip.com/u9H6AsA6azmA/-Wallet-Setup#temp:C:aXG191738dd4065486f9c632656b -->

# 🧑‍🦰💬🤵 Onboard @ Wallet

> Implements a [Wallet 🧑‍🦰 app](<../🧑‍🦰🛠️ Wallet app.md>)

* Registers a [Wallet 🧑‍🦰 app](<../🧑‍🦰🛠️ Wallet app.md>) on a [Broker 🤵 domain](<../../Brokers 🤵/🤵🤲 Broker helper.md>).

<br/>

## Chat

| [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| | | Install [🧑‍🦰 Wallet](<../🧑‍🦰🛠️ Wallet app.md>) |
| 🤵 [Broker](<../../Brokers 🤵/🤵🤲 Broker helper.md>) | 😃 Hi! What's your region? <br/> - [ 🇬🇧 ] United Kingdom <br> - ...  | > 🇬🇧 
| 🤵 [Broker](<../../Brokers 🤵/🤵🤲 Broker helper.md>) | ℹ️ I'll speak in British English 🇬🇧 [+]
| 🤵 [Broker](<../../Brokers 🤵/🤵🤲 Broker helper.md>) | ℹ️ Default agents set [+]
| 🤵 [Broker](<../../Brokers 🤵/🤵🤲 Broker helper.md>) | ✅ You are ready to go. 
||

<br/>

## Flow diagram

![Onboard](<../.📎 Assets/Set-up 📎/⚙️ Onboard.png>)


| # | Call | Notes
|-|-|-
| 1 | [🧑‍🦰🚀📣 `Onboard@Notifier`](<../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>) | Register the [Wallet 🧑‍🦰](<../🧑‍🦰🛠️ Wallet app.md>) on the [Notifier 📣](<../../Notifiers 📣/📣👥 Notifier domain.md>)
| 2 | [📣🚀🤵 `Onboard@Broker`](<../../Brokers 🤵/🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/📣🚀🤵 Onboard.md>) | Register a wallet ID on the [Broker 🤵](<../../Brokers 🤵/🤵🤲 Broker helper.md>)
| 3 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Ask for the user's region/country.
| 4 | [🤵⏩🗄️ Bind Vault 🔗](<../../Brokers 🤵/🤵⏩ Broker flows/Bind vault 🗄️/🤵⏩🗄️ Bind vault.md>) | Bind to the default [Vaults 🗄️](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)
||
