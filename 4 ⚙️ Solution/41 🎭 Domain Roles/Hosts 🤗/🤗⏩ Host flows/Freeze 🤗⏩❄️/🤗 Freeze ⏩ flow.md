# 🤗⏩🧑‍🦰 Freeze @ Host ❄️ 

* Activated by:
    * [❄️ Talker `FREEZE` command](<../../../../35 💬 Chats/Scripts 📃/📃 methods 🤵/FREEZE ❄️/❄️ FREEZE ⌘ cmd.md>)
    * [💳 Talker `CHARGE` command](<../../../../35 💬 Chats/Scripts 📃/📃 methods 🤵/CHARGE 💳/💳 CHARGE ⌘ cmd.md>)

<br/>

## ⏩ Flow diagram

![alt text](<⚙️❄️ Freeze.png>)

| # | Call | Notes
|-|-|-
|1|[🤗⏩🧑‍🦰 Prompt 🐶](<../Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | The [Host 🤗](<../../🤗 Host role/🤗🎭 Host role.md>) sends a first dog 🐶 prompt
|2|[🤗⏩🧑‍🦰 Prompt 🐱](<../Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | The [Host 🤗](<../../🤗 Host role/🤗🎭 Host role.md>) sends a second cat 🐱 prompt
|3|[🧑‍🦰🐌🤗 `Reply@Host`](<../../🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>) | The user can still reply late to dog 🐶
|4|[🤗🐌🤵 `Freeze@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Freeze 🤗🐌🤵/🤵 Freeze 🐌 msg.md>) | The [Host 🤗](<../../🤗 Host role/🤗🎭 Host role.md>) freezes the [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
|5|[🤗⏩🧑‍🦰 Prompt 🐠](<../Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | The [Host 🤗](<../../🤗 Host role/🤗🎭 Host role.md>) sends a third fish  prompt 🐠
|6|[🧑‍🦰🐌🤗 `Reply@Host`](<../../🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>) | The user can still reply to fish 🐠
|7| - | [Wallets 🧑‍🦰](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰🛠️ Wallet app.md>) block pre-freeze reply to cat 🐱
|8|[🧑‍🦰🐌🤗 `Reply@Host`](<../../🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>) | Non-compliant [Wallets 🧑‍🦰](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰🛠️ Wallet app.md>) may try to reply
|9| - | [Hosts 🤗](<../../🤗 Host role/🤗🎭 Host role.md>) ignore rogue pre-freeze replies
|