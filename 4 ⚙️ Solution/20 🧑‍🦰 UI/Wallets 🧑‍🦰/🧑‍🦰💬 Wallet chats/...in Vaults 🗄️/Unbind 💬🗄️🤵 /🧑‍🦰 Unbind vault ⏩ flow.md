# 🧑‍🦰💬🤵 Unbind @ Wallet

> Implemented by the [`Pop Vault` script](<../../../../Brokers 🤵/🤵😃 Broker talkers/PopBind 🔗 talker/Bind » Remove/🤵 PopBindRemove 😃 handler.md>).

> Implements a [Wallet 🧑‍🦰 app](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)


* Scenario: the user wants to unbind from a [Vault 🗄️ domain](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>).

<br/>

## Chat

> Implemented by [Pop Vault 🔆 handler](<../../../../Brokers 🤵/🤵😃 Broker talkers/PopBind 🔗 talker/Bind » Remove/🤵 PopBindRemove 😃 handler.md>).

| [Domain](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
...
| 🗄️ [Vault](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) | ✅ Done. Your wallet is bound.
| | | > Broker 🤵 |
| 🤵 [Broker](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 What do you need? <br/> - [ Unbind ] vault <br/> - [ Something else ] | > Unbind
| 🤵 [Broker](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 Which codes? [All, No] <br/> - [ ] Some schema code 🧩 <br/> - [ ] Some other schema code 🧩 | > All
| 🤵 [Broker](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | ✅ Codes unbound.
||

<br/>


## Flow diagram

![alt text](<🧑‍🦰 Unbind Vault ⚙️ uml.png>)


| # | Call | Notes
|-|-|-
| 1 | [`Locate@Broker` 🐌 msg](<../../../../Brokers 🤵/🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | Call the [Broker 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) in a [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)  with a [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) 
| 2 | [🤗⏩🧑‍🦰 `Prompt@Host`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | Ask the [Broker 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) to remove the  [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
| 3 | [🤵🐌🗄️ `Unbound@Vault`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️📨 Vault msgs/Unbound 🤵🐌🗄️/🗄️ Unbound 🐌 msg.md>) | The [Broker 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) unbinds and informs the [Vault 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>)
|



<br/>
