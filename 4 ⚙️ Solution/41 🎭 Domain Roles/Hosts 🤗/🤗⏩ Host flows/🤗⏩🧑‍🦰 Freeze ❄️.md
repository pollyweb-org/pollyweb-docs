# 🤗⏩🧑‍🦰 Freeze @ Host ❄️ 

* Activated by:
    * [❄️ Talker `FREEZE` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...methods 🤵/FREEZE/FREEZE ❄️ msg.md>)
    * [💳 Talker `CHARGE` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...methods 🤵/CHARGE/CHARGE 💳 msg.md>)

<br/>

## ⏩ Flow diagram

![alt text](<../.📎 Assets/⚙️❄️ Freeze.png>)

| # | Call | Notes
|-|-|-
|1|[🤗⏩🧑‍🦰 Prompt 🐶](<🤗⏩🧑‍🦰 Prompt 🤔.md>) | The [Host 🤗](<../🤗🎭 Host role.md>) sends a first dog 🐶 prompt
|2|[🤗⏩🧑‍🦰 Prompt 🐱](<🤗⏩🧑‍🦰 Prompt 🤔.md>) | The [Host 🤗](<../🤗🎭 Host role.md>) sends a second cat 🐱 prompt
|3|[🧑‍🦰🐌🤗 `Reply@Host`](<../🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply/🧑‍🦰🐌🤗 Reply.md>) | The user can still reply late to dog 🐶
|4|[🤗🐌🤵 `Freeze@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Freeze 🤗🐌🤵/🤵 Freeze 🐌 msg.md>) | The [Host 🤗](<../🤗🎭 Host role.md>) freezes the [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>)
|5|[🤗⏩🧑‍🦰 Prompt 🐠](<🤗⏩🧑‍🦰 Prompt 🤔.md>) | The [Host 🤗](<../🤗🎭 Host role.md>) sends a third fish  prompt 🐠
|6|[🧑‍🦰🐌🤗 `Reply@Host`](<../🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply/🧑‍🦰🐌🤗 Reply.md>) | The user can still reply to fish 🐠
|7| - | [Wallets 🧑‍🦰](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) block pre-freeze reply to cat 🐱
|8|[🧑‍🦰🐌🤗 `Reply@Host`](<../🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply/🧑‍🦰🐌🤗 Reply.md>) | Non-compliant [Wallets 🧑‍🦰](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) may try to reply
|9| - | [Hosts 🤗](<../🤗🎭 Host role.md>) ignore rogue pre-freeze replies
|