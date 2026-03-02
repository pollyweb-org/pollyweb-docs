# 🎴 `Issuer.Tokens.Issue` ⏩ flow

> About
* Part of the [Issuer 🎴 domain](<../../../🎴 Issuer/🎴🎭 Issuer role.md>) role
* Part of the [`Issuer.Tokens` 🪣 table](<../🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>) 
* Counterpart of the [🤵 `Broker.Tokens.Issue` ⏩ flow](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Tokens 🎫 table/🪣🧱 10 Issue ⏩ flow/🤵 Broker.Tokens.Issue ⏩ flow.md>)

<br/>

## Diagram

![alt text](<🎴 Issuer.Tokens.Issued ⚙️ uml.png>)

Step|Details
|-|-
|[`ISSUE` ⌘ command](<../../../🎴⌘ Issuer cmds/ISSUE 🎫/🎫 ISSUE ⌘ cmd.md>) | [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) intent to issue a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) in a [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
|[`ISSUE` 📃 script](<../../../🎴⌘ Issuer cmds/ISSUE 🎫/🎫 ISSUE 📃 script.md>) | [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements [`ISSUE` ⌘ command](<../../../🎴⌘ Issuer cmds/ISSUE 🎫/🎫 ISSUE ⌘ cmd.md>)
|[`OnTokenIssued` 🔔 handler](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Tokens 🎫 table/🪣🧱 11 Issued 🔔 event/🤵 OnTokenIssued 🔔 handler.md>) | [`Issuer.Tokens` 🪣](<../🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>) event that calls [`SEND` 📬](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
|[`Issue@Broker` 🐌 msg](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [Broker 🤵 ](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) endpoint that receives the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) offer
|[`Issued@Issuer` 📨 msg](<../../../🎴📨 Issuer msgs/Issued 🧑‍🦰🚀🎴/🎴 Issued 📃 handler.md>) | [Issuer 🎴](<../../../🎴 Issuer/🎴🎭 Issuer role.md>) endpoint for [Wallets 🧑‍🦰](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to read the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|[`Issued@Issuer` 📃 handler](<../../../🎴📨 Issuer msgs/Issued 🧑‍🦰🚀🎴/🎴 Issued 📃 handler.md>) | [`Issued@Issuer` 📨 msg](<../../../🎴📨 Issuer msgs/Issued 🧑‍🦰🚀🎴/🎴 Issued 📃 handler.md>) handler
|[`Offered@Issuer` 🐌 msg](<../../../🎴📨 Issuer msgs/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>) | [Issuer 🎴 domain](<../../../🎴 Issuer/🎴🎭 Issuer role.md>) method that receives accept or decline
|[`OnTokenOffered` 🔔 handler](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Tokens 🎫 table/🪣🧱 13 Offered 🔔 event/🤵 OnTokenOffered 🔔 handler.md>) | [`Issuer.Tokens` 🪣](<../🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>) event that returns to [`ISSUE` ⌘](<../../../🎴⌘ Issuer cmds/ISSUE 🎫/🎫 ISSUE ⌘ cmd.md>)
|
