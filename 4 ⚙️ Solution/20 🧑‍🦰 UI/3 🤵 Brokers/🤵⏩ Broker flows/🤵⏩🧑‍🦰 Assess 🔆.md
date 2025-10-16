# 🤵⏩🧑‍🦰 Assess @ Broker

* Given a [Locator 🔆](<../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>)
    * parses the [Locator 🔆](<../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) in the [Broker 🤵](<../🤵🤲 Broker helper.md>)
    * and opens a [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) on the [Wallet 🧑‍🦰 app](<../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>).
* Used by:
    * [🧑‍🦰👉🤗 Scan host QR](<../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet chats/in App 🏠/🧑‍🦰🔆🤗 Tap host locator.md>) flow
    * [🧑‍🦰👉🤗 Scan printer QR](<../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet chats/in App 🏠/🧑‍🦰🔆🖨️ Tap alias locator.md>) flow
    * [🧑‍🦰👉🤗 Prompt option](<../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet chats/in Prompts 🤔/🧑‍🦰👉🤗 Click locator 🔆.md>) flow
    * [🗄️⏩🧑‍🦰 Engage @ Vault 💬](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️⏩ Vault flows/🗄️⏩🧑‍🦰 Engage 💬.md>) flow

<br/>

## Chat

| [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| | | 🔆 [scan](<../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) |
| 🔎 [Finder](<../../../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) | ⓘ Any Host (4.8 ⭐) [+]
| 🤵 [Broker](<../🤵🤲 Broker helper.md>) | ⓘ From another chat: <br/>- [Return] to original chat
| 🤵 [Broker](<../🤵🤲 Broker helper.md>) | ⓘ Tokens shared [+]
| 🤗 [Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Received context [+]
| 🤗 [Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [ Bla ] <br/>- [ Something else ] | > Bla
||


<br/>


## Flow diagram

![New chat](<../.📎 Assets/⚙️🔆 Assess.png>)


| # | Call | Notes
|-|-|-|
|1|[🤵🚀🖨️ `Resolve@Printer`](<../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/👥🚀🖨️ Resolve.md>) | Ask [Printers 🖨️](<../../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>) to resolve [`.ALIAS` 🧩](<../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>)
| 2 | [🤵⏩🧑‍🦰 Converse 🔆](<🤵⏩🧑‍🦰 Converse 💬.md>) | Ask [Wallets 🧑‍🦰](<../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)  to open a chat window
| 3 | [🔎⏩🧑‍🦰 Introduce 🤗](<../../../50 🫥 Agent domains/Finders 🔎/🔎⏩ Finder flows/🔎⏩🧑‍🦰 Introduce 🤗.md>) | Ask [Finders 🔎](<../../../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) to introduce [Hosts 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)
| 4 | [🔎⏩🧑‍🦰 Prompt ⓘ](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Finders 🔎](<../../../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) introduce [Hosts 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)
| 5 | [🤵⏩🧑‍🦰 Prompt ⓘ](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../🤵🤲 Broker helper.md>) reference original [Chats 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) 
| 6 | [🤵⏩🧑‍🦰 Prompt ⓘ](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../🤵🤲 Broker helper.md>) disclose shared [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) 
| 7 | [🤵🐌🤗 `Hello@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>) | Ask [Hosts 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) to interact
| 8 | [🤗⏩🧑‍🦰 Prompt ⓘ](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Context message from [Hosts 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
| 9 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Welcome message from [Hosts 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
||
