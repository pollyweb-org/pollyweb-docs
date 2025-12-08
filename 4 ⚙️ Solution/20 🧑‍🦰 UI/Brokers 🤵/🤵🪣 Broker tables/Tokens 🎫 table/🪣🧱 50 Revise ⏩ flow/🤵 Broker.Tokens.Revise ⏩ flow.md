# 🤵 Broker.Tokens.Revise ⏩ flow

> Part of the [`Broker.Tokens` 🪣 table](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 Broker.Tokens.Revise ⚙️ uml.png>)

Step | Purpose |
|-|-
|[`Revise@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>)| Message for [Issuer 🎴 domains](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) to change a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|[`Revise@Broker` 📃 handler](<../../../🤵📨 Broker msgs/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 📃 handler.md>)| [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that saves the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) status
|[`OnTokenRevised` 🔔 handler](<../🪣🧱 51 Revised 🔔 event/🤵 OnTokenRevised 🔔 handler.md>)| [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that registers a Pop
| `TODO` | [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that notifies the user
|[`OnFrontendAltered` 🔔 handler](<../../Frontend 📱 table/🪣🔔 Altered/🤵 OnFrontendAltered 🔔 handler.md>)| [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that refreshes the Frontend display
|[`Frontend@Broker` 📨 msg](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 📃 handler.md>)| Call by a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) app to get the display
|