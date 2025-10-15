# 🤵⏩🗄️ Update Tokens @ Broker

> The [Broker 🤵 domain](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) updates the list of [Tokens 🎫](<../../4 ⚙️ Solution/30 🧩 Data/30 🎫 Tokens/🎫 Token.md>).

> Used in:
> <br/>• [🎴⏩🧑‍🦰 Offer Token @ Issuer](<../90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) 
> <br/>• [🧑‍🦰👉🤵 Remove Token @ Wallet](<../90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/03 🧑‍🦰👉🤵 Remove token.md>)
> <br/>• [🧑‍🦰👉🤵 List Tokens @ Wallet](<../90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/01 🧑‍🦰👉🤵 List tokens.md>)

<br/>


## Flow diagram

![Update tokens](<.📎 Assets/⚙️🎫 Update tokens.png>)


| # | Call | Notes |
|-|-|-
| 1 | [🤵🐌📣 `Updated@Notifier`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>)| [Brokers 🤵](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) tell [Notifiers 📣](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/📣 Notifier domain.md>) to update [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| 2 | [🧑‍🦰🚀🤵 `Tokens@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/54 🧑‍🦰🚀🤵 Tokens.md>) | [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) get [Tokens 🎫](<../../4 ⚙️ Solution/30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) from [Brokers 🤵](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>)
||
