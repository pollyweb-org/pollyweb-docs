# 🧑‍🦰👉🤗 Prompt option @ Wallet


> Implements a [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)


* On their [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    * users selects an [Option 🔘](<../../../9 😃 Talkers/20 🤔 Prompts/1 📘 Prompt specs/04 🔘 with Options.md>) with a [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) 
    * from a [Prompt 🤔](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) in a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>).


<br/>


## Flow diagram

![alt text](<.📎 Assets/⚙️🤔 Prompt option.png>)

| # | Call | Notes
|-|-|-
| 1 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Prompt 🤔](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) with [Locators 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) in [Options 🔘](<../../../9 😃 Talkers/20 🤔 Prompts/1 📘 Prompt specs/04 🔘 with Options.md>) 
| 2 | [🤵⏩🧑‍🦰 Assess 🔆](<../../10 🤵⏩ Brokers/01 🤵⏩🧑‍🦰 Assess 🔆.md>) | Parse the [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) in the [Broker 🤵](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>)
| 3 | [🤵🐌🤗 `Hello@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/01 🤵🐌🤗 Hello.md>) | Ask the [Host 🤗](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) to interact
| 4 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | The welcome message from the [Host 🤗](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) 
||
