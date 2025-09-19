# 🧑‍🦰👉🤗 Chat home @ [Wallet](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)


## Chat


| Service | Prompt | User
| - | - | - |
...
| 🤗 [Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) | 😃 Lost is maze? [Yes, No] 
| | | > Broker 🤵 |
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 What do you need? <br/> - [ Home ] menu <br/> - [ Something else ] | > Home
| 🤗 [Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) | 😃 What do you need? <br/> - [ Something ] <br> - [ Something else ]  | 
||


## Flow Diagram

![Talker](<.📎 Assets/⚙️ Home.png>)


| # | Call | Notes
|-|-|-
| 1 | [🧑‍🦰🐌🤗 Home @ Host](<../../../6 🅰️ APIs/09 🤗🅰️ Host/02 🧑‍🦰🐌🤗 Home.md>) | Ask the [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) to show the talker 
| 2 | [🤗⏩🧑‍🦰 Prompt @ Host](<../../03 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | Show the home menu in the [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
||


| # | Call | Notes
|-|-|-
| 1 | [🧑‍🦰🐌🤗 Home @ Host](<../../../6 🅰️ APIs/09 🤗🅰️ Host/02 🧑‍🦰🐌🤗 Home.md>) | Call the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) in a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>)  with a [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) 
| 2 | [🤗⏩🧑‍🦰 Prompt @ Host](<../../03 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | Ask the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) to abandon the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) 
| 3 | [🤵🐌🤗 Abandoned @ Host](<../../../6 🅰️ APIs/09 🤗🅰️ Host/03 🤵🐌🤗 Abandoned.md>) | The [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) informs the [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) about it
| 4 | [🤵⏩🧑‍🦰 Update Chats @ Broker](<../../08 🤵⏩ Brokers/05 🤵⏩🧑‍🦰 Update chats.md>) | The [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) asks the [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to refresh the list