# 🤗⏩🧑‍🦰 Invite @ Host

* A [Host 🤗 domain](<../🤗🎭 Host role.md>) 
    * invites a [Helper 🤲 domain](<../../../45 🤲 Helper domains/$ 🤲 Helpers/🤲👥 Helper domain.md>) 
    * to a [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>).
  
* Used in:
    * [💼⏩🧑‍🦰 Share Token+ID @ Consumer](<../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/05 🧑‍🦰👉💼 Share Token+ID.md>) flow
  
* Examples: 
    * [Split bill at a restaurant 🍽️](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/74 💳 Pay: Split bill ✂️.md>) use case
    * [Confused senior user 👴🏻](<../../../25 Locators/74 💍 Userables/💍⏩ Userable flows/13 💍📱 Userable senior user.md>) use case for [Userable 💍 things](<../../../25 Locators/74 💍 Userables/💍💠 Userable thing.md>)

<br/>



## 💬 Chat

Consider the following [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>) as an example.

| [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🤗 Host  | ℹ️ I'll ask my Helper for a random number. | 
| 🤵 [Broker](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 [Allow invited guest?](<🤗⏩🧑‍🦰 Invite 🤲.md>) [Yes, No]  <br/> - Any Helper 🤲 <br/>- [ Always ] for Any Host  🤗 | > Yes
| 🤲 Helper | ℹ️ Hi! I'm Any Helper. The number is 27.    
| 🤗 Host  | ℹ️ 27, got it! Thanks, Any Helper!  
|

The associated [Talker 😃](<../../../35 Chats/😃 Talkers/😃 Talker.md>) is as follows.

```yaml
- INFO|I'll ask my Helper for a random number.
- INVITE >> $number:
    Invitee: host-b.com
    Code: any-authority.org/RANDOM-NUMBER
- INFO|{number}, got it! Thanks, Any Helper!  
```

| [Command ⌘](<../../../35 Chats/😃 Talkers/😃🌊 Talker flow/10 ⌘ Command.md>) | Purpose
|-|-
| ℹ️ [`INFO`](<../../../35 Chats/🤔 Prompts/🤔📢 Prompt status/21 ℹ️ INFO prompt.md>) | To show the messages to the user.
| 🛠️ [`INVITE`](<../../../35 Chats/😃 Talkers/😃📨 Talker msgs/46 🤲 INVITE msg.md>) | To collect a random number.
|


<br/>


## ⏩ Flow diagram 


![alt text](<../.📎 Assets/⚙️🤲 Invite.png>)


|#| Step | Purpose
|-|-|-
|1|[💼🐌🤵 `Invite@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Invite.md>)|Invite another [Host 🤗](<../🤗🎭 Host role.md>) to the [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>)
|2|[🤗⏩🧑‍🦰 Prompt 🤔](<🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) may ask for user permission
|3| [🤵🐌🛠️ `Invited@Helper`](<../../../45 🤲 Helper domains/$ 🤲 Helpers/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>) | Proxy  invites to [Helper 🤲](<../../../45 🤲 Helper domains/$ 🤲 Helpers/🤲👥 Helper domain.md>) invitees
|4|[🤗⏩🧑‍🦰 Prompt 🤔](<🤗⏩🧑‍🦰 Prompt 🤔.md>) | Invitees continue the [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>)
|5|[🗄️⏩💼 Consume 🧩](<../../80 🗄️ Vaults/🗄️⏩ Vault flows/🗄️⏩💼 Consume 🔗.md>) | Invitees share the final result
|

<br/>