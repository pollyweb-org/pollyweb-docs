# 💼⏩🧑‍🦰 Share a Token @ Consumer

> Request from a [💼 Consumer domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) to access the user's [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>).

> Mentioned in [🆔 Verify Tokens @ Identity](<../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/14 🆔🎫 Verify Tokens.md>)

<br/> 


## Flow diagram

![alt text](<.📎 Assets/⚙️ Query Token.png>)

|#| Step | Purpose
|-|-|-
|1| [💼🐌🤵 Query @ Broker](<../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>) | Ask for user data in specific [Schema Codes 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
|2| [👥🚀🕸 Queryable @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/05 👥🚀🕸 Queryable.md>) | Match user [Bind 🔗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) with usable [Trust 👍](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>) paths
|3| [👥🚀🕸 Translate @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/06 👥🚀🕸 Translate.md>) | Translate the [Schema Codes 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
|4| [🤵🐌📣 Share @ Notifier](<../../6 🅰️ APIs/65 📣🅰️ Notifier/02 📣💬🅰️ Chats/22 🤵🐌📣 Share.md>) | Show the request to the user
|5| [🤵🐌💼 Shared @ Consumer](<../../6 🅰️ APIs/30 💼🅰️ Consumer/02 🧑‍🦰🐌💼 Shared.md>) | Send the shared offline [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
|6| [👥🚀🕸 Trusts @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/03 👥🚀🕸 Trusts.md>) | Verify if the [Issuers 🎴](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) are [Trustworthy 👍](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>)
|7| [👥🚀🕸 Public Key @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/07 👥🚀🕸 Public Key.md>) | Get the DKIM public key of each [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
|

<br/>

## FAQ

1. **Why isn't the verification done on the Issuer?**

    `Privacy` [Issuer 🎴 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) should not be allowed to track users by knowing in which [Consumer 💼 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) their [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) where used.

    ---
    <br/>