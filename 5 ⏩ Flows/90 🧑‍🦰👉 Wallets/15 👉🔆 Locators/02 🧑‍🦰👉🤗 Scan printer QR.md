# 🧑‍🦰👉🤗 Tap Printer Locator @ Wallet


> Implements a [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)


* The user scans a [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) with their [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
* Scenario where the [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) is managed by a [Printer 🖨️](<../../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>) domain.

<br/>

## Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Msgs/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [scan](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) |
| 🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Host (4.8 ⭐) [+]
| 🤗 [Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [ Something ] <br/>- [ Something else ] 
||


<br/>


## Flow diagram

![PrinterQR](<.📎 Assets/⚙️🖨️ Printer QR.png>)


| # | Call | Notes
|-|-|-
| 1 | [👥🐌🏭 `Order@Supplier`](<../../../6 🅰️ APIs/90 🏭🅰️ Supplier/01 👥🐌🏭 Order.md>) | Order dynamic [Locators 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>)
| 2 | [🤵⏩🧑‍🦰 Assess 🔆](<../../10 🤵⏩ Brokers/01 🤵⏩🧑‍🦰 Assess 🔆.md>) | Parse the [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) in the [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
| 3 | [👥🚀🖨️ `Resolve@Printer`](<../../../6 🅰️ APIs/75 🖨️🅰️ Printer/03 👥🚀🖨️ Resolve.md>) | Get the host's locator from the [Printer 🖨️](<../../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>)
| 4 | [🤵🐌🤗 `Hello@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/01 🤵🐌🤗 Hello.md>) | Ask the [Host 🤗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) to interact
| 5 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | The welcome message from the [Host 🤗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) 
||
