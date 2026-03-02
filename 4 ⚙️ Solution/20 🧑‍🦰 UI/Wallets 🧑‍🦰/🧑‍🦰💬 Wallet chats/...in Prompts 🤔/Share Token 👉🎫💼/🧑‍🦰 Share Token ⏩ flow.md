# 💼⏩🧑‍🦰 Share a Token @ Consumer

> About
* Request from a [💼 Consumer domain](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) to access the user's [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>).
* Mentioned in [🆔 Verify Tokens @ Identifier](<../../../../../50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/3 Verify Tokens 🆔⏩🎫/🆔⏩ Verify Tokens.md>)

<br/> 

## 💬 Chat 

Consider the following excerpt from the [Flight check in 🤝 use case](<../../../../../../3 🤝 Use Cases/03 🧳 Travel/09 🧳 Travel by air 💺/14 💺 Ticket/05 Flight check in.md>) as an example.

| [Domain](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🛩️ Airline     | ℹ️ I need Alice's passport.
| 🤵 [Broker](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 Share passport?  [No] <br/> - [ 🇬🇧 UK Alice ]<br/>- [ 🇬🇧 UK Teresa ]<br/>- [ 🇺🇸 US Teresa ] | > 🇬🇧 UK Alice 
| 🛩️ Airline     | ✅ Thanks!
|

<br/> 

## Flow diagram

![alt text](<🧑‍🦰 Share Token ⚙️ uml.png>)

|#| Step | Purpose
|-|-|-
|1| [💼🐌🤵 `Query@Broker`](<../../../../Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | Ask for user data in specific [Schema Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|2| [👥🚀🕸 `Queryable@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Queryable/🕸 Queryable 🚀 call.md>) | Match user [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) with usable [Trust 🫡](<../../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) paths
|3| [👥🚀🕸 `Translate@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>) | Translate the [Schema Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|4| [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Brokers 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) ask users to share their [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|5| [🤵🐌📣 `Share@Notifier`](<../../../../Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>) | Proxy the share order to the [Wallet 🧑‍🦰 app](<../../../🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|6| [🤵🐌💼 `Receive@Consumer`](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼📨 Consumer msgs/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>) | Send the shared offline [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|7| [👥🚀🕸 `Trusts@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>) | Verify if the [Issuers 🎴](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) are [Trustworthy 🫡](<../../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>)
|8| [👥🚀🕸 `PublicKey@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Public Key/🕸 Public Key 🚀 call.md>) | Get the DKIM public key of each [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|9| [💼⏩🤵 Token status 🎫](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Token Status 💼⏩🎫/💼 Token Status ⏩ flow.md>) | Ask the Token's [Broker 🤵](<../../../../Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) if it is still active
|

<br/>

## FAQ

1. **Why isn't the verification done on the Issuer?**

    `Privacy` [Issuer 🎴 domains](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) should not be allowed to track users by knowing in which [Consumer 💼 domains](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) their [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) where used.

    ---
    <br/>