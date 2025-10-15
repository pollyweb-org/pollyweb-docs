# 🤗⏩🧑‍🦰 Freeze @ Host ❄️ 

* Activated by:
    * [❄️ Talker `FREEZE` command](<../../9 😃 Talkers/60 ⏩ Msg flows/42 ❄️ FREEZE msg.md>)
    * [💳 Talker `CHARGE` command](<../../9 😃 Talkers/60 ⏩ Msg flows/53 💳 CHARGE msg.md>)

<br/>

## ⏩ Flow diagram

![alt text](<.📎 Assets/⚙️❄️ Freeze.png>)

| # | Call | Notes
|-|-|-
|1|[🤗⏩🧑‍🦰 Prompt 🐶](<01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | The [Host 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) sends a first dog 🐶 prompt
|2|[🤗⏩🧑‍🦰 Prompt 🐱](<01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | The [Host 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) sends a second cat 🐱 prompt
|3|[🧑‍🦰🐌🤗 `Reply@Host`](<../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) | The user can still reply late to dog 🐶
|4|[🤗🐌🤵 `Freeze@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/07 🤗🐌🤵 Freeze.md>) | The [Host 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) freezes the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)
|5|[🤗⏩🧑‍🦰 Prompt 🐠](<01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | The [Host 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) sends a third fish  prompt 🐠
|6|[🧑‍🦰🐌🤗 `Reply@Host`](<../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) | The user can still reply to fish 🐠
|7| - | [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) block pre-freeze reply to cat 🐱
|8|[🧑‍🦰🐌🤗 `Reply@Host`](<../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) | Non-compliant [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) may try to reply
|9| - | [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) ignore rogue pre-freeze replies
|