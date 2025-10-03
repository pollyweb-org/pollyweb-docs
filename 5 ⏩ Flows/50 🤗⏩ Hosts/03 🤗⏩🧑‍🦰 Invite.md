# 🤗⏩🧑‍🦰 Invite @ Host

> A [Host 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) invites another to a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).

> Used in the [💼⏩🧑‍🦰 Share Token+ID @ Consumer](<../20 💼⏩ Consumers/04 💼⏩🧑‍🦰 Share Token+ID.md>) flow.

> Examples: 
> <br/> • [Split bill at a restaurant 🍽️](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/74 💳 Pay: Split bill ✂️.md>) use case
> <br/> • [Confused senior user 👴🏻](<../../4 ⚙️ Solution/70 🌳 Ambient/74 💍 Brand Userables/13 💍📱 Userable senior user.md>) use case for [Userable 💍 things](<../../4 ⚙️ Solution/70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>).

<br/>



## 💬 Chat

Consider the following [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) as an example.

| Domain | Prompt | User
| - | - | - |
| 🤗 Host A | ℹ️ I'll ask Host B for a random number. | 
| 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Allow invited guest? [Yes, No]  <br/> - Host B 😶 <br/>- [ Always ] for Host A 🤗 | > Yes
| 😶 Host B | ⓘ Hi! I'm Host B. The number is 27.    
| 🤗 Host A | ℹ️ 27, got it! Thanks, Host B!  
|

<br/>

## 😃 Talker 😃

The associated [Talker 😃](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/01 😃 Talker.md>) would be the following.

```yaml
- INFO|I'll invite Host B.
- INVITE|host-b.com|any-authority.org/RANDOM-NUMBER >> my-number
    # Domain: host-b.com
    # Code: any-authority.org/RANDOM-NUMBER
    # Output: my-number
- INFO|{my-number}, got it! Thanks, Host B!
```

<br/>


## ⏩ Flow diagram 


![alt text](<.📎 Assets/⚙️ Invite.png>)


|#| Step | Purpose
|-|-|-
|1|[💼🐌🤵 Invite @ Broker](<../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>)|Invite another [Host 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) to the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
|2|[🤗⏩🧑‍🦰 Prompt 🤔](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) may ask for user permission
|3| [🤵🐌🤗 Invited @ Host](<../../6 🅰️ APIs/50 🤗🅰️ Host/11 🤵🐌🤗 Invited.md>) | Proxy the invite to the Invitee 
|4|[🤗⏩🧑‍🦰 Prompt 🤔](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | The invitee continues the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
|

<br/>