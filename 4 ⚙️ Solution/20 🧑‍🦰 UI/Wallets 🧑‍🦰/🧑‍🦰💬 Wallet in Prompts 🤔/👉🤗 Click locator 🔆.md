# 🧑‍🦰👉🤗 Prompt option @ Wallet


> Implements a [Wallet 🧑‍🦰 app](<../🧑‍🦰🛠️ Wallet app.md>)


* On their [Wallet 🧑‍🦰 app](<../🧑‍🦰🛠️ Wallet app.md>)
    * users selects an [Option 🔘](<../../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/4 🔘 with Options.md>) with a [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) 
    * from a [Prompt 🤔](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) in a [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>).


<br/>


## Flow diagram

![alt text](<../.📎 Assets/Locators 📎/⚙️🤔 Prompt option.png>)

| # | Call | Notes
|-|-|-
| 1 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Prompt 🤔](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) with [Locators 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) in [Options 🔘](<../../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/4 🔘 with Options.md>) 
| 2 | [🤵⏩🧑‍🦰 Assess 🔆](<../../Brokers 🤵/🤵⏩ Broker flows/🤵⏩🧑‍🦰 Assess 🔆.md>) | Parse the [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) in the [Broker 🤵](<../../Brokers 🤵/🤵🤲 Broker helper.md>)
| 3 | [🤵🐌🤗 `Hello@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>) | Ask the [Host 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) to interact
| 4 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | The welcome message from the [Host 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
||
