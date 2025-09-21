<!-- https://quip.com/b8a0AHaXf3C6#temp:C:DPS9f5401c512ad42d89656f6b4e -->

# 🧑‍🦰👉🗄️ Bind Vault @ Wallet 


> While the user is in a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) with a [Vault 🗄️ host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>), 
<br/>creates a [Bind 🔗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) between the [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and the [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>).


## Chat

| Service | Prompt | User
| - | - | - |
| ...
| 🗄️ [Vault](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) | 😃 What's the SMS code we sent? | 🔢 1234
| 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Bind to Any Vault? [All, No] <br/> - [ ] Some schema code 🧩 <br/> - [ ] Some other schema code 🧩 | > All
| 🗄️ [Vault](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) | ✅ Done. Your wallet is bound.


## Steps

| # | Call | Notes |
|-|-|-
| 1 | [🗄️🐌🤵 Bindable @ Broker](<../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/42 🗄️🐌🤵 Bindable.md>)| The [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) offers bindable [Schema Codes 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
| 2 | [👥🚀🕸 Translate @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/06 👥🚀🕸 Translate.md>) | The [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) translates them to the user's language
| 3 | [🤗⏩🧑‍🦰 Prompt @ Host](<../03 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | The [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) asks for user confirmation in the [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| 4 | [🤵⏩🗄️ Bind Vault @ Broker](<../08 🤵⏩ Brokers/02 🤵⏩🗄️ Bind vault.md>) | The [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) binds the [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to the [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)


## Flow diagram

![alt text](<.📎 Assets/⚙️ Bind vault.png>)
