<!-- https://quip.com/b8a0AHaXf3C6#temp:C:DPSe1a859381bc449598713c8c71 -->

# 🧑‍🦰👉🗄️ Unbind @ Wallet

> Implements a [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)


* Scenario: the user wants to unbind from a [Vault 🗄️ domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>).

<br/>

## Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/35 Chats/20 🤔 Prompts/🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
...
| 🗄️ [Vault](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) | ✅ Done. Your wallet is bound.
| | | > Broker 🤵 |
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 What do you need? <br/> - [ Unbind ] vault <br/> - [ Something else ] | > Unbind
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Which codes? [All, No] <br/> - [ ] Some schema code 🧩 <br/> - [ ] Some other schema code 🧩 | > All
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | ✅ Codes unbound.
||

<br/>


## Flow diagram

![alt text](<.📎 Assets/⚙️ Unbind.png>)


| # | Call | Notes
|-|-|-
| 1 | [🧑‍🦰🐌🤗 `Home@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Home.md>) | Call the [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) in a [Chat 💬](<../../../4 ⚙️ Solution/35 Chats/12 💬 Chats/💬 Chat.md>)  with a [Host 🤗](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) 
| 2 | [🤗⏩🧑‍🦰 `Prompt@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Ask the [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) to remove the  [Bind 🔗](<../../../4 ⚙️ Solution/30 Data/20 🔗 Binds/🔗 Bind.md>)
| 3 | [🤵🐌🗄️ `Unbound@Vault`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🅰️ Vault methods/🤵🐌🗄️ Unbind.md>) | The [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) unbinds and informs the [Vault 🗄️](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>)
| 4 | [🤵⏩🧑‍🦰 Update Binds 🔗](<../../10 🤵⏩ Brokers/06 🤵⏩🧑‍🦰 Update Binds 🔗.md>) | Asks the [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) to update the [Binds 🔗](<../../../4 ⚙️ Solution/30 Data/20 🔗 Binds/🔗 Bind.md>)
|
