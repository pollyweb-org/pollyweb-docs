# 🧑‍🦰👉🗄️ Bind Vault @ Wallet 

> Purpose

* While the user is in a [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) with a [Vault 🗄️ host](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>),
    * creates a [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) 
    * between the [Wallet 🧑‍🦰 app](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) 
    * and the [Vault 🗄️ domain](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>).

<br/>

## 💬 Chat

| [Domain](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🗄️ [Vault](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ] my Wallet | > Bind
| 🤵 [Broker](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 [Bind?](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️⌘ Vault cmds/BIND 🔗/🔗 BIND ⌘ cmd.md>) [Yes, No] <br/> - Some schema 🧩 <br/> - By Any Vault <br/> - Description: Bla, bla | > Yes
| 🗄️ [Vault](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) | ✅ [Bound!](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)
||

<br/>

## 😃 Talker 

The associated [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) uses the [`BIND` 🔗 command](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️⌘ Vault cmds/BIND 🔗/🔗 BIND ⌘ cmd.md>).

```yaml
💬 [Bind] my Wallet:
- BIND: some-authority.dom/SOME-CODE
- DONE: Bound!
```


<br/>

## ⏩ Flow diagram

![alt text](<🧑‍🦰 Bind Vault ⚙️ uml.png>)


| # | Call | Notes |
|-|-|-
| 1 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | 😃 Hi! What do you need?
| 2 | [🗄️🐌🤵 `Bind@Broker`](<../../../../Brokers 🤵/🤵📨 Broker msgs/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>)| [Vaults 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) offer a bindable [Schema  🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
| 3 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | 🫥 [Bind?](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️⌘ Vault cmds/BIND 🔗/🔗 BIND ⌘ cmd.md>) [Yes, No]
| 4 | [🤵🐌🗄️ `Bound@Vault`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️📨 Vault msgs/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)| Tell [Vaults 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) about the user answer
| 5 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | ✅ [Bound!](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)
|