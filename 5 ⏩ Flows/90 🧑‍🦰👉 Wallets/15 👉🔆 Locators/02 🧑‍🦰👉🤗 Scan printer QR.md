# 🧑‍🦰👉🤗 Tap Printer Locator @ Wallet


> Implements a [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)


* The user scans a [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) with their [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>).
* Scenario where the [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) is managed by a [Printer 🖨️](<../../../4 ⚙️ Solution/45 🤲 Helper domains/75 🖨️ Printers/🖨️🤲 Printer helper.md>) domain.

<br/>

## Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [scan](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) |
| 🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agents/40 🔎 Finders/🔎🫥 Finder agent.md>) | ⓘ Any Host (4.8 ⭐) [+]
| 🤗 [Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [ Something ] <br/>- [ Something else ] 
||


<br/>


## Flow diagram

![PrinterQR](<.📎 Assets/⚙️🖨️ Printer QR.png>)


| # | Call | Notes
|-|-|-
| 1 | [👥🐌🏭 `Order@Supplier`](<../../../6 🅰️ APIs/90 🏭🅰️ Supplier/01 👥🐌🏭 Order.md>) | Order dynamic [Locators 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>)
| 2 | [🤵⏩🧑‍🦰 Assess 🔆](<../../10 🤵⏩ Brokers/01 🤵⏩🧑‍🦰 Assess 🔆.md>) | Parse the [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) in the [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>)
| 3 | [👥🚀🖨️ `Resolve@Printer`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/75 🖨️ Printers/🖨️🅰️ Printer methods/👥🚀🖨️ Resolve.md>) | Get the host's locator from the [Printer 🖨️](<../../../4 ⚙️ Solution/45 🤲 Helper domains/75 🖨️ Printers/🖨️🤲 Printer helper.md>)
| 4 | [🤵🐌🤗 `Hello@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>) | Ask the [Host 🤗](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) to interact
| 5 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | The welcome message from the [Host 🤗](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) 
||
