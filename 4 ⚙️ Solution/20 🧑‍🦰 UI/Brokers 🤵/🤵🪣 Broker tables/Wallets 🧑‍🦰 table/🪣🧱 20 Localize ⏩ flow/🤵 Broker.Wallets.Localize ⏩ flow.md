# 🤵 Broker.Tokens.Localize ⏩ flow

> Part of the [`Broker.Tokens` 🪣 table](<../../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 Broker.Wallets.Localize ⚙️ uml.png>)

Step | Purpose |
|-|-
|[`Pop@Broker` 🅰️ method](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>)| Message from [Wallet 🧑‍🦰 apps](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to for a Pop
| [`Pop@Broker` 📃 handler](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 📃 handler.md>) | Inserts into the [`Broker.Pops` 🪣 table](<../../Pops 🎈 table/🪣 Pops/🤵 Broker.Pops 🪣 table.md>)
|[`OnPopLocalize` 🔔 handler](<../../Pops 🎈 table/🪣🧱 22 Wallet » Localize 🔔/🤵 OnPopLocalize 🔔 handler.md>)| Sets the language on [`Broker.Wallets`](<../🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
|[`OnWalletLocalized` 🔔 handler](<../🪣🧱 21 Localized 🔔/🤵 OnWalletLocalized 🔔 handler.md>) | Localizes the [`Broker.Wallets` 🪣 table](<../🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)
|[`OnFrontendAltered` 🔔 handler](<../../Frontend 📱 table/🪣🧱 Altered 🔔 event/🤵 OnFrontendAltered 🔔 handler.md>)| Calls the [`Updated@Notifier` 🅰️ method](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|[`Frontend@Broker` 🅰️ method](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 📃 handler.md>)| Call by a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) app to get the display
|