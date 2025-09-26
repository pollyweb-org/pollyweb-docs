# 🤵⏩🗄️ Update Tokens @ Broker

> The [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) updates the list of [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>).

> Used in:
> <br/>• [🎴⏩🧑‍🦰 Offer Token @ Issuer](<../60 🎴⏩ Issuers/01 🎴⏩🧑‍🦰 Offer token.md>) 
> <br/>• [🧑‍🦰👉🤵 Remove Token @ Wallet](<../90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/03 🧑‍🦰👉🤵 Remove token.md>)
> <br/>• [🧑‍🦰👉🤵 List Tokens @ Wallet](<../90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/01 🧑‍🦰👉🤵 List tokens.md>)

<br/>


## Flow diagram

![Update tokens](<.📎 Assets/⚙️🎫 Update tokens.png>)


| # | Call | Notes |
|-|-|-
| 1 | [🤵🐌📣 Updated @ Notifier](<../../6 🅰️ APIs/65 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/23 🤵🐌📣 Updated.md>)| The [Broker 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) tells the [Notifier 📣](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) to update the [Wallet 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| 2 | [🧑‍🦰🚀🤵 Tokens @ Broker](<../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/54 🧑‍🦰🚀🤵 Tokens.md>) | The [Wallet 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) gets the [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) from the [Broker 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
||
