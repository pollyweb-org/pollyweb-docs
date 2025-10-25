# 💼⏩🧑‍🦰 Share a Token @ Consumer

> Request from a [💼 Consumer domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) to access the user's [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>).

> Mentioned in [🆔 Verify Tokens @ Identity](<../../../../50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/3 🆔⏩🎫 Verify Tokens.md>)

<br/> 

## 💬 Chat 

Consider the following excerpt from the [Flight check in 🤝 use case](<../../../../../3 🤝 Use Cases/03 🧳 Travel/09 🧳 Travel by air 💺/14 💺 Ticket/05 Flight check in.md>) as an example.

| Service       | Prompt | User
| - | - | - |
| 🛩️ Airline     | ℹ️ I need the passports.
| 🤵 [Broker](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 Share passports?  [All, No] <br/> - [ ] 🇬🇧 UK Alice <br/>- [ ] 🇬🇧 UK Teresa <br/>- [ ] 🇺🇸 US Teresa  | [X] 🇬🇧 UK Alice <br/> [X] 🇺🇸 US Teresa
| 🛩️ Airline     | ✅ Thanks!
|

<br/> 

## Flow diagram

![alt text](<../../.📎 Assets/Tokens 📎/⚙️🎫 Share Token.png>)

|#| Step | Purpose
|-|-|-
|1| [💼🐌🤵 `Query@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | Ask for user data in specific [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|2| [👥🚀🕸 `Queryable@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Queryable.md>) | Match user [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) with usable [Trust 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) paths
|3| [👥🚀🕸 `Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | Translate the [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|4| [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) ask users to share their [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
|5| [🤵🐌📣 `Share@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>) | Proxy the share order to the [Wallet 🧑‍🦰 app](<../../🧑‍🦰🛠️ Wallet app.md>)
|6| [🤵🐌💼 `Receive@Consumer`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>) | Send the shared offline [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
|7| [👥🚀🕸 `Trusts@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts.md>) | Verify if the [Issuers 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) are [Trustworthy 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>)
|8| [👥🚀🕸 `PublicKey@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Public Key.md>) | Get the DKIM public key of each [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
|9| [💼⏩🤵 Token status 🎫](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Token Status 💼⏩🎫/💼 Token Status ⏩ flow.md>) | Ask the Token's [Broker 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) if it is still active
|

<br/>

## FAQ

1. **Why isn't the verification done on the Issuer?**

    `Privacy` [Issuer 🎴 domains](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) should not be allowed to track users by knowing in which [Consumer 💼 domains](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) their [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) where used.

    ---
    <br/>