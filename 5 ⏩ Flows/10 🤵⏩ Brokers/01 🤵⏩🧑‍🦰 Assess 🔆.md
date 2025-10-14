# 🤵⏩🧑‍🦰 Assess @ Broker

* Given a [Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>)
    * parses the [Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) in the [Broker 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
    * and opens a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) on the [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
* Used by:
    * [🧑‍🦰👉🤗 Scan host QR](<../90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/01 🧑‍🦰👉🤗 Scan host QR.md>) flow
    * [🧑‍🦰👉🤗 Scan printer QR](<../90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/02 🧑‍🦰👉🤗 Scan printer QR.md>) flow
    * [🧑‍🦰👉🤗 Prompt option](<../90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/03 🧑‍🦰👉🤗 Prompt option.md>) flow
    * [🗄️⏩🧑‍🦰 Engage @ Vault 💬](<../80 🗄️⏩ Vaults/04 🗄️⏩🧑‍🦰 Engage 💬.md>) flow

<br/>

## Chat

| [Domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/00 👥 Domain.md>) | [Prompt](<../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [scan](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) |
| 🔎 [Finder](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Host (4.8 ⭐) [+]
| 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ From another chat: <br/>- [Return] to original chat
| 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Tokens shared [+]
| 🤗 [Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Received context [+]
| 🤗 [Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [ Bla ] <br/>- [ Something else ] | > Bla
||


<br/>


## Flow diagram

![New chat](<.📎 Assets/⚙️🔆 Assess.png>)


| # | Call | Notes
|-|-|-|
|1|[🤵🚀🖨️ `Resolve@Printer`](<../../6 🅰️ APIs/75 🖨️🅰️ Printer/03 👥🚀🖨️ Resolve.md>) | Ask [Printers 🖨️](<../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>) to resolve [`.ALIAS` 🧩](<../../7 🧩 Codes/$/🧩 Alias.md>)
| 2 | [🤵⏩🧑‍🦰 Converse 🔆](<03 🤵⏩🧑‍🦰 Converse 💬.md>) | Ask [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)  to open a chat window
| 3 | [🔎⏩🧑‍🦰 Introduce 🤗](<../40 🔎⏩ Finders/01 🔎⏩🧑‍🦰 Introduce 🤗.md>) | Ask [Finders 🔎](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) to introduce [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>)
| 4 | [🔎⏩🧑‍🦰 Prompt ⓘ](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Finders 🔎](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) introduce [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>)
| 5 | [🤵⏩🧑‍🦰 Prompt ⓘ](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) reference original [Chats 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) 
| 6 | [🤵⏩🧑‍🦰 Prompt ⓘ](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) disclose shared [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) 
| 7 | [🤵🐌🤗 `Hello@Host`](<../../6 🅰️ APIs/50 🤗🅰️ Host/01 🤵🐌🤗 Hello.md>) | Ask [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) to interact
| 8 | [🤗⏩🧑‍🦰 Prompt ⓘ](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | Context message from [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) 
| 9 | [🤗⏩🧑‍🦰 Prompt 🤔](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | Welcome message from [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) 
||
