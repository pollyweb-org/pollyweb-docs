# 🤵 Broker.Tokens.Remove ⏩ flow

> Part of the [`Broker.Tokens` 🪣 table](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 Broker.Tokens.Remove ⚙️ uml.png>)

Step | Purpose |
|-|-
|[`OnPopToken` 🔔 handler](<../../../🤵😃 Broker talkers/PopToken 🔆/Token/🤵 PopToken 🔆 handler.md>) | 
|[`OnPopRemoveToken` 🔔 handler](<../../../🤵😃 Broker talkers/PopToken 🔆/Token » Remove/🤵 PopTokenRemove 🔆 handler.md>)| 
|[`OnTokenRemoved` 🔔 handler](<../🪣🧱 41 Removed 🔔 event/🤵 OnTokenRemoved 🔔 handler.md>)
|[`Removed@Issuer` 🐌 msg](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴📨 Issuer msgs/Removed 🤵🐌🎴/🎴 Removed 🐌 msg.md>)
|[`Remove@Notifier` 🐌 msg](<../../../../Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Remove 🤵🐌📣/📣 Remove 🐌 msg.md>)
|[`OnFrontendAltered` 🔔 handler](<../../Frontend 📱 table/🪣🧱 Altered 🔔 event/🤵 OnFrontendAltered 🔔 handler.md>)| Calls the [`Update@Notifier` 🐌 msg](<../../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|[`Frontend@Broker` 📨 msg](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 📃 handler.md>)| Call by a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) app to get the display
|