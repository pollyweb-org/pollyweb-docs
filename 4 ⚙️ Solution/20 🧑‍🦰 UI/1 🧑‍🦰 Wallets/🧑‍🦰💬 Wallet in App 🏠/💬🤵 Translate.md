<!-- https://quip.com/u9H6AsA6azmA#temp:C:aXGd01a597ee468481d9af56aa02 -->

# 🧑‍🦰💬🤵 Set language @ Wallet

> Implements a [Wallet 🧑‍🦰 app](<../🧑‍🦰🛠️ Wallet app.md>)

<br/>

## Chat

| [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| 🤵 [Broker](<../../3 🤵 Brokers/🤵🤲 Broker helper.md>) | 😃 Hi! What do you need? <br/> - Change [ language ] <br> - [ Something else ]  | > language
| 🤵 [Broker](<../../3 🤵 Brokers/🤵🤲 Broker helper.md>) | 😃 What should I speak? <br/> - [ 🇵🇹 ] Português <br> - ...  | > 🇵🇹
| 🤵 [Broker](<../../3 🤵 Brokers/🤵🤲 Broker helper.md>) | ✅ Pronto!  
||

<br/>

## Flow diagram

![Translate](<../.📎 Assets/Set-up 📎/⚙️ Translate.png>)


| # | Call | Notes
|-|-|-
| 1 | [🧑‍🦰🐌🤵 `Translate@Broker`](<../../3 🤵 Brokers/🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/🧑‍🦰🐌🤵 Translate.md>) | User changed the language
| 2 | [👥🚀🕸 `Translate@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | Translate from [Manifests 📜](<../../../40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>)
| 3 | [🤵🐌📣 `Translated@Notifier`](<../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/2 🤵🐌📣 Translated.md>) | Finished translating the database
| 4 | [🧑‍🦰🚀🤵 `Chats@Broker`](<../../3 🤵 Brokers/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🚀🤵 Chats.md>) | Fetch translated [Chats 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>)
| 5 | [🧑‍🦰🚀🤵 `Binds@Broker`](<../../3 🤵 Brokers/🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🧑‍🦰🚀🤵 Binds.md>) | Fetch translated [Binds 🔗](<../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>)
| 6 | [🧑‍🦰🚀🤵 `Tokens@Broker`](<../../3 🤵 Brokers/🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🧑‍🦰🚀🤵 Tokens.md>) | Fetch translated [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
|