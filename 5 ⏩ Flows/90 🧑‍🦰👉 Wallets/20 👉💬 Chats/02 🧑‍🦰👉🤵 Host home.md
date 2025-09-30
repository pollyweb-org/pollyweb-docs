# 🧑‍🦰👉🤗 Chat home @ [Wallet](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)

> On the [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), ask to show the home menu of a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).

<br/>

## Chat


| Service | Prompt | User
| - | - | - |
...
| 🤗 [Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Lost is maze? [Yes, No] 
| | | > Broker 🤵 |
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 What do you need? <br/> - [ Home ] menu <br/> - [ Something else ] | > Home
| 🤗 [Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What do you need? <br/> - [ Something ] <br> - [ Something else ]  | 
||

<br/>

## Flow Diagram

![Talker](<.📎 Assets/⚙️ Home.png>)


| # | Call | Notes
|-|-|-
| 1 | [🧑‍🦰🐌🤵 Help @ Broker](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/07 🧑‍🦰🐌🤵 Help.md>) | Open the context menu
| 2 | [🤗⏩🧑‍🦰 Prompt @ Host](<../../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | Ask the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) to abandon the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) 
| 3 | [🧑‍🦰🐌🤗 Home @ Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/02 🤵🐌🤗 Home.md>) | Show the main menu
|
