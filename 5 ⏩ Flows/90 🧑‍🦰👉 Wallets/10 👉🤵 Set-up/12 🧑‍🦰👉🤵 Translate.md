<!-- https://quip.com/u9H6AsA6azmA#temp:C:aXGd01a597ee468481d9af56aa02 -->

# 🧑‍🦰👉🤵 Set language @ Wallet



## Chat

| Service | Prompt | User
| - | - | - |
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 😃 Hi! What do you need? <br/> - Change [ language ] <br> - [ Something else ]  | > language
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 😃 What should I speak? <br/> - [ 🇵🇹 ] Português <br> - ...  | > 🇵🇹
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | ✅ Pronto!  
||

<br/>

## Flow diagram

![Translate](<.📎 Assets/⚙️ Translate.png>)


| # | Call | Notes
|-|-|-
| 1 | [🧑‍🦰🐌🤵 Translate @ Broker](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/10 🤵🅰️ Wallets 🧑‍🦰/12 🧑‍🦰🐌🤵 Translate.md>) | User changed the language.
| 2 | [🚀🕸 Translate @ Graph](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/06 👥🚀🕸 Translate.md>) | Translate from [Manifests 📜](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>). 
| 3 | [🤵🐌📣 Translated @ Notifier](<../../../6 🅰️ APIs/65 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/21 🤵🐌📣 Translated.md>) | Finished translating the database.
| 4 | [🧑‍🦰🚀🤵 Chats @ Broker](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/02 🧑‍🦰🚀🤵 Chats.md>) | Fetch translated [Chats 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>).
| 5 | [🧑‍🦰🚀🤵 Binds @ Broker](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/41 🧑‍🦰🚀🤵 Binds.md>) | Fetch translated [Binds 🔗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>)
| 6 | [🧑‍🦰🚀🤵 Tokens @ Broker](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/54 🧑‍🦰🚀🤵 Tokens.md>) | Fetch translated [Tokens 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
|