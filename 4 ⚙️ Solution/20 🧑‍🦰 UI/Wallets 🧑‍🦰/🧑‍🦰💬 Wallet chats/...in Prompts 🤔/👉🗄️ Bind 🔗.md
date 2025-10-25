<!-- https://quip.com/b8a0AHaXf3C6#temp:C:DPS9f5401c512ad42d89656f6b4e -->

# 🧑‍🦰👉🗄️ Bind Vault @ Wallet 


* While the user is in a [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) with a [Vault 🗄️ host](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>),
    * creates a [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) 
    * between the [Wallet 🧑‍🦰 app](<../../🧑‍🦰🛠️ Wallet app.md>) 
    * and the [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>).

<br/>

## 💬 Chat

| [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| 🗄️ [Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ] my Wallet | > Bind
| 🤵 [Broker](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 [Bind?](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...methods 🤵/BIND 🔗/BIND 🔗 msg.md>) [Yes, No] <br/> - Some schema code 🧩 <br/> - Some other schema code 🧩 | > Yes
| 🗄️ [Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | ✅ [Bound](<../../../../35 💬 Chats/🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)
||

<br/>

## 😃 Talker 

The associated [Talker 😃](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) uses the [`BIND` 🔗 command](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...methods 🤵/BIND 🔗/BIND 🔗 msg.md>).

```yaml
💬 [Bind] my Wallet:
- BIND:
    - some-authority.com/SOME-CODE
    - another-authority.com/ANOTHER-CODE
- SUCCESS: Bound
```


<br/>

## ⏩ Flow diagram

![alt text](<../../.📎 Assets/Binds 📎/⚙️ Bind vault.png>)


| # | Call | Notes |
|-|-|-
| 1 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Users ask [Vaults 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) to [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) to their [Wallets 🧑‍🦰](<../../🧑‍🦰🛠️ Wallet app.md>) 
| 1 | [🗄️🐌🤵 `Bindable@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>)| [Vaults 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) offer bindable [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
| 2 | [👥🚀🕸 `Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | [Brokers 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) translate to the user's language
| 3 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) ask for user confirmation 
| 4 | [🤵🐌🗄️ `Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Bound.md>)| Tell [Vaults 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) about each bound [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
| 5 | [🤵⏩🧑‍🦰 Update Binds 🔗](<../../../Brokers 🤵/🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Binds 🔗.md>) | [Brokers 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) asks [Wallets 🧑‍🦰](<../../🧑‍🦰🛠️ Wallet app.md>) to update the [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
|