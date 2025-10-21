# 🧑‍🦰💬🤵 Remove token @ Wallet


> Implements a [Wallet 🧑‍🦰 app](<../🧑‍🦰🛠️ Wallet app.md>)

> Implemented by [`Pop Token` 📃 script](<../../Brokers 🤵/🤵📃 Broker scripts/...others/🤵📃 Pop Token 🎫.md>)


* When users ask their [Broker 🤵](<../../Brokers 🤵/🤵🤲 Broker helper.md>) to remove a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>),
  - it first does a soft delete only, hiding the [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
  - the removal only happens after a period of time (e.g., 30 days);
  - this allows users to undo the removal for a short period.

<br/>

## Chat 💬

> Implemented by [Pop Token 🔆 handler](<../../Brokers 🤵/🤵📃 Broker scripts/...others/🤵📃 Pop Token 🎫.md>).

| [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| | | > [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
| | | > [Broker 🤵](<../../Brokers 🤵/🤵🤲 Broker helper.md>) 
| 🤵 [Broker](<../../Brokers 🤵/🤵🤲 Broker helper.md>)  | 😃 What do you need? <br/> - [ Remove ] token | > Remove
| 🤵 [Broker](<../../Brokers 🤵/🤵🤲 Broker helper.md>)  | ✅ Token removed. <br/> - [ Undo ] removal
||

<br/>

## Flow diagram ⏩

![alt text](<../.📎 Assets/Tokens 📎/⚙️🎫 Remove.png>)



| # | API | Description
|-|-|-
| 1 | [🧑‍🦰🐌🤵 `Pop@Broker`](<../../Brokers 🤵/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🐌🤵 Pop.md>)  | The user calls the [Broker 🤵](<../../Brokers 🤵/🤵🤲 Broker helper.md>) from the [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
| 2 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Then tells the [Broker 🤵](<../../Brokers 🤵/🤵🤲 Broker helper.md>) to remove the [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) 
| 3 | [🤵⏩🧑‍🦰 Update Tokens 🎫](<../../Brokers 🤵/🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Tokens 🎫.md>) | The [Broker 🤵](<../../Brokers 🤵/🤵🤲 Broker helper.md>) tells the [Wallet 🧑‍🦰](<../🧑‍🦰🛠️ Wallet app.md>) to update the list
| 4 | [🤵🐌📣 `Remove@Notifier`](<../../Notifiers 📣/📣🅰️ Notifier methods/4 🎫 Tokens/3 🤵🐌📣 Remove.md>) | The [Broker 🤵](<../../Brokers 🤵/🤵🤲 Broker helper.md>) tells the [Wallet 🧑‍🦰](<../🧑‍🦰🛠️ Wallet app.md>) to remove it
||
