# 🤵 Broker.Tokens.Tag ⏩ flow

> Part of the [`Broker.Tokens` 🪣 table](<../../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 Broker.Tokens.Tag ⚙️ uml.png>)

Step | Purpose |
|-|-
|[`Pop@Broker` 🅰️ method](<../../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>)| Message from [Wallet 🧑‍🦰 apps](<../../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to add a tag to a [Token 🎫](<../../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|[`OnPopToken` 📃 handler](<../../../Pops 🎈 table/🪣🔔 61 Token/🤵 OnPopToken 🔔 handler.md>)
|[`OnPopTagToken` 📃 handler](<../../../Pops 🎈 table/🪣🔔 63 Token » Tag/🤵 OnPopTagToken 🔔 handler.md>)| [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that saves the tag to the [Token 🎫](<../../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|[`OnTokenAltered` 📃 handler](<../../🪣🧱 0 Altered 🔔 event/🤵 OnTokenAltered 🔔 handler.md>)| [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that updates the Frontend table
|[`OnFrontendAltered` 📃 handler](<../../../Frontend 📱 table/🪣🔔 on Altered/🤵 OnFrontendAltered 🔔 handler.md>)| [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that refreshes the Frontend display
|[`Frontend@Broker` 🅰️ method](<../../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 📃 handler.md>)| Call by a [Wallet 🧑‍🦰 app](<../../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) app to get the display