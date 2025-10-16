# 🧑‍🦰👉🤵 Remove token @ Wallet


> Implements a [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)


* When users ask their [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) to remove a [Token 🎫](<../../../4 ⚙️ Solution/30 Data/30 🎫 Tokens/🎫 Token.md>),
  - it first does a soft delete only, hiding the [Token 🎫](<../../../4 ⚙️ Solution/30 Data/30 🎫 Tokens/🎫 Token.md>)
  - the removal only happens after a period of time (e.g., 30 days);
  - this allows users to undo the removal for a short period.

<br/>

## Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/35 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | > [Token 🎫](<../../../4 ⚙️ Solution/30 Data/30 🎫 Tokens/🎫 Token.md>)
| | | > [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) 
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>)  | 😃 What do you need? <br/> - [ Remove ] token | > Remove
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>)  | ✅ Token removed. <br/> - [ Undo ] removal
||



## Flow diagram

![alt text](<.📎 Assets/⚙️ Remove.png>)



| # | API | Description
|-|-|-
| 1 | [🧑‍🦰🐌🤗 `Home@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Home.md>) | The user calls the [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) from the [Token 🎫](<../../../4 ⚙️ Solution/30 Data/30 🎫 Tokens/🎫 Token.md>)
| 2 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Then tells the [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) to remove the [Token 🎫](<../../../4 ⚙️ Solution/30 Data/30 🎫 Tokens/🎫 Token.md>) 
| 3 | [🤵⏩🧑‍🦰 Update Tokens 🎫](<../../10 🤵⏩ Brokers/08 🤵⏩🧑‍🦰 Update Tokens 🎫.md>) | The [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) tells the [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) to update the list
| 4 | [🤵🐌📣 `Remove@Notifier`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/4 🎫 Tokens/3 🤵🐌📣 Remove.md>) | The [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) tells the [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) to remove it
||
