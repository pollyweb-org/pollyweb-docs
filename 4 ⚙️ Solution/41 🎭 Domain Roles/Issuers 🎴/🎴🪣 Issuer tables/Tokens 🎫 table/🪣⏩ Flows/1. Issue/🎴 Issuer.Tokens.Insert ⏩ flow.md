# 🎴 Issuer.Tokens.Insert ⏩ flow

> Part of the [`Issuer.Tokens` 🪣 table](<../../🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>)

<br/>

## Diagram

![alt text](<🎴 Issuer.Tokens.Insert ⚙️ uml.png>)

Step|Details
|-|-
|[`ISSUE` ⌘ command](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/ISSUE 🎫/🎫 ISSUE ⌘ cmd.md>) | [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) intent to issue a [Token 🎫](<../../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) in a [Chat 💬](<../../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
|[`ISSUE` 📃 script](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/ISSUE 🎫/🎫 ISSUE 📃 script.md>) | [Script 📃](<../../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements [`ISSUE` ⌘ command](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/ISSUE 🎫/🎫 ISSUE ⌘ cmd.md>)
|[`OnTokenIssued` 🔔 handler](<../../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Tokens 🎫 table/🪣🔔 1 Issued/🤵 OnTokenIssued 🔔 handler.md>) | [`Issuer.Tokens` 🪣](<../../🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>) event that calls [`SEND` 📬](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
|[`Issue@Broker` 🅰️ method](<../../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [Broker 🤵 ](<../../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) endpoint that receives the [Token 🎫](<../../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) offer
|[`Issued@Issuer` 🅰️ method](<../../../../🎴🅰️ Issuer methods/Issued 🧑‍🦰🚀🎴/🎴 Issued 📃 handler.md>) | [Issuer 🎴](<../../../../🎴 Issuer/🎴🎭 Issuer role.md>) endpoint for [Wallets 🧑‍🦰](<../../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to read the [Token 🎫](<../../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|[`Issued@Issuer` 📃 handler](<../../../../🎴🅰️ Issuer methods/Issued 🧑‍🦰🚀🎴/🎴 Issued 📃 handler.md>) | [`Issued@Issuer` 🅰️ method](<../../../../🎴🅰️ Issuer methods/Issued 🧑‍🦰🚀🎴/🎴 Issued 📃 handler.md>) handler
|[`Offered@Issuer` 🅰️ method](<../../../../🎴🅰️ Issuer methods/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>) | [Issuer 🎴 domain](<../../../../🎴 Issuer/🎴🎭 Issuer role.md>) method that receives accept or decline
|[`OnTokenOffered` 🔔 handler](<../../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Tokens 🎫 table/🪣🔔 3 Offered/🤵 OnTokenOffered 🔔 handler.md>) | [`Issuer.Tokens` 🪣](<../../🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>) event that returns to [`ISSUE` ⌘](<../../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/ISSUE 🎫/🎫 ISSUE ⌘ cmd.md>)
|
