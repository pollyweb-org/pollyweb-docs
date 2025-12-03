# 🤵 `Broker.Tokens.Issue` ⏩ flow

> About
* Part of the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) role
* Part of the [`Broker.Tokens` 🪣 table](<../🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
* Counterpart of the [🎴 `Issuer.Tokens.Issue` ⏩ flow](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🪣 Issuer tables/Tokens 🎫 table/🪣⏩ Issued flow/🎴 Issuer.Tokens.Issued ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🤵 Broker.Tokens.Issue ⚙️ uml.png>)

Step | Purpose |
|-|-
|[`Issue@Broker` 📨 msg](<../../../🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | External message from an [Issuer 🎴 domain](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>)
|[`Issue@Broker` 📃 handler](<../../../🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 📃 handler.md>) | [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that stores the issued [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|[`OnTokenIssued` 🔔 handler](<../🪣🧱 11 Issued 🔔 event/🤵 OnTokenIssued 🔔 handler.md>) | [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that localizes the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|[`OnTokenDetailed` 🔔 handler](<../🪣🧱 12 Detailed 🔔 event/🤵 OnTokenDetailed 🔔 handler.md>) | [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that asks for user confirmation
|[`OnTokenOffered` 🔔 handler](<../🪣🧱 13 Offered 🔔 event/🤵 OnTokenOffered 🔔 handler.md>) | [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that processes user response
|[`OnTokenSaved` 🔔 handler](<../🪣🧱 15 Saved 🔔 event/🤵 OnTokenSaved 🔔 handler.md>) | [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that finalizes the Token storage
|[`OnTokenAltered` 🔔 handler](<../🪣🧱 00 Altered 🔔 event/🤵 OnTokenAltered 🔔 handler.md>) | [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that gets the Tokens to display
|[`OnFrontendAltered` 🔔 handler](<../../Frontend 📱 table/🪣🧱 Altered 🔔 event/🤵 OnFrontendAltered 🔔 handler.md>) | [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that refreshes the Frontend display
|[`Frontend@Broker` 📨 msg](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>) | Call by a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to get the display
|