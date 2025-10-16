<!-- https://quip.com/u9H6AsA6azmA#temp:C:aXGd01a597ee468481d9af56aa02 -->

# 🧑‍🦰👉🤵 Set language @ Wallet

> Implements a [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)

<br/>

## Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | 😃 Hi! What do you need? <br/> - Change [ language ] <br> - [ Something else ]  | > language
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | 😃 What should I speak? <br/> - [ 🇵🇹 ] Português <br> - ...  | > 🇵🇹
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | ✅ Pronto!  
||

<br/>

## Flow diagram

![Translate](<.📎 Assets/⚙️ Translate.png>)


| # | Call | Notes
|-|-|-
| 1 | [🧑‍🦰🐌🤵 `Translate@Broker`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/10 🤵🅰️ Wallets 🧑‍🦰/🧑‍🦰🐌🤵 Translate.md>) | User changed the language
| 2 | [👥🚀🕸 `Translate@Graph`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | Translate from [Manifests 📜](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/📜 Manifest.md>)
| 3 | [🤵🐌📣 `Translated@Notifier`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/1 🤵 Onboard/2 🤵🐌📣 Translated.md>) | Finished translating the database
| 4 | [🧑‍🦰🚀🤵 `Chats@Broker`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/30 🤵🅰️ Chats 💬/🧑‍🦰🚀🤵 Chats.md>) | Fetch translated [Chats 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)
| 5 | [🧑‍🦰🚀🤵 `Binds@Broker`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/40 🤵🅰️ Binds 🔗/🧑‍🦰🚀🤵 Binds.md>) | Fetch translated [Binds 🔗](<../../../4 ⚙️ Solution/30 🧩 Data/20 🔗 Binds/🔗 Bind.md>)
| 6 | [🧑‍🦰🚀🤵 `Tokens@Broker`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/50 🤵🅰️ Tokens 🎫/🧑‍🦰🚀🤵 Tokens.md>) | Fetch translated [Tokens 🎫](<../../../4 ⚙️ Solution/30 🧩 Data/30 🎫 Tokens/🎫 Token.md>)
|