# 👉 Introduce Host @ Finder 

> Ask the [Finder 🔎 domain](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) to introduce the [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>)

> Used by:
> <br/>• [🧑‍🦰👉🤗 Scan host QR](<../90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/01 🧑‍🦰👉🤗 Scan host QR.md>)
> <br/>• [🧑‍🦰👉🤗 Scan printer QR](<../90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/02 🧑‍🦰👉🤗 Scan printer QR.md>)

<br/>

## 💬 Chat

| [Domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Msgs/00 👥 Domain.md>) | [Prompt](<../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>)
| 🔎 [Finder](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Host (4.3 ⭐): <br/> This host sells shoes.<br/>- They were founded in 1987.<br/>- Joined NLWeb 2 years ago.<br/>User feedback:<br/>- Delivery 4.7⭐ by 357 users<br/>- Support 3.5⭐ by 21 users
|

<br/>


## Flow diagram

![Introduce](<.📎 Assets/⚙️ Introduce.png>)


| # | Call | Notes
|-|-|-
| 1 | [🤵🐌🔎 `Introduce@Finder`](<../../6 🅰️ APIs/40 🔎🅰️ Finder/01 🤵🐌🔎 Introduce.md>) | Ask to introduce a [Host 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>).
| 2 | [🔎🚀⭐ `Reviews@Reviewer`](<../../6 🅰️ APIs/80 ⭐🅰️ Reviewer/01 🔎🚀⭐ Reviews.md>) | Get domain reviews (may be cached).
| 3 | [👥🚀🕸 `Identity@Graph`](<../../6 🅰️ APIs/45 🕸🅰️ Graph/04 👥🚀🕸 Identity.md>) | Get domain identity (may be cached).
| 4 | [🤗⏩🧑‍🦰 Prompt 🤔](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | Inform the user.
| 5 | [🔎🐌🤵 `Introduced@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/04 🔎🐌🤵 Introduced.md>) | Finish introduction.
||