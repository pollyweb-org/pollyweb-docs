# 🧑‍🦰💬🤵 Remove token @ Wallet


> Implements a [Wallet 🧑‍🦰 app](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)

> Implemented by [`Pop Token` 📃 script](<../../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🎫 PopToken/🤵 PopToken 📃 handler.md>)


* When users ask their [Broker 🤵](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) to remove a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>),
  - it first does a soft delete only, hiding the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
  - the removal only happens after a period of time (e.g., 30 days);
  - this allows users to undo the removal for a short period.

<br/>

## Chat 💬

> Implemented by [Pop Token 🔆 handler](<../../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🎫 PopToken/🤵 PopToken 📃 handler.md>).

| [Domain](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| | | > [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
| | | > [Broker 🤵](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) 
| 🤵 [Broker](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>)  | 😃 What do you need? <br/> - [ Remove ] token | > Remove
| 🤵 [Broker](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>)  | ✅ Token removed. <br/> - [ Undo ] removal
||

<br/>

## Flow diagram ⏩

![alt text](<🧑‍🦰 Remove Token ⚙️ uml.png>)



| # | API | Description
|-|-|-
| 1 | [🧑‍🦰🐌🤵 `Pop@Broker`](<../../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>)  | The user calls the [Broker 🤵](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) from the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
| 2 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | Then tells the [Broker 🤵](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) to remove the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) 
| 3 | [🤵⏩🧑‍🦰 Update Tokens 🎫](<../../../../Brokers 🤵/🤵⏩ Broker flows/Update Tokens 🤵⏩🎫/🤵 Update Tokens ⏩ flow.md>) | The [Broker 🤵](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) tells the [Wallet 🧑‍🦰](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to update the list
| 4 | [🤵🐌📣 `Remove@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Remove 🤵🐌📣/📣 Remove 🐌 msg.md>) | The [Broker 🤵](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) tells the [Wallet 🧑‍🦰](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to remove it
||
