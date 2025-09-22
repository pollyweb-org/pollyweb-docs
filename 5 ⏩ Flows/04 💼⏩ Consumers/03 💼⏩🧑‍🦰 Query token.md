<!-- #TODO -->

# 👉 Share token




## Flow diagram

![alt text](<.📎 Assets/⚙️ Query Token.png>)

|#| Step | Purpose
|-|-|-
|1| [💼🐌🤵 Query @ Broker](<../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>) | In a Chat, a consumer asks access to user data of one or mode Schema Codes.
|2| [👥🚀🕸 Queryable @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/05 👥🚀🕸 Queryable.md>) | The Broker matches possible user Vaults with the Schema Codes, and asks a Graph to filters out the ones without usable Trust paths.
|3| [👥🚀🕸 Translate @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/06 👥🚀🕸 Translate.md>) | The Broker asks a Graph to translate the Schema Codes to the Chat's language.
|4| [🤵🐌📣 Share @ Notifier](<../../6 🅰️ APIs/65 📣🅰️ Notifier/02 📣💬🅰️ Chats/22 🤵🐌📣 Share.md>) | The Broker sends the share request to the user via the Notifier domain, who then delivers it to the Wallet app.
|5| [🤵🐌💼 Verify @ Consumer](<../../6 🅰️ APIs/30 💼🅰️ Consumer/02 🧑‍🦰🐌💼 Verify.md>)
|6| [👥🚀🕸 Trusts @ Graph](<../../6 🅰️ APIs/45 🕸🅰️ Graph/03 👥🚀🕸 Trusts.md>)
|7| [💼🐌🎴 Verify @ Issuer](<../../6 🅰️ APIs/55 🎴🅰️ Issuer/02 💼🐌🎴 Verify.md>)
|8| [🎴🐌💼 Verified @ Consumer](<../../6 🅰️ APIs/30 💼🅰️ Consumer/03 🎴🐌💼 Verified.md>)
|