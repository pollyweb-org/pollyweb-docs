<!-- https://quip.com/YdJpA3idWduO#temp:C:afPf2204358162a42529b4a902e9 -->

# 🧑‍🦰👉🎴 Accept token @ [Wallet](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) 


## Privacy

- [Tokens 🎫](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/01 🎫 Token.md>) are not proxied via the [Broker 🤵](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
  - Instead, [Wallets 🧑‍🦰](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) download the [Token 🎫](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/01 🎫 Token.md>) directly from [Issuers 🎴](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/02 🎴🎭 Issuer role.md>)
  - Accepted [Tokens 🎫](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/01 🎫 Token.md>) are stored locally, and only the path is sent to the [Broker 🤵](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)


## Chat 💬

| Service | Prompt | User
| - | - | - |
| 🎴 [Issuer](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/02 🎴🎭 Issuer role.md>) | ⏳ Issuing your token...
| 🤵 [Broker](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save token? [Yes, No]  | > Yes
| 🎴 [Issuer](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/02 🎴🎭 Issuer role.md>) | ✅ Saved to your wallet.
||



## Flow diagram ⏩

![Accept](<./📎 Assets/⚙️ Offer.png>)



## Steps

| # | Call | Notes
|-|-|-
| 1 | [🎴🐌🤵 Offer @ Broker](<../../6 ⏳ 🅰️ APIs/02 ⏳ 🤵🅰️ Broker/50 ⏳ 🤵🅰️ Tokens 🎫/51 ⏳ 🎴🐌🤵 Offer.md>) | With the User in a [Chat 💬](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>), an [Issuer 🎴](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/02 🎴🎭 Issuer role.md>) issues a [Token 🎫](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/01 🎫 Token.md>)
| 2 | [🤗⏩🧑‍🦰 Prompt @ Host](<../03 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | The [Broker 🤵](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) ask for user confirmation in the [Wallet 🧑‍🦰](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| 3 | [🤵🐌📣 Offer @ Notifier](<../../6 ⏳ 🅰️ APIs/12 ⏳ 📣🅰️ Notifier/04 ⏳ 📣🎫🅰️ Tokens/41 ⏳ 🤵🐌📣 Offer.md>) | The [Broker 🤵](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) proxies the [Token 🎫](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/01 🎫 Token.md>) offer
| 4 | [🧑‍🦰🚀🎴 Token @ Issuer](<../../6 ⏳ 🅰️ APIs/10 ⏳ 🎴🅰️ Issuer/01 ⏳ 🧑‍🦰🚀🎴 Token.md>) | The [Wallet 🧑‍🦰](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) downloads it from the [Issuer 🎴](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/02 🎴🎭 Issuer role.md>) and saves it
| 5 | [🧑‍🦰🐌🤵 Accepted @ Broker](<../../6 ⏳ 🅰️ APIs/02 ⏳ 🤵🅰️ Broker/50 ⏳ 🤵🅰️ Tokens 🎫/53 ⏳ 🧑‍🦰🐌🤵 Accepted.md>) | The [Wallet 🧑‍🦰](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) informs the [Broker 🤵](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) that it was accepted
| 6 | [🤵⏩🎫 Update Tokens @ Broker](<../08 🤵⏩ Brokers/04 🤵⏩🧑‍🦰 Update tokens.md>) | The [Broker 🤵](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) tells the [Wallet 🧑‍🦰](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to update the list
| 7 | [🤵🐌🎴 Accepted @ Issuer](<../../6 ⏳ 🅰️ APIs/10 ⏳ 🎴🅰️ Issuer/03 ⏳ 🤵🐌🎴 Accepted.md>) | The [Broker 🤵](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) tells the [Issuer 🎴](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/02 🎴🎭 Issuer role.md>) that it was successful
| 8 | [🤗⏩🧑‍🦰 Prompt @ Host](<../03 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | The [Issuer 🎴](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/02 🎴🎭 Issuer role.md>) continues the [Chat 💬](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>)
||
