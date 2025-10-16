# 💼⏩🧑‍🦰 Token Status @ Consumer

* Request from a [💼 Consumer domain](<../💼🎭 Consumer role.md>) 
  * to assess if a [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) is still valid 
  * or if it has been revoked or suspended.


<br/> 


## Flow diagram

![alt text](<../.📎 Assets/⚙️ Token status.png>)

|#| Step | Purpose
|-|-|-
|1| [🧑‍🦰👉🎴 Save Token 🎫](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰⏩ Wallet flows/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) | Users save [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) from [Issuers 🎴](<../../Issuers 🎴/🎴🎭 Issuer role.md>) 
|2| [🧑‍🦰👉💼 Share Token 🎫](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰⏩ Wallet flows/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token 🎫.md>) | Users share [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) with [Consumers 💼](<../💼🎭 Consumer role.md>) 
|3| [🎴🐌🤵 `Revise@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🎴🐌🤵 Revise.md>) | Async update of the status of a [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>)
|4| [💼🚀🤵 `Status@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🚀🤵 Status.md>) | Anonymously, verify [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) statuses
|5| [👥🚀🕸 `Trusts@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts.md>) | Verify if [Consumers 💼](<../💼🎭 Consumer role.md>) are [Trustworthy 👍](<../../../40 👥 Domains/👥👍 Domain Trusts/👍 Domain Trust.md>)
|

<br/>

## FAQ

1. **Why isn't the verification done on the Issuer?**

    `Privacy` [Issuer 🎴 domains](<../../Issuers 🎴/🎴🎭 Issuer role.md>) should not be allowed to track users by knowing in which [Consumer 💼 domains](<../💼🎭 Consumer role.md>) their [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) where used.

    ---
    <br/>