# 🎴⏩🧑‍🦰 Revise Token @ Issuer

> An [Issuer 🎴 domain](<../../🎴 Issuer/🎴🎭 Issuer role.md>) revises the status of a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>). 

<br/>

## 💬 Chat

Consider the following Chat excerpt from the [Pass gates at train station 🤝 use case](<../../../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/02 🚂 Customer @ Station/22 Pass gates 1 person.md>), where the railway revokes the ticket upon opening the gate.

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
| 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | ⓘ Ticket shared 
| 🚂 Railway | ✅ Entry gate opened!
| 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | ⓘ Ticket voided 
|

<br/>

## ⏪ Flow diagram

![alt text](<🎴 Revise Token ⚙️ uml.png>)

| # | Call | Notes
|-|-|-
1| [🎴🐌🤵 `Revise@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>) | [Issuers 🎴](<../../🎴 Issuer/🎴🎭 Issuer role.md>) ask to revise a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
2| [🤗⏩🧑‍🦰 Prompt 🤔](<../../../Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) tell users about what happened
|