<!-- https://quip.com/b8a0AHaXf3C6#temp:C:DPS9f5401c512ad42d89656f6b4e -->

# 🧑‍🦰👉🗄️ Bind Vault @ Wallet 


* While the user is in a [Chat 💬](<../../../../35 Chats/💬 Chats/💬 Chat.md>) with a [Vault 🗄️ host](<../../../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>),
    * creates a [Bind 🔗](<../../../../30 Data/2 🔗 Binds/🔗 Bind.md>) 
    * between the [Wallet 🧑‍🦰 app](<../../🧑‍🦰 Wallet app.md>) 
    * and the [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>).

<br/>

## 💬 Chat

| [Domain](<../../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../../35 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🗄️ [Vault](<../../../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ] my Wallet | > Bind
| 🤵 [Broker](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 [Bind?](<../../../../55 👷 Build domains/3 😃 Talkers/😃📨 Talker msgs/44 🔗 BIND msg.md>) [Yes, No] <br/> - Some schema code 🧩 <br/> - Some other schema code 🧩 | > Yes
| 🗄️ [Vault](<../../../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) | ✅ [Bound](<../../../../35 Chats/🤔 Prompts/🤔📢 Prompt status/23 ✅ SUCCESS prompt.md>)
||

<br/>

## 😃 Talker 

The associated [Talker 😃](<../../../../55 👷 Build domains/3 😃 Talkers/😃 Talker.md>) uses the [`BIND` 🔗 command](<../../../../55 👷 Build domains/3 😃 Talkers/😃📨 Talker msgs/44 🔗 BIND msg.md>).

```yaml
💬 [Bind] my Wallet:
- BIND:
    - some-authority.com/SOME-CODE
    - another-authority.com/ANOTHER-CODE
- SUCCESS: Bound
```


<br/>

## ⏩ Flow diagram

![alt text](<.📎 Assets/⚙️ Bind vault.png>)


| # | Call | Notes |
|-|-|-
| 1 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Users ask [Vaults 🗄️](<../../../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) to [Bind 🔗](<../../../../30 Data/2 🔗 Binds/🔗 Bind.md>) to their [Wallets 🧑‍🦰](<../../🧑‍🦰 Wallet app.md>) 
| 1 | [🗄️🐌🤵 `Bindable@Broker`](<../../../3 🤵 Brokers/🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>)| [Vaults 🗄️](<../../../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) offer bindable [Schema Codes 🧩](<../../../../30 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)
| 2 | [👥🚀🕸 `Translate@Graph`](<../../../../45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | [Brokers 🤵](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) translate to the user's language
| 3 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) ask for user confirmation 
| 4 | [🤵🐌🗄️ `Bound@Vault`](<../../../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🅰️ Vault methods/🤵🐌🗄️ Bound.md>)| Tell [Vaults 🗄️](<../../../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) about each bound [Schema Code 🧩](<../../../../30 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)
| 5 | [🤵⏩🧑‍🦰 Update Binds 🔗](<../../../3 🤵 Brokers/🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Binds 🔗.md>) | [Brokers 🤵](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) asks [Wallets 🧑‍🦰](<../../🧑‍🦰 Wallet app.md>) to update the [Binds 🔗](<../../../../30 Data/2 🔗 Binds/🔗 Bind.md>)
|