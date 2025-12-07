# 🤵 Broker.Wallets.Localize ⏩ flow

> About
* Part of the [`Broker.Wallets` 🪣 table](<../🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)

> Triggers
* [`OnBindLocalized` 🔔 handler](<../../Binds 🔗 table/🪣🧱 51 Localized 🔔 event/🤵 OnBindLocalized 🔔 handler.md>)
* [`OnChatLocalized` 🔔 handler](<../../Chats 💬 table/🪣🧱 21 Localized 🔔 event/🤵 OnChatLocalized 🔔 handler.md>)
* [`OnDomainLocalized` 🔔 handler](<../../Domains 👥 table/🪣🧱 2 Localized 🔔 event/🤵 OnDomainLocalized 🔔 handler.md>)
* [`OnSchemaLocalized` 🔔 handler](<../../Schemas 🧩 table/🪣🧱 Localized 🔔 event/🤵 OnSchemaLocalized 🔔 handler.md>)
* [`OnTokenLocalized` 🔔 handler](<../../Tokens 🎫 table/🪣🧱 21 Localized 🔔 event/🤵 OnTokenLocalized 🔔 handler.md>)
<br/>

## Diagram

![alt text](<🤵 Broker.Wallets.Localize ⚙️ uml.png>)

Step | Purpose |
|-|-
|[`Locate@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| Message from [Wallet 🧑‍🦰 apps](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) for a Pop
|[`PopWalletLocalize` 🔆 handler](<../../../🤵😃 Broker talkers/PopWallet 🧑‍🦰 talker/Wallet » Localize/🤵 PopWalletLocalize 😃 handler.md>)| Sets the language on [`Broker.Wallets`](<../🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
|[`OnWalletLocalized` 🔔 handler](<../🪣🧱 21 Localized 🔔/🤵 OnWalletLocalized 🔔 handler.md>) | Localizes the [`Broker.Wallets` 🪣 table](<../🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
|[`OnFrontendAltered` 🔔 handler](<../../Frontend 📱 table/🪣🧱 Altered 🔔 event/🤵 OnFrontendAltered 🔔 handler.md>)| Calls the [`Updated@Notifier` 🐌 msg](<../../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|[`Frontend@Broker` 📨 msg](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 📃 handler.md>)| Call by a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) app to get the display
|