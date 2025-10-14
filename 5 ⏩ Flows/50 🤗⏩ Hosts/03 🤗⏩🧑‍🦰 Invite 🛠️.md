# 🤗⏩🧑‍🦰 Invite @ Host

* A [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) 
    * invites a [Helper 🛠️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) 
    * to a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).
  
* Used in:
    * [💼⏩🧑‍🦰 Share Token+ID @ Consumer](<../90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/05 🧑‍🦰👉💼 Share Token+ID.md>) flow
  
* Examples: 
    * [Split bill at a restaurant 🍽️](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/74 💳 Pay: Split bill ✂️.md>) use case
    * [Confused senior user 👴🏻](<../../4 ⚙️ Solution/70 🌳 Ambient/74 💍 Brand Userables/13 💍📱 Userable senior user.md>) use case for [Userable 💍 things](<../../4 ⚙️ Solution/70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>)

<br/>



## 💬 Chat

Consider the following [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) as an example.

| [Domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Msgs/00 👥 Domain.md>) | [Prompt](<../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🤗 Host  | ℹ️ I'll ask my Helper for a random number. | 
| 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Allow invited guest?](<03 🤗⏩🧑‍🦰 Invite 🛠️.md>) [Yes, No]  <br/> - Any Helper 🛠️ <br/>- [ Always ] for Any Host  🤗 | > Yes
| 🛠️ Helper | ℹ️ Hi! I'm Any Helper. The number is 27.    
| 🤗 Host  | ℹ️ 27, got it! Thanks, Any Helper!  
|

The associated [Talker 😃](<../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) is as follows.

```yaml
- INFO|I'll ask my Helper for a random number.
- INVITE >> $number:
    Invitee: host-b.com
    Code: any-authority.org/RANDOM-NUMBER
- INFO|{number}, got it! Thanks, Any Helper!  
```

| [Command ⌘](<../../9 😃 Talkers/40 🌊 Talker flows/10 ⌘ Command.md>) | Purpose
|-|-
| ℹ️ [`INFO`](<../../9 😃 Talkers/20 🤔 Prompts/4 ⚠️ Status prompts/21 ℹ️ INFO prompt.md>) | To show the messages to the user.
| 🛠️ [`INVITE`](<../../9 😃 Talkers/60 ⏩ Msg flows/46 🛠️ INVITE msg.md>) | To collect a random number.
|


<br/>


## ⏩ Flow diagram 


![alt text](<.📎 Assets/⚙️🛠️ Invite.png>)


|#| Step | Purpose
|-|-|-
|1|[💼🐌🤵 `Invite@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>)|Invite another [Host 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) to the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
|2|[🤗⏩🧑‍🦰 Prompt 🤔](<01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) may ask for user permission
|3| [🤵🐌🛠️ `Invited@Helper`](<../../6 🅰️ APIs/49 🛠️🅰️ Helper/11 🤵🐌🛠️ Invited.md>) | Proxy  invites to [Helper 🛠️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) invitees
|4|[🤗⏩🧑‍🦰 Prompt 🤔](<01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | Invitees continue the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
|5|[🗄️⏩💼 Consume 🧩](<../80 🗄️⏩ Vaults/02 🗄️⏩💼 Consume 🔗.md>) | Invitees share the final result
|

<br/>