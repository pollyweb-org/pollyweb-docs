# 🤵 `Broker.Tokens.Tag` ⏩ flow

> About
* Part of the [`Broker.Tokens` 🪣 table](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
* Allows users to add a custom title to a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)

<br/>

## Diagram

![alt text](<🤵 Broker.Tokens.Tag ⚙️ uml.png>)

Step | Purpose |
|-|-
| [`Locate@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | Message from [Wallet 🧑‍🦰 apps](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to add a tag to a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|[`PopTagToken` 🔆 handler](<../../../🤵😃 Broker talkers/PopToken 🎫 talker/Token » Tag/🤵 PopTokenTag 😃 handler.md>)| [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that saves the tag to the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|[`OnTokenAltered` 🔔 handler](<../🪣🧱 00 Altered 🔔 event/🤵 OnTokenAltered 🔔 handler.md>)| [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that updates the [`Broker.Frontend` 🪣 table](<../../Frontend 📱 table/🪣 Frontend/🤵 Broker.Frontend 🪣 table.md>)
|[`OnFrontendAltered` 🔔 handler](<../../Frontend 📱 table/🪣🧱 Altered 🔔 event/🤵 OnFrontendAltered 🔔 handler.md>)| [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that calls [`Updated@Notifier` 📨](<../../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|[`Frontend@Broker` 📨 msg](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 📃 handler.md>)| Call by a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) app to get the display
|