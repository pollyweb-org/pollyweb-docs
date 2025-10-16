<!-- https://quip.com/b8a0AHaXf3C6#temp:C:DPSe1a859381bc449598713c8c71 -->

# 🧑‍🦰👉🗄️ Unbind @ Wallet

> Implements a [Wallet 🧑‍🦰 app](<../../🧑‍🦰🛠️ Wallet app.md>)


* Scenario: the user wants to unbind from a [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>).

<br/>

## Chat

| [Domain](<../../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
...
| 🗄️ [Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | ✅ Done. Your wallet is bound.
| | | > Broker 🤵 |
| 🤵 [Broker](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 What do you need? <br/> - [ Unbind ] vault <br/> - [ Something else ] | > Unbind
| 🤵 [Broker](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Which codes? [All, No] <br/> - [ ] Some schema code 🧩 <br/> - [ ] Some other schema code 🧩 | > All
| 🤵 [Broker](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) | ✅ Codes unbound.
||

<br/>


## Flow diagram

![alt text](<../../🧑‍🦰⏩ Wallet flows/30 👉🔗 Binds/.📎 Assets/⚙️ Unbind.png>)


| # | Call | Notes
|-|-|-
| 1 | [🧑‍🦰🐌🤗 `Home@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🤵🐌🤗 Home.md>) | Call the [Broker 🤵](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) in a [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>)  with a [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
| 2 | [🤗⏩🧑‍🦰 `Prompt@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Ask the [Broker 🤵](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) to remove the  [Bind 🔗](<../../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>)
| 3 | [🤵🐌🗄️ `Unbound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/🤵🐌🗄️ Unbind.md>) | The [Broker 🤵](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) unbinds and informs the [Vault 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)
| 4 | [🤵⏩🧑‍🦰 Update Binds 🔗](<../../../3 🤵 Brokers/🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Binds 🔗.md>) | Asks the [Wallet 🧑‍🦰](<../../🧑‍🦰🛠️ Wallet app.md>) to update the [Binds 🔗](<../../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>)
|
