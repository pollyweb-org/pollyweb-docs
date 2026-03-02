# 🧑‍🦰👉🤗 Scan or tap `.ALIAS` Locator @ Wallet


> Implements a [Wallet 🧑‍🦰 app](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)


* The user scans a [Locator 🔆](<../../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) with their [Wallet 🧑‍🦰 app](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
* Scenario where the [Locator 🔆](<../../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) is managed by a [Printer 🖨️](<../../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>) domain.

<br/>

## Chat

| [Domain](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| | | 🔆 [scan](<../../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) |
| 🔎 [Finder](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Host (4.8 ⭐) [+]
| 🤗 [Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [ Something ] <br/>- [ Something else ] 
||


<br/>


## Flow diagram

![PrinterQR](<🧑‍🦰 Tap alias locator ⚙️ uml.png>)


| # | Call | Notes
|-|-|-
| 1 | [👥🐌🏭 `Order@Supplier`](<../../../../../41 🎭 Domain Roles/Suppliers 🏭/🏭📨 Supplier msgs/👥🐌🏭 Order.md>) | Order dynamic [Locators 🔆](<../../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
| 2 | [🤵⏩🧑‍🦰 Locate 🔆](<../../../../Brokers 🤵/🤵⏩ Broker flows/Locate 🔆⏩🤵/🤵 Locate ⏩ flow.md>) | Parse the [Locator 🔆](<../../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) in the [Broker 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>)
| 3 | [👥🚀🖨️ `Resolve@Printer`](<../../../../../45 🤲 Helper domains/Printers 🖨️/🖨️📨 Printer msgs/Resolve 👥🚀🖨️/🖨️ Resolve 🚀 call.md>) | Get the host's locator from the [Printer 🖨️](<../../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>)
| 4 | [🤵🐌🤗 `Hello@Host`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) | Ask the [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) to interact
| 5 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | The welcome message from the [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) 
||
