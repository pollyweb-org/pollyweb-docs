# 💼⏩🧑‍🦰 Token Status @ Consumer

> Request from a [💼 Consumer domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) to assess if a [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) is still valid or if it has been revoked or suspended.


<br/> 


## Flow diagram

![alt text](<.📎 Assets/⚙️ Token status.png>)

|#| Step | Purpose
|-|-|-
|1| [🎴⏩🧑‍🦰 Offer @ Issuer](<../90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/01 🎴⏩🧑‍🦰 Save token.md>) | [Issuer 🎴 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) offer [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
|2| [💼⏩🧑‍🦰 Share @ Consumer](<03 💼⏩🧑‍🦰 Share Token.md>) | [Consumer 💼 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) ask for [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
|3| [🎴🐌🤵 Revise @ Broker](<../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/52 🎴🐌🤵 Revise.md>) | Async update of the status of a [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
|4| [💼🚀🤵 Status @ Broker](<../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/62 💼🚀🤵 Status.md>) | Anonymously, verify the status of a [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
|5| [👥🚀🕸 Trusts @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/03 👥🚀🕸 Trusts.md>) | Verify if the Consumer is [Trustworthy 👍](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>)
|

<br/>

## FAQ

1. **Why isn't the verification done on the Issuer?**

    `Privacy` [Issuer 🎴 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) should not be allowed to track users by knowing in which [Consumer 💼 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) their [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) where used.

    ---
    <br/>