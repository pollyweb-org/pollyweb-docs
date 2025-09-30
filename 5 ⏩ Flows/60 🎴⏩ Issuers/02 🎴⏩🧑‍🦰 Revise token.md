# 🎴⏩🧑‍🦰 Revise Token @ Issuer

> An [Issuer 🎴 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) revises the status of a [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>). 

<br/>

## 💬 Chat

Consider the following Chat excerpt from the [Pass gates at train station 🤝 use case](<../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/02 🚂 Customer @ Station/22 Pass gates 1 person.md>), where the railway revokes the ticket upon opening the gate.

| Service | Prompt | User
| - | - | - |
| | | 🔆 [tap](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>)
| 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Ticket shared 
| 🚂 Railway | ✅ Entry gate opened!
| 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Ticket voided 
|

<br/>

## ⏪ Flow diagram

![alt text](<.📎 Assets/⚙️ Revise.png>)

| # | Call | Notes
|-|-|-
1| [🎴🐌🤵 Revise @ Broker](<../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/52 🎴🐌🤵 Revise.md>) | [Issuers 🎴](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) ask to revise a [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
2| [🤵⏩🎫 Update Tokens](<../10 🤵⏩ Brokers/04 🤵⏩🧑‍🦰 Update tokens.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) tell [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to update the list
3| [🤗⏩🧑‍🦰 Prompt](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) tell users about what happened
|