# 🤵 Broker.Tokens.Insert ⏩ flow

## Diagram

![alt text](<🤵 Broker.Tokens.Insert ⚙️ uml.png>)

Step | Purpose |
|-|-
|[`Issue@Broker` 🅰️ method](<../../../../🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | External message from an [Issuer 🎴 domain](<../../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>)
|[`Issue@Broker` 📃 handler](<../../../../🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 📃 handler.md>) | [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that stores the issued [Token 🎫](<../../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|[`OnTokenIssued` 🔔 handler](<../../🪣🔔 1 Issued/🤵 OnTokenIssued 📃 handler.md>) | [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that localizes the [Token 🎫](<../../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|[`OnTokenDetailed` 🔔 handler](<../../🪣🔔 2 Detailed/🤵 OnTokenDetailed 📃 handler.md>) | [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that asks for user confirmation
|[`OnTokenOffered` 🔔 handler](<../../🪣🔔 3 Offered/🤵 OnTokenOffered 📃 handler.md>) | [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that processes user response
|[`OnTokenSaved` 🔔 handler](<../../🪣🔔 5 Saved/🤵 OnTokenSaved 📃 handler.md>) | [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that finalizes the Token storage
|[`OnTokenAltered` 🔔 handler](<../../🪣🔔 0 Altered/🤵 OnTokenAltered 📃 handler.md>) | [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that gets the Tokens to display
|[`OnFrontendAltered` 🔔 handler](<../../../Frontend 📱 table/🪣🔔 on Altered/🤵 OnFrontendAltered 🔔 handler.md>) | [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that refreshes the Frontend display
|[`Frontend@Broker` 🅰️ method](<../../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>) | Call by a [Wallet 🧑‍🦰 app](<../../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to get the display
|