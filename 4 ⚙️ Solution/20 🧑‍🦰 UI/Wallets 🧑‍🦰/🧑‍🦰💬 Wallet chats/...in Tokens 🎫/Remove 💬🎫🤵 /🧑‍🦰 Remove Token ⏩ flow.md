# 🧑‍🦰💬🤵 Remove token @ Wallet

> About
* Implements a [Wallet 🧑‍🦰 app](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
* Implemented by [`PopToken` 🔆 handler](<../../../../Brokers 🤵/🤵😃 Broker talkers/PopToken 🎫 talker/Token/🤵 PopToken 😃 handler.md>)

<br/>

## Chat 💬

| [Domain](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| | | > [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
| | | > [Broker 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) 
| 🤵 [Broker](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>)  | 😃 What do you need? <br/> - [ Remove ] token | > Remove
| 🤵 [Broker](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>)  | ✅ Token removed. <br/> - [ Undo ] removal
||

<br/>

## Flow diagram ⏩

![alt text](<🧑‍🦰 Remove Token ⚙️ uml.png>)



| # | API | Description
|-|-|-
| 1 | [`Locate@Broker` 🐌 msg](<../../../../Brokers 🤵/🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | The user calls the [Broker 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) from the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
| 2 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | Then tells the [Broker 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) to remove the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) 
| 3 | [🤵🐌📣 `Remove@Notifier`](<../../../../Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Remove 🤵🐌📣/📣 Remove 🐌 msg.md>) | The [Broker 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) tells the [Wallet 🧑‍🦰](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to remove it
||
