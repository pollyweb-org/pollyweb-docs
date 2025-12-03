# 🤗⏩🧑‍🦰 Invite @ Host

> Purpose

* A [Host 🤗 domain](<../../🤗 Host role/🤗🎭 Host role.md>) 
    * invites a [Helper 🤲 domain](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) 
    * to a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).
  
> Used in

* [💼⏩🧑‍🦰 Share Token+ID @ Consumer](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token+ID 👉🆔💼/🧑‍🦰 Share Token+ID ⏩ flow.md>) flow

> Examples

* [Split bill at a restaurant 🍽️](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/74 💳 Pay: Split bill ✂️.md>) use case
* [Confused senior user 👴🏻](<../../../../25 🔆 Locators/Userables 💍/💍⏩ Userable flows/💍📱 Senior user.md>) use case for [Userable 💍 things](<../../../../25 🔆 Locators/Userables 💍/💍💠 Userable thing.md>)

<br/>



## 💬 Chat

Consider the following [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) as an example.

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🤗 Host  | ℹ️ I'll ask my Helper for a random number. | 
| 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 [Allow invited guest?](<🤗 Invite ⏩ flow.md>) [Yes, No]  <br/> - Any Helper 🤲 <br/>- [ Always ] for Any Host  🤗 | > Yes
| 🤲 Helper | ℹ️ Hi! I'm Any Helper. The number is 27.    
| 🤗 Host  | ℹ️ 27, got it! Thanks, Any Helper!  
|

The associated [`Script`](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) is as follows.

```yaml
- INFO|I'll ask my Helper for a random number.
- INVITE >> $number:
    Invitee: host-b.dom
    Schema: any-authority.org/RANDOM-NUMBER
- INFO|{number}, got it! Thanks, Any Helper!  
```

Sure: [`INFO`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`INVITE`](<../../🤗⌘ Host cmds/INVITE 🤲/🤲 INVITE ⌘ cmd.md>)


<br/>


## ⏩ Flow diagram 


![alt text](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Invite 💼🐌🤵/🤵 Invite ⚙️ uml.png>)


|#| Step | Purpose
|-|-|-
|1|[💼🐌🤵 `Invite@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)|Invite another [Host 🤗](<../../🤗 Host role/🤗🎭 Host role.md>) to the [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
|2|[🤗⏩🧑‍🦰 Prompt 🤔](<../Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) may ask for user permission
|3| [🤵🐌🛠️ `Invited@Helper`](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited/🤲 Invited 🐌 msg.md>) | Proxy  invites to [Helper 🤲](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) invitees
|4|[🤗⏩🧑‍🦰 Prompt 🤔](<../Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | Invitees continue the [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
|5|[🗄️⏩💼 Consume 🧩](<../../../Vaults 🗄️/🗄️⏩ Vault flows/Consume 🗄️⏩💼/🗄️ Consume ⏩ flow.md>) | Invitees share the final result
|

<br/>