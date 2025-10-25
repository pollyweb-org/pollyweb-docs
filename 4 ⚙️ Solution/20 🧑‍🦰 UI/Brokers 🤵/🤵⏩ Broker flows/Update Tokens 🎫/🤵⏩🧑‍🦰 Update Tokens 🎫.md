# 🤵⏩🗄️ Update Tokens @ Broker

> The [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) updates the list of [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>).

> Used in:
> <br/>• [🎴⏩🧑‍🦰 Offer Token @ Issuer](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉🎴 Save token.md>) 
> <br/>• [🧑‍🦰👉🤵 Remove Token @ Wallet](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Tokens 🎫/💬🤵 Remove 🎫 chat.md>)
> <br/>• [🧑‍🦰👉🤵 List Tokens @ Wallet](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/💬🤵 List Tokens 🎫.md>)

<br/>


## Flow diagram

![Update tokens](<../../.📎 Assets/⚙️🎫 Update tokens.png>)


| # | Call | Notes |
|-|-|-
| 1 | [🤵🐌📣 `Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>)| [Brokers 🤵](<../../🤵🤲 Broker helper.md>) tell [Notifiers 📣](<../../../Notifiers 📣/📣👥 Notifier domain.md>) to update [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
| 2 | [🧑‍🦰🚀🤵 `Tokens@Broker`](<../../🤵🅰️ Broker methods/5 ...for Tokens 🎫/🧑‍🦰🚀🤵 Tokens.md>) | [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) get [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) from [Brokers 🤵](<../../🤵🤲 Broker helper.md>)
||
