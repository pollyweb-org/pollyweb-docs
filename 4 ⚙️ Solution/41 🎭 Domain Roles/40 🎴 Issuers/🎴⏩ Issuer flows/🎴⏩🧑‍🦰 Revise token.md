# 🎴⏩🧑‍🦰 Revise Token @ Issuer

> An [Issuer 🎴 domain](<../🎴🎭 Issuer role.md>) revises the status of a [Token 🎫](<../../../30 Data/30 🎫 Tokens/🎫 Token.md>). 

<br/>

## 💬 Chat

Consider the following Chat excerpt from the [Pass gates at train station 🤝 use case](<../../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/02 🚂 Customer @ Station/22 Pass gates 1 person.md>), where the railway revokes the ticket upon opening the gate.

| [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 Chats/20 🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../25 Locators/15 🔆 Locators/🔆 Locator.md>)
| 🤵 [Broker](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | ⓘ Ticket shared 
| 🚂 Railway | ✅ Entry gate opened!
| 🤵 [Broker](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) | ⓘ Ticket voided 
|

<br/>

## ⏪ Flow diagram

![alt text](<../.📎 Assets/⚙️ Revise.png>)

| # | Call | Notes
|-|-|-
1| [🎴🐌🤵 `Revise@Broker`](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/50 🤵🅰️ Tokens 🎫/🎴🐌🤵 Revise.md>) | [Issuers 🎴](<../🎴🎭 Issuer role.md>) ask to revise a [Token 🎫](<../../../30 Data/30 🎫 Tokens/🎫 Token.md>)
2| [🤵⏩🧑‍🦰 Update Tokens 🎫](<../../../../5 ⏩ Flows/10 🤵⏩ Brokers/08 🤵⏩🧑‍🦰 Update Tokens 🎫.md>) | [Brokers 🤵](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) tell [Wallets 🧑‍🦰](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) to update the list
3| [🤗⏩🧑‍🦰 Prompt 🤔](<../../30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) tell users about what happened
|