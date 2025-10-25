<!-- https://quip.com/b8a0AHaXf3C6#temp:C:DPSe1a859381bc449598713c8c71 -->

# 🧑‍🦰💬🤵 Unbind @ Wallet

> Implemented by the [`Pop Vault` script](<../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Pop 🧑‍🦰🐌🤵/🤵 Pop 📃 Vault 🗄️ script.md>).

> Implements a [Wallet 🧑‍🦰 app](<../../🧑‍🦰🛠️ Wallet app.md>)


* Scenario: the user wants to unbind from a [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>).

<br/>

## Chat

> Implemented by [Pop Vault 🔆 handler](<../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Pop 🧑‍🦰🐌🤵/🤵 Pop 📃 Vault 🗄️ script.md>).

| [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
...
| 🗄️ [Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | ✅ Done. Your wallet is bound.
| | | > Broker 🤵 |
| 🤵 [Broker](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 What do you need? <br/> - [ Unbind ] vault <br/> - [ Something else ] | > Unbind
| 🤵 [Broker](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 Which codes? [All, No] <br/> - [ ] Some schema code 🧩 <br/> - [ ] Some other schema code 🧩 | > All
| 🤵 [Broker](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) | ✅ Codes unbound.
||

<br/>


## Flow diagram

![alt text](<../../.📎 Assets/Binds 📎/⚙️ Unbind vault.png>)


| # | Call | Notes
|-|-|-
| 1 | [🧑‍🦰🐌🤵 `Pop@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>) | Call the [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) in a [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>)  with a [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
| 2 | [🤗⏩🧑‍🦰 `Prompt@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Ask the [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) to remove the  [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
| 3 | [🤵⏩🧑‍🦰 Update Binds 🔗](<../../../Brokers 🤵/🤵⏩ Broker flows/Update Binds 🤵⏩🔗/🤵 Update Binds ⏩ flow.md>) | Asks the [Wallet 🧑‍🦰](<../../🧑‍🦰🛠️ Wallet app.md>) to update the [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
| 4 | [🤵🐌🗄️ `Unbound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Unbound 🤵🐌🗄️/🗄️ Unbound 🐌 msg.md>) | The [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) unbinds and informs the [Vault 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)
|



<br/>
