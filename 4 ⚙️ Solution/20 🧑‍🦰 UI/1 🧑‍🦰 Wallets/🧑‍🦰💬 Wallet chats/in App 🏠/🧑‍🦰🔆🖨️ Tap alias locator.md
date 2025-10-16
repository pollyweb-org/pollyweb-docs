# 🧑‍🦰👉🤗 Scan or tap `.ALIAS` Locator @ Wallet


> Implements a [Wallet 🧑‍🦰 app](<../../🧑‍🦰🛠️ Wallet app.md>)


* The user scans a [Locator 🔆](<../../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) with their [Wallet 🧑‍🦰 app](<../../🧑‍🦰🛠️ Wallet app.md>).
* Scenario where the [Locator 🔆](<../../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) is managed by a [Printer 🖨️](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>) domain.

<br/>

## Chat

| [Domain](<../../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| | | 🔆 [scan](<../../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) |
| 🔎 [Finder](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) | ⓘ Any Host (4.8 ⭐) [+]
| 🤗 [Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [ Something ] <br/>- [ Something else ] 
||


<br/>


## Flow diagram

![PrinterQR](<../../.📎 Assets/Locators 📎/⚙️🖨️ Printer QR.png>)


| # | Call | Notes
|-|-|-
| 1 | [👥🐌🏭 `Order@Supplier`](<../../../../41 🎭 Domain Roles/Suppliers 🏭/🏭🅰️ Supplier methods/👥🐌🏭 Order.md>) | Order dynamic [Locators 🔆](<../../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>)
| 2 | [🤵⏩🧑‍🦰 Assess 🔆](<../../../3 🤵 Brokers/🤵⏩ Broker flows/🤵⏩🧑‍🦰 Assess 🔆.md>) | Parse the [Locator 🔆](<../../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) in the [Broker 🤵](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>)
| 3 | [👥🚀🖨️ `Resolve@Printer`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/👥🚀🖨️ Resolve.md>) | Get the host's locator from the [Printer 🖨️](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>)
| 4 | [🤵🐌🤗 `Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>) | Ask the [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) to interact
| 5 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | The welcome message from the [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
||
