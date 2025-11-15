# 🔎⏩🧑‍🦰 Present Host @ Finder 

> Purpose

* Ask the [Finder 🔎 domain](<../../🔎 Finder agent/🔎 Finder 🫥 agent.md>) 
    * to introduce the [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>)

> Used by
    
* [🧑‍🦰👉🤗 Scan host QR](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Tap host locator 🔆🤗 /🧑‍🦰 Tap host locator ⏩ flow.md>)
* [🧑‍🦰👉🤗 Scan printer QR](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Tap alias locator 🔆🖨️ /🧑‍🦰 Tap alias locator ⏩ flow.md>)

<br/>

## 💬 Chat

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
| 🔎 [Finder](<../../🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Host (4.3 ⭐): <br/> This host sells shoes.<br/>- They were founded in 1987.<br/>- Joined NLWeb 2 years ago.<br/>User feedback:<br/>- Delivery 4.7⭐ by 357 users<br/>- Support 3.5⭐ by 21 users
|

<br/>


## Flow diagram

![Present](<🔎 Present ⚙️ uml.png>)


| # | Call | Notes
|-|-|-
| 1 | [🤵🐌🔎 `Present@Finder`](<../../🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>) | Ask to introduce a [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).
| 2 | [🔎🚀⭐ `Reviews@Reviewer`](<../../../Reviewers ⭐/⭐🅰️ Reviewer methods/🔎🚀⭐ Reviews.md>) | Get domain reviews (may be cached).
| 3 | [👥🚀🕸 `About@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 About/🕸 About 🚀 call.md>) | Get domain identity (may be cached).
| 4 | [👥🚀🕸 `Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>) | Get domain translations (may be cached).
| 5 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | Inform the user.
| 6 | [🔎🐌🤵 `Presented@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Presented 🔎🐌🤵/🤵 Presented 🐌 msg.md>) | Finish introduction.
||