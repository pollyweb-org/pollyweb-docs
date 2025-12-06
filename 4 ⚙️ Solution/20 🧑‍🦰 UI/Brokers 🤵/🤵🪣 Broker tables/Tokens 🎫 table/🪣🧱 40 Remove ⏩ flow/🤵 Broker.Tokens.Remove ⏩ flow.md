# 🤵 Broker.Tokens.Remove ⏩ flow

> Part of the [`Broker.Tokens` 🪣 table](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 Broker.Tokens.Remove ⚙️ uml.png>)

Step | Purpose |
|-|-
|[`Pop@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>) | [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) endpoint to pop-up a [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
|[`Pop@Broker` 📃 handler](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 📃 handler.md>)
|[`OnPopToken` 🔔 handler](<../../../🤵🔆 Broker locators/PopToken 🔆/🪣🧱 61 Token 🔔/🤵 OnPopToken 🔔 handler.md>) | 
|[`OnPopRemoveToken` 🔔 handler](<../../../🤵🔆 Broker locators/PopToken 🔆/🪣🧱 62 Token » Remove 🔔/🤵 OnPopRemoveToken 🔔 handler.md>)| 
|[`OnTokenRemoved` 🔔 handler](<../🪣🧱 41 Removed 🔔 event/🤵 OnTokenRemoved 🔔 handler.md>)
|[`Removed@Issuer` 🐌 msg](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴📨 Issuer msgs/Removed 🤵🐌🎴/🎴 Removed 🐌 msg.md>)
|[`Remove@Notifier` 🐌 msg](<../../../../Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Remove 🤵🐌📣/📣 Remove 🐌 msg.md>)
|[`OnFrontendAltered` 🔔 handler](<../../Frontend 📱 table/🪣🧱 Altered 🔔 event/🤵 OnFrontendAltered 🔔 handler.md>)| Calls the [`Update@Notifier` 🐌 msg](<../../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|[`Frontend@Broker` 📨 msg](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 📃 handler.md>)| Call by a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) app to get the display
|