# 🔎⏩🧑‍🦰 Introduce Host @ Finder 

> Purpose

* Ask the [Finder 🔎 domain](<../🔎🫥 Finder agent.md>) 
    * to introduce the [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)

> Used by
    
* [🧑‍🦰👉🤗 Scan host QR](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/🔆🤗 Tap host locator/🔆🤗 Tap host locator.md>)
* [🧑‍🦰👉🤗 Scan printer QR](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/🔆🖨️ Tap alias locator/🔆🖨️ Tap alias locator.md>)

<br/>

## 💬 Chat

| [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
| 🔎 [Finder](<../🔎🫥 Finder agent.md>) | ⓘ Any Host (4.3 ⭐): <br/> This host sells shoes.<br/>- They were founded in 1987.<br/>- Joined NLWeb 2 years ago.<br/>User feedback:<br/>- Delivery 4.7⭐ by 357 users<br/>- Support 3.5⭐ by 21 users
|

<br/>


## Flow diagram

![Introduce](<../. 📎 Assets/⚙️ Introduce.png>)


| # | Call | Notes
|-|-|-
| 1 | [🤵🐌🔎 `Introduce@Finder`](<../🔎🅰️ Finder methods/🤵🐌🔎 Introduce.md>) | Ask to introduce a [Host 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>).
| 2 | [🔎🚀⭐ `Reviews@Reviewer`](<../../Reviewers ⭐/🅰️ Reviewer methods/01 🔎🚀⭐ Reviews.md>) | Get domain reviews (may be cached).
| 3 | [👥🚀🕸 `Identity@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>) | Get domain identity (may be cached).
| 4 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | Inform the user.
| 5 | [🔎🐌🤵 `Introduced@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Introduced 🔎🐌🤵/🤵 Introduced 🐌 msg.md>) | Finish introduction.
||