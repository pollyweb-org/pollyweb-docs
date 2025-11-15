<!-- https://quip.com/b8a0AHaXf3C6#temp:C:DPS9f5401c512ad42d89656f6b4e -->

# 🧑‍🦰👉🗄️ Bind Vault @ Wallet 

> Purpose

* While the user is in a [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) with a [Vault 🗄️ host](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>),
    * creates a [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) 
    * between the [Wallet 🧑‍🦰 app](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) 
    * and the [Vault 🗄️ domain](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>).

<br/>

## 💬 Chat

| [Domain](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🗄️ [Vault](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ] my Wallet | > Bind
| 🤵 [Broker](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 [Bind?](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>) [Yes, No] <br/> - Some schema code 🧩 <br/> - Some other schema code 🧩 | > Yes
| 🗄️ [Vault](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | ✅ [Bound](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>)
||

<br/>

## 😃 Talker 

The associated [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) uses the [`BIND` 🔗 command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>).

```yaml
💬 [Bind] my Wallet:
- BIND:
    - some-authority.dom/SOME-CODE
    - another-authority.dom/ANOTHER-CODE
- SUCCESS: Bound
```


<br/>

## ⏩ Flow diagram

![alt text](<🧑‍🦰 Bind vault ⚙️ uml.png>)


| # | Call | Notes |
|-|-|-
| 1 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | Users ask [Vaults 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) to [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) to their [Wallets 🧑‍🦰](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) 
| 1 | [🗄️🐌🤵 `Bindable@Broker`](<../../../../Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>)| [Vaults 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) offer bindable [Schema Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
| 2 | [👥🚀🕸 `Translate@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>) | [Brokers 🤵](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) translate to the user's language
| 3 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Brokers 🤵](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) ask for user confirmation 
| 4 | [🤵🐌🗄️ `Bound@Vault`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)| Tell [Vaults 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) about each bound [Schema 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|