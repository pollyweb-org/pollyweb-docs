# 💼⏩🧑‍🦰 Share a Token @ Consumer

> Request from a [💼 Consumer domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) to access the user's [Tokens 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/$ 🎫 Token.md>).

> Mentioned in [🆔 Verify Tokens @ Identity](<../../../4 ⚙️ Solution/30 🫥 Agents/45 🆔 Identities/14 🆔🎫 Verify Tokens.md>)

<br/> 

## 💬 Chat 

Consider the following excerpt from the [Flight check in 🤝 use case](<../../../3 🤝 Use Cases/03 🧳 Travel/09 🧳 Travel by air 💺/14 💺 Ticket/05 Flight check in.md>) as an example.

| Service       | Prompt | User
| - | - | - |
| 🛩️ Airline     | ℹ️ I need the passports.
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) | 🫥 Share passports?  [All, No] <br/> - [ ] 🇬🇧 UK Alice <br/>- [ ] 🇬🇧 UK Teresa <br/>- [ ] 🇺🇸 US Teresa  | [X] 🇬🇧 UK Alice <br/> [X] 🇺🇸 US Teresa
| 🛩️ Airline     | ✅ Thanks!
|

<br/> 

## Flow diagram

![alt text](<.📎 Assets/⚙️ Share Token.png>)

|#| Step | Purpose
|-|-|-
|1| [💼🐌🤵 `Query@Broker`](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>) | Ask for user data in specific [Schema Codes 🧩](<../../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>)
|2| [👥🚀🕸 `Queryable@Graph`](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/05 👥🚀🕸 Queryable.md>) | Match user [Bind 🔗](<../../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/01 🔗 Bind.md>) with usable [Trust 👍](<../../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) paths
|3| [👥🚀🕸 `Translate@Graph`](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/06 👥🚀🕸 Translate.md>) | Translate the [Schema Codes 🧩](<../../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>)
|4| [🤗⏩🧑‍🦰 Prompt 🤔](<../../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) ask users to share their [Tokens 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/$ 🎫 Token.md>)
|5| [🤵🐌📣 `Share@Notifier`](<../../../6 🅰️ APIs/65 📣🅰️ Notifier/02 📣💬🅰️ Chats/22 🤵🐌📣 Share.md>) | Proxy the share order to the [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
|6| [🤵🐌💼 `Receive@Consumer`](<../../../6 🅰️ APIs/30 💼🅰️ Consumer/03 🧑‍🦰🐌💼 Receive.md>) | Send the shared offline [Tokens 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/$ 🎫 Token.md>)
|7| [👥🚀🕸 `Trusts@Graph`](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/03 👥🚀🕸 Trusts.md>) | Verify if the [Issuers 🎴](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/40 🎴 Issuers/$ 🎴🎭 Issuer role.md>) are [Trustworthy 👍](<../../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>)
|8| [👥🚀🕸 `PublicKey@Graph`](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/07 👥🚀🕸 Public Key.md>) | Get the DKIM public key of each [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/$ 🎫 Token.md>)
|9| [💼⏩🤵 Token status 🎫](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/05 💼⏩🤵 Token status.md>) | Ask the Token's [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) if it is still active
|

<br/>

## FAQ

1. **Why isn't the verification done on the Issuer?**

    `Privacy` [Issuer 🎴 domains](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/40 🎴 Issuers/$ 🎴🎭 Issuer role.md>) should not be allowed to track users by knowing in which [Consumer 💼 domains](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) their [Tokens 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/$ 🎫 Token.md>) where used.

    ---
    <br/>