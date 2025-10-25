<!-- https://quip.com/YdJpA3idWduO#temp:C:afPf2204358162a42529b4a902e9 -->

# 🎴⏩🧑‍🦰 Save Token @ Wallet

* On the [Wallet 🧑‍🦰 app](<../../🧑‍🦰🛠️ Wallet app.md>), 
    * a user accepts a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) 
    * offered by an [Issuer 🎴 domain](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>).


<br/>

## 💬 Chat 

Consider the following excerpt from the [Book restaurant table 🤝 use case](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>).

| [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| 🎴 [Issuer](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) | ℹ️ Issuing your token...
| 🤵 [Broker](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 Save token? [Yes, No]  | > Yes
| 🎴 [Issuer](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) | ✅ Saved to your wallet.
||

<br/>

## 😃 Talker 

The associated [Talker 😃](<../../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) uses the [`ISSUE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...methods 🤵/ISSUE 🎫/ISSUE 🎫 msg.md>) command.

```yaml
- INFO|Issuing your token...
- ISSUE >> $token
- IF|{$accepted}:
    Then: SUCCESS|Saved to your wallet.
    Else: FAILURE|You rejected the token.
```

| [Command ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>) | Purpose
|-|-
| 🎫 [`ISSUE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...methods 🤵/ISSUE 🎫/ISSUE 🎫 msg.md>) | Call the [Save Token ⏩ flow](<👉🎴 Save token.md>).
|

<br/>

## ⏩ Flow diagram 

![Accept](<../../.📎 Assets/Tokens 📎/⚙️🎫 Save.png>)


| # | Call | Notes
|-|-|-
|1| [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Users run transactions with [Issuers 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)
|2| [🎴🐌🤵 `Offer@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/5 ...for Tokens 🎫/🎴🐌🤵 Offer.md>) | In the [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>), [Issuers 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) offer a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
|3|[👥🚀🕸 `Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | [Brokers 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) translate [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
| 4 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) ask for user acceptance
| 5 | [🤵🐌📣 `Save@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/4 🎫 Tokens/1 🤵🐌📣 Save.md>) | [Brokers 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) send the [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) ID
| 6 | [🧑‍🦰🚀🎴 `Issued@Issuer`](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/🧑‍🦰🚀🎴 Issued.md>) | [Wallets 🧑‍🦰](<../../🧑‍🦰🛠️ Wallet app.md>) download it and save it
| 7 | [🧑‍🦰🐌🤵 `Saved@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/5 ...for Tokens 🎫/Saved/🧑‍🦰🐌🤵 Saved.md>) | [Wallets 🧑‍🦰](<../../🧑‍🦰🛠️ Wallet app.md>) tell [Brokers 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) it's saved
| 8 | [🤵⏩🧑‍🦰 Update Tokens 🎫](<../../../Brokers 🤵/🤵⏩ Broker flows/Update Tokens 🎫/🤵⏩🧑‍🦰 Update Tokens 🎫.md>) | [Brokers 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) tell [Wallets 🧑‍🦰](<../../🧑‍🦰🛠️ Wallet app.md>) to update the list
| 9 | [🤵🐌🎴 `Accepted@Issuer`](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/🤵🐌🎴 Accepted.md>) | [Brokers 🤵](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) tell [Issuers 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) of acceptance
| A | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Issuers 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) continue the [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>)
||

<br/>

## FAQ

1. **Why the extra step to download the Token?**

    `Privacy` [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) are not proxied via the [Broker 🤵 domain](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) to protect user's privacy.    
    * Instead, [Wallet 🧑‍🦰 apps](<../../🧑‍🦰🛠️ Wallet app.md>) download the [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) directly from [Issuer 🎴 domain](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>).
    * Accepted [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) are stored locally, and only the path is sent to the [Broker 🤵 domain](<../../../Brokers 🤵/🤵🤲 Broker helper.md>).

    ---
    <br/>