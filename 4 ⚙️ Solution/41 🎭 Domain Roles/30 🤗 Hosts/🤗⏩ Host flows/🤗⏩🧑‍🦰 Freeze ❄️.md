# 🤗⏩🧑‍🦰 Freeze @ Host ❄️ 

* Activated by:
    * [❄️ Talker `FREEZE` command](<../../../90 👷 Build/3 😃 Talkers/😃📨 Talker msgs/42 ❄️ FREEZE msg.md>)
    * [💳 Talker `CHARGE` command](<../../../90 👷 Build/3 😃 Talkers/😃📨 Talker msgs/53 💳 CHARGE msg.md>)

<br/>

## ⏩ Flow diagram

![alt text](<../.📎 Assets/⚙️❄️ Freeze.png>)

| # | Call | Notes
|-|-|-
|1|[🤗⏩🧑‍🦰 Prompt 🐶](<🤗⏩🧑‍🦰 Prompt 🤔.md>) | The [Host 🤗](<../🤗🎭 Host role.md>) sends a first dog 🐶 prompt
|2|[🤗⏩🧑‍🦰 Prompt 🐱](<🤗⏩🧑‍🦰 Prompt 🤔.md>) | The [Host 🤗](<../🤗🎭 Host role.md>) sends a second cat 🐱 prompt
|3|[🧑‍🦰🐌🤗 `Reply@Host`](<../🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>) | The user can still reply late to dog 🐶
|4|[🤗🐌🤵 `Freeze@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🤗🐌🤵 Freeze.md>) | The [Host 🤗](<../🤗🎭 Host role.md>) freezes the [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>)
|5|[🤗⏩🧑‍🦰 Prompt 🐠](<🤗⏩🧑‍🦰 Prompt 🤔.md>) | The [Host 🤗](<../🤗🎭 Host role.md>) sends a third fish  prompt 🐠
|6|[🧑‍🦰🐌🤗 `Reply@Host`](<../🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>) | The user can still reply to fish 🐠
|7| - | [Wallets 🧑‍🦰](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) block pre-freeze reply to cat 🐱
|8|[🧑‍🦰🐌🤗 `Reply@Host`](<../🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>) | Non-compliant [Wallets 🧑‍🦰](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) may try to reply
|9| - | [Hosts 🤗](<../🤗🎭 Host role.md>) ignore rogue pre-freeze replies
|