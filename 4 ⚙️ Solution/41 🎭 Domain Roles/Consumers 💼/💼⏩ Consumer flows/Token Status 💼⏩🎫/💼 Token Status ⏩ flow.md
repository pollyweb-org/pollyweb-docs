# 💼⏩🧑‍🦰 Token Status @ Consumer

* Request from a [💼 Consumer domain](<../../💼🎭 Consumer role.md>) 
  * to assess if a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) is still valid 
  * or if it has been revoked or suspended.


<br/> 


## Flow diagram

![alt text](<💼 Token Status ⚙️ uml.png>)

|#| Step | Purpose
|-|-|-
|1| [🧑‍🦰👉🎴 Save Token 🎫](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉🎴 Save token/👉🎴 Save token.md>) | Users save [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) from [Issuers 🎴](<../../../Issuers 🎴/🎴🎭 Issuer role.md>) 
|2| [🧑‍🦰👉💼 Share Token 🎫](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉💼 Share Token 🎫/🎫 Share Token ⏩ flow.md>) | Users share [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) with [Consumers 💼](<../../💼🎭 Consumer role.md>) 
|3| [🎴🐌🤵 `Revise@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>) | Async update of the status of a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
|4| [💼🚀🤵 `Status@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Status 💼🚀🤵/🤵 Status 🚀 request.md>) | Anonymously, verify [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) statuses
|5| [👥🚀🕸 `Trusts@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts.md>) | Verify if [Consumers 💼](<../../💼🎭 Consumer role.md>) are [Trustworthy 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>)
|

<br/>

## FAQ

1. **Why isn't the verification done on the Issuer?**

    `Privacy` [Issuer 🎴 domains](<../../../Issuers 🎴/🎴🎭 Issuer role.md>) should not be allowed to track users by knowing in which [Consumer 💼 domains](<../../💼🎭 Consumer role.md>) their [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) where used.

    ---
    <br/>