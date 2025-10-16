<!-- https://quip.com/b8a0AHaXf3C6#temp:C:DPS9f5401c512ad42d89656f6b4e -->

# 🧑‍🦰👉🗄️ Bind Vault @ Wallet 


* While the user is in a [Chat 💬](<../../../4 ⚙️ Solution/35 Chats/12 💬 Chats/💬 Chat.md>) with a [Vault 🗄️ host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>),
    * creates a [Bind 🔗](<../../../4 ⚙️ Solution/30 Data/20 🔗 Binds/🔗 Bind.md>) 
    * between the [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) 
    * and the [Vault 🗄️ domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>).

<br/>

## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/35 Chats/20 🤔 Prompts/🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🗄️ [Vault](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ] my Wallet | > Bind
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 [Bind?](<../../../9 😃 Talkers/60 ⏩ Msg flows/44 🔗 BIND msg.md>) [Yes, No] <br/> - Some schema code 🧩 <br/> - Some other schema code 🧩 | > Yes
| 🗄️ [Vault](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) | ✅ [Bound](<../../../4 ⚙️ Solution/35 Chats/20 🤔 Prompts/4 ⚠️ Status prompts/23 ✅ SUCCESS prompt.md>)
||

<br/>

## 😃 Talker 

The associated [Talker 😃](<../../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) uses the [`BIND` 🔗 command](<../../../9 😃 Talkers/60 ⏩ Msg flows/44 🔗 BIND msg.md>).

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
| 1 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Users ask [Vaults 🗄️](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) to [Bind 🔗](<../../../4 ⚙️ Solution/30 Data/20 🔗 Binds/🔗 Bind.md>) to their [Wallets 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) 
| 1 | [🗄️🐌🤵 `Bindable@Broker`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/40 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>)| [Vaults 🗄️](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) offer bindable [Schema Codes 🧩](<../../../4 ⚙️ Solution/30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)
| 2 | [👥🚀🕸 `Translate@Graph`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | [Brokers 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) translate to the user's language
| 3 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) ask for user confirmation 
| 4 | [🤵🐌🗄️ `Bound@Vault`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🅰️ Vault methods/🤵🐌🗄️ Bound.md>)| Tell [Vaults 🗄️](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) about each bound [Schema Code 🧩](<../../../4 ⚙️ Solution/30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)
| 5 | [🤵⏩🧑‍🦰 Update Binds 🔗](<../../10 🤵⏩ Brokers/06 🤵⏩🧑‍🦰 Update Binds 🔗.md>) | [Brokers 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) asks [Wallets 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) to update the [Binds 🔗](<../../../4 ⚙️ Solution/30 Data/20 🔗 Binds/🔗 Bind.md>)
|