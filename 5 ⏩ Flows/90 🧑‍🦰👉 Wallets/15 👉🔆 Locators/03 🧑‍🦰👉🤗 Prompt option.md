# 🧑‍🦰👉🤗 Prompt option @ Wallet


> Implements a [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)


* On their [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    * users selects an [Option 🔘](<../../../4 ⚙️ Solution/35 Chats/🤔 Prompts/🤔📘 Prompt features/04 🔘 with Options.md>) with a [Locator 🔆](<../../../4 ⚙️ Solution/25 Locators/15 🔆 Locators/🔆 Locator.md>) 
    * from a [Prompt 🤔](<../../../4 ⚙️ Solution/35 Chats/🤔 Prompts/🤔 Prompt.md>) in a [Chat 💬](<../../../4 ⚙️ Solution/35 Chats/💬 Chats/💬 Chat.md>).


<br/>


## Flow diagram

![alt text](<.📎 Assets/⚙️🤔 Prompt option.png>)

| # | Call | Notes
|-|-|-
| 1 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Prompt 🤔](<../../../4 ⚙️ Solution/35 Chats/🤔 Prompts/🤔 Prompt.md>) with [Locators 🔆](<../../../4 ⚙️ Solution/25 Locators/15 🔆 Locators/🔆 Locator.md>) in [Options 🔘](<../../../4 ⚙️ Solution/35 Chats/🤔 Prompts/🤔📘 Prompt features/04 🔘 with Options.md>) 
| 2 | [🤵⏩🧑‍🦰 Assess 🔆](<../../10 🤵⏩ Brokers/01 🤵⏩🧑‍🦰 Assess 🔆.md>) | Parse the [Locator 🔆](<../../../4 ⚙️ Solution/25 Locators/15 🔆 Locators/🔆 Locator.md>) in the [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>)
| 3 | [🤵🐌🤗 `Hello@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>) | Ask the [Host 🤗](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) to interact
| 4 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | The welcome message from the [Host 🤗](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) 
||
