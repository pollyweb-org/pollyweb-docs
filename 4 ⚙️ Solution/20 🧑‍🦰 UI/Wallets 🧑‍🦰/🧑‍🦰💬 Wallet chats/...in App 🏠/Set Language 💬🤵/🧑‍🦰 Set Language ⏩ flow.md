# 🧑‍🦰💬🤵 Set language @ Wallet

> Implements a [Wallet 🧑‍🦰 app](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)



## Chat

| [Domain](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🤵 [Broker](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 😃 Hi! What do you need? <br/> - Change [ language ] <br> - [ Something else ]  | > language
| 🤵 [Broker](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 😃 What should I speak? <br/> - [ 🇵🇹 ] Português <br> - ...  | > 🇵🇹
| 🤵 [Broker](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | ✅ Pronto!  
||



## Flow diagram

![Translate](<🧑‍🦰 Set Language ⚙️ uml.png>)


| # | Call | Notes
|-|-|-
| 1 | [`Locate@Broker` 🐌 msg](<../../../../Brokers 🤵/🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | User changed the language
| 2 | [👥🚀🕸 `Translate@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>) | Translate from [Manifests 📜](<../../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>)
|3|[🤵🐌📣 `Updated@Notifier`](<../../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>) | Inform the [Wallet 🧑‍🦰 app](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|4|[🧑‍🦰🚀🤵 `Frontend@Broker`](<../../../../Brokers 🤵/🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>) | Update the [Wallet 🧑‍🦰 app](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|