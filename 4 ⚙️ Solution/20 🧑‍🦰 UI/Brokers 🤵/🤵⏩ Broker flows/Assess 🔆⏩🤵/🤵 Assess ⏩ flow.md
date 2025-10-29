# 🤵⏩🧑‍🦰 Assess @ Broker

> Implemented by the [`Assess` 📃 handler](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 📃 handler.md>)

> Purpose

* Given a [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
    * parses the [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) in the [Broker 🤵](<../../🤵🤲 Broker helper.md>)
    * and opens a [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) on the [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).

> Used by

* [🧑‍🦰👉🤗 Scan host QR](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Tap host locator 🔆🤗 /🧑‍🦰 Tap host locator ⏩ flow.md>) flow
* [🧑‍🦰👉🤗 Scan printer QR](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Tap alias locator 🔆🖨️ /🔆🖨️ Tap alias locator ⏩ flow.md>) flow
* [🧑‍🦰👉🤗 Prompt option](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Click locator 👉🔆🤗/👉🤗 Click locator ⏩ flow.md>) flow
* [🗄️⏩🧑‍🦰 Engage @ Vault 💬](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️⏩ Vault flows/Engage 🗄️⏩💬/🗄️ Engage ⏩ flow.md>) flow

<br/>

## Chat

| [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| | | 🔆 [scan](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) |
| 🔎 [Finder](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) | ⓘ Any Host (4.8 ⭐) [+]
| 🤵 [Broker](<../../🤵🤲 Broker helper.md>) | ⓘ From another chat: <br/>- [Return] to original chat
| 🤵 [Broker](<../../🤵🤲 Broker helper.md>) | ⓘ Tokens shared [+]
| 🤗 [Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Received context [+]
| 🤗 [Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [ Bla ] <br/>- [ Something else ] | > Bla
||


<br/>


## Flow diagram

![New chat](<🤵 Assess ⚙️ uml.png>)


| # | Call | Notes
|-|-|-|
|0|[🧑‍🦰🐌🤵 `Assess@Broker`](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>) | Parse the [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
|1|[🤵🚀🖨️ `Resolve@Printer`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/Resolve 👥🚀🖨️/🖨️ Resolve 🚀 request.md>) | Ask [Printers 🖨️](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>) to resolve [`.ALIAS` 🧩](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>)
| 2 | [🤵⏩🧑‍🦰 Converse 🔆](<../Converse 🤵⏩💬/🤵 Converse ⏩ flow.md>) | Ask [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  to open a chat window
| 3 | [🔎⏩🧑‍🦰 Introduce 🤗](<../../../../50 🫥 Agent domains/Finders 🔎/🔎⏩ Finder flows/🔎⏩🧑‍🦰 Introduce 🤗.md>) | Ask [Finders 🔎](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) to introduce [Hosts 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)
| 4 | [🔎⏩🧑‍🦰 Prompt ⓘ](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Finders 🔎](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) introduce [Hosts 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)
| 5 | [🤵⏩🧑‍🦰 Prompt ⓘ](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Brokers 🤵](<../../🤵🤲 Broker helper.md>) reference original [Chats 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) 
| 6 | [🤵⏩🧑‍🦰 Prompt ⓘ](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Brokers 🤵](<../../🤵🤲 Broker helper.md>) disclose shared [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) 
| 7 | [🤵🐌🤗 `Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) | Ask [Hosts 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) to interact
| 8 | [🤗⏩🧑‍🦰 Prompt ⓘ](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | Context message from [Hosts 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
| 9 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | Welcome message from [Hosts 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
||
