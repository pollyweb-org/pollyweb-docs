<!-- https://quip.com/u9H6AsA6azmA#temp:C:aXGd01a597ee468481d9af56aa02 -->

# 🧑‍🦰💬🤵 Set language @ Wallet

> Implements a [Wallet 🧑‍🦰 app](<../../../🧑‍🦰🛠️ Wallet app.md>)

<br/>

## Chat

| [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) | [User](<../../../🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| 🤵 [Broker](<../../../../Brokers 🤵/🤵🤲 Broker helper.md>) | 😃 Hi! What do you need? <br/> - Change [ language ] <br> - [ Something else ]  | > language
| 🤵 [Broker](<../../../../Brokers 🤵/🤵🤲 Broker helper.md>) | 😃 What should I speak? <br/> - [ 🇵🇹 ] Português <br> - ...  | > 🇵🇹
| 🤵 [Broker](<../../../../Brokers 🤵/🤵🤲 Broker helper.md>) | ✅ Pronto!  
||

<br/>

## Flow diagram

![Translate](<🧑‍🦰 Set Language ⚙️ uml.png>)


| # | Call | Notes
|-|-|-
| 1 | [🧑‍🦰🐌🤵 `Language@Broker`](<../../../../Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Language 🧑‍🦰🐌🤵/🤵 Language 🐌 msg.md>) | User changed the language
| 2 | [👥🚀🕸 `Translate@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | Translate from [Manifests 📜](<../../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>)
| 3 | [🤵🐌📣 `Translated@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Translated 🤵🐌📣/📣 Translated 🐌 msg.md>) | Finished translating the database
| 4 | [🧑‍🦰🚀🤵 `Chats@Broker`](<../../../../Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Chats 🧑‍🦰🚀🤵/🤵 Chats 🚀 request.md>) | Fetch translated [Chats 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
| 5 | [🧑‍🦰🚀🤵 `Binds@Broker`](<../../../../Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Binds 🧑‍🦰🚀🤵/🤵 Binds 🚀 request.md>) | Fetch translated [Binds 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
| 6 | [🧑‍🦰🚀🤵 `Tokens@Broker`](<../../../../Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Tokens 🧑‍🦰🚀🤵/🤵 Tokens 🚀 request.md>) | Fetch translated [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
|