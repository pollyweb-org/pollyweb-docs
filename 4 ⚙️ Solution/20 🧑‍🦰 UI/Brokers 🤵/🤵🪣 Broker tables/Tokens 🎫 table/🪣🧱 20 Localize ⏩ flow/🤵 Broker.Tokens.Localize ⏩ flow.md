# 🤵 Broker.Tokens.Localize ⏩ flow

> About
* Part of the [`Broker.Tokens` 🪣 table](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
* Part of the [🤵 `Broker.Wallets.Localize` ⏩ flow](<../../Wallets 🧑‍🦰 table/🪣🧱 20 Localize ⏩ flow/🤵 Broker.Wallets.Localize ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 Broker.Tokens.Localize ⚙️ uml.png>)

Step | Purpose |
|-|-
|[`Pop@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>)| Message from [Wallet 🧑‍🦰 apps](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to for a Pop
|[`OnPopLocalize` 🔔 handler](<../../Pops 🎈 table/🪣🧱 22 Wallet » Localize 🔔/🤵 OnPopLocalize 🔔 handler.md>)| Localizes the [`Broker.Wallets` 🪣 table](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
|[`OnWalletLocalized` 🔔 handler](<../../Wallets 🧑‍🦰 table/🪣🧱 21 Localized 🔔/🤵 OnWalletLocalized 🔔 handler.md>) | Localizes all the Wallet's [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|[`OnTokenLocalized` 📃 handler](<../🪣🧱 21 Localized 🔔 event/🤵 OnTokenLocalized 🔔 handler.md>) | Localizes a single item in [`Broker.Tokens`](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
|[`OnTokenAltered` 📃 handler](<../🪣🧱 00 Altered 🔔 event/🤵 OnTokenAltered 🔔 handler.md>)| [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that updates the Frontend table
|[`OnFrontendAltered` 📃 handler](<../../Frontend 📱 table/🪣🧱 Altered 🔔 event/🤵 OnFrontendAltered 🔔 handler.md>)| [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that refreshes the Frontend display
|[`Frontend@Broker` 📨 msg](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 📃 handler.md>)| Call by a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) app to get the display