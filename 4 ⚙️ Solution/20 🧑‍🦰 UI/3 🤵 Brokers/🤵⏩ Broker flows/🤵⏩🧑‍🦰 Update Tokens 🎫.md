# 🤵⏩🗄️ Update Tokens @ Broker

> The [Broker 🤵 domain](<../🤵🤲 Broker helper.md>) updates the list of [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>).

> Used in:
> <br/>• [🎴⏩🧑‍🦰 Offer Token @ Issuer](<../../1 🧑‍🦰 Wallets/🧑‍🦰👉 Wallet flows/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) 
> <br/>• [🧑‍🦰👉🤵 Remove Token @ Wallet](<../../1 🧑‍🦰 Wallets/🧑‍🦰👉 Wallet flows/40 👉🎫 Tokens/03 🧑‍🦰👉🤵 Remove token.md>)
> <br/>• [🧑‍🦰👉🤵 List Tokens @ Wallet](<../../1 🧑‍🦰 Wallets/🧑‍🦰👉 Wallet flows/40 👉🎫 Tokens/01 🧑‍🦰👉🤵 List tokens.md>)

<br/>


## Flow diagram

![Update tokens](<../.📎 Assets/⚙️🎫 Update tokens.png>)


| # | Call | Notes |
|-|-|-
| 1 | [🤵🐌📣 `Updated@Notifier`](<../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>)| [Brokers 🤵](<../🤵🤲 Broker helper.md>) tell [Notifiers 📣](<../../2 📣 Notifiers/📣👥 Notifier domain.md>) to update [Wallets 🧑‍🦰](<../../1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| 2 | [🧑‍🦰🚀🤵 `Tokens@Broker`](<../🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🧑‍🦰🚀🤵 Tokens.md>) | [Wallets 🧑‍🦰](<../../1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) get [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) from [Brokers 🤵](<../🤵🤲 Broker helper.md>)
||
