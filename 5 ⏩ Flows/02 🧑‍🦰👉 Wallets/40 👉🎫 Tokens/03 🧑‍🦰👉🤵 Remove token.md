# 🧑‍🦰👉🤵 Remove token @ [Wallet](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>) 


## About

- When users ask their [Broker 🤵](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) to remove a [Token 🎫](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/01 ✅ 🎫 Token.md>)
    - the first does a soft delete only, hiding the [Token 🎫](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/01 ✅ 🎫 Token.md>)
    - the removal only happens after a period of time (e.g., 30 days);
    - this allows users to undo the removal for a short period.


## Chat

| Service | Prompt | User
| - | - | - |
| | | > [Token 🎫](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/01 ✅ 🎫 Token.md>)
| | | > [Broker 🤵](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) 
| 🤵 [Broker](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>)  | 😃 What do you need? <br/> - [ Remove ] token | > Remove
| 🤵 [Broker](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>)  | ✅ Token removed. <br/> - [ Undo ] removal
||


## Steps

| # | API | Description
|-|-|-
| 1 | [🧑‍🦰🐌🤗 Talker @ Host](<../../../6 ⏳ 🅰️ APIs/09 ⏳ 🤗🅰️ Host/02 ⏳ 🧑‍🦰🐌🤗 Talker.md>) | The user calls the [Broker 🤵](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) from the [Token 🎫](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/01 ✅ 🎫 Token.md>)
| 2 | [🤗⏩🧑‍🦰 Prompt @ Host](<../../03 ✅ 🤗⏩ Hosts/01 ✅ 🤗⏩🧑‍🦰 Prompt.md>) | Then tells the [Broker 🤵](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) to remove the [Token 🎫](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/01 ✅ 🎫 Token.md>) 
| 3 | [🤵⏩🎫 Update Tokens @ Broker](<../../08 ✅ 🤵⏩ Brokers/04 ✅ 🤵⏩🧑‍🦰 Update tokens.md>) | The [Broker 🤵](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) tells the [Wallet 🧑‍🦰](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>) to update the list
| 4 | [🤵🐌📣 Remove @ Notifier](<../../../6 ⏳ 🅰️ APIs/12 ⏳ 📣🅰️ Notifier/04 ⏳ 📣🎫🅰️ Tokens/42 ⏳ 🤵🐌📣 Remove.md>) | The [Broker 🤵](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) tells the [Wallet 🧑‍🦰](<../../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>) to remove it
||


## Flow diagram

![alt text](<📎 Assets/⚙️ Remove.png>)