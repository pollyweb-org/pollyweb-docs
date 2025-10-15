# 👉 Introduce Host @ Finder 

> Ask the [Finder 🔎 domain](<$ 🔎🫥 Finder agent.md>) to introduce the [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>)

> Used by:
> <br/>• [🧑‍🦰👉🤗 Scan host QR](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/01 🧑‍🦰👉🤗 Scan host QR.md>)
> <br/>• [🧑‍🦰👉🤗 Scan printer QR](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/02 🧑‍🦰👉🤗 Scan printer QR.md>)

<br/>

## 💬 Chat

| [Domain](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>)
| 🔎 [Finder](<$ 🔎🫥 Finder agent.md>) | ⓘ Any Host (4.3 ⭐): <br/> This host sells shoes.<br/>- They were founded in 1987.<br/>- Joined NLWeb 2 years ago.<br/>User feedback:<br/>- Delivery 4.7⭐ by 357 users<br/>- Support 3.5⭐ by 21 users
|

<br/>


## Flow diagram

![Introduce](<. 📎 Assets/⚙️ Introduce.png>)


| # | Call | Notes
|-|-|-
| 1 | [🤵🐌🔎 `Introduce@Finder`](<51 🤵🐌🔎 Introduce@Finder.md>) | Ask to introduce a [Host 🤗](<../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>).
| 2 | [🔎🚀⭐ `Reviews@Reviewer`](<../../../6 🅰️ APIs/80 ⭐🅰️ Reviewer/01 🔎🚀⭐ Reviews.md>) | Get domain reviews (may be cached).
| 3 | [👥🚀🕸 `Identity@Graph`](<../../45 🛠️ Helper domains/50 🕸 Graphs/45 🕸🅰️ Graph methods/04 👥🚀🕸 Identity.md>) | Get domain identity (may be cached).
| 4 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../41 🎭 Domain Roles/30 🤗 Hosts/31 🤗⏩🧑‍🦰 Prompt 🤔 flow.md>) | Inform the user.
| 5 | [🔎🐌🤵 `Introduced@Broker`](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/04 🔎🐌🤵 Introduced.md>) | Finish introduction.
||