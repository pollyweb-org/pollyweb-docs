<!-- https://quip.com/b8a0AHaXf3C6#temp:C:DPSe1a859381bc449598713c8c71 -->

# 🧑‍🦰👉🗄️ Unbind @ [Wallet](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) 

> Scenario: the user wants to unbind from a [Vault 🗄️ domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>).

<br/>

## Chat

| Service | Prompt | User
| - | - | - |
...
| 🗄️ [Vault](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) | ✅ Done. Your wallet is bound.
| | | > Broker 🤵 |
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 What do you need? <br/> - [ Unbind ] vault <br/> - [ Something else ] | > Unbind
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Which codes? [All, No] <br/> - [ ] Some schema code 🧩 <br/> - [ ] Some other schema code 🧩 | > All
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | ✅ Codes unbound.
||

<br/>


## Flow diagram

![alt text](<.📎 Assets/⚙️ Unbind.png>)


| # | Call | Notes
|-|-|-
| 1 | [🧑‍🦰🐌🤗 Home @ Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/02 🤵🐌🤗 Home.md>) | Call the [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) in a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)  with a [Host 🤗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) 
| 2 | [🤗⏩🧑‍🦰 Prompt @ Host](<../../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | Ask the [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) to remove the  [Bind 🔗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>)
| 3 | [🤵🐌🗄️ Unbound @ Vault](<../../../6 🅰️ APIs/95 🗄️🅰️ Vault/02 🤵🐌🗄️ Unbind.md>) | The [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) unbinds and informs the [Vault 🗄️](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)
| 4 | [🤵⏩🧑‍🦰 Update Binds @ Broker](<../../10 🤵⏩ Brokers/03 🤵⏩🧑‍🦰 Update binds.md>) | Asks the [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to update the [Binds 🔗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>)
|
