<!-- https://quip.com/YdJpA3idWduO#temp:C:afPf2204358162a42529b4a902e9 -->

# 🎴⏩🧑‍🦰 Offer Token @ Wallet

* On the [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), 
    * a user accepts a [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) 
    * offered by an [Issuer 🎴 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>).


<br/>

## 💬 Chat 

Consider the following excerpt from the [Book restaurant table 🤝 use case](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>).

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🎴 [Issuer](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) | ℹ️ Issuing your token...
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save token? [Yes, No]  | > Yes
| 🎴 [Issuer](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) | ✅ Saved to your wallet.
||

<br/>

## 😃 Talker 

The associated [Talker 😃](<../../../9 😃 Talkers/10 📘 Talker specs/01 😃 Talker.md>) uses the [`OFFER`](<../../../9 😃 Talkers/60 ⏩ Msg flows/49 🎫 OFFER msg.md>) command.

```yaml
- INFO|Issuing your token...
- OFFER|{GetTokenID} >> accepted
- IF|{$accepted}:
    Then: SUCCESS|Saved to your wallet.
    Else: FAILURE|You rejected the token.
```

<br/>

## ⏩ Flow diagram 

![Accept](<.📎 Assets/⚙️ Save.png>)


| # | Call | Notes
|-|-|-
|1| [🤗⏩🧑‍🦰 Prompt 🤔](<../../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | Users run transactions with [Issuers 🎴](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>)
|2| [🎴🐌🤵 `Offer@Broker`](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/51 🎴🐌🤵 Offer.md>) | In the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>), [Issuers 🎴](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) offer a [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
|3|[👥🚀🕸 `Translate@Graph`](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/06 👥🚀🕸 Translate.md>) | [Brokers 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) translate [Schema Codes 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
| 4 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Brokers 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) ask for user acceptance
| 5 | [🤵🐌📣 `Save@Notifier`](<../../../6 🅰️ APIs/65 📣🅰️ Notifier/04 📣🎫🅰️ Tokens/41 🤵🐌📣 Save.md>) | [Brokers 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) send the [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) ID
| 6 | [🧑‍🦰🚀🎴 `Issued@Issuer`](<../../../6 🅰️ APIs/55 🎴🅰️ Issuer/01 🧑‍🦰🚀🎴 Issued.md>) | [Wallets 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) download it and save it
| 7 | [🧑‍🦰🐌🤵 `Saved@Broker`](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/53 🧑‍🦰🐌🤵 Saved.md>) | [Wallets 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) tell [Brokers 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) it's saved
| 8 | [🤵⏩🧑‍🦰 Update Tokens 🎫](<../../10 🤵⏩ Brokers/04 🤵⏩🧑‍🦰 Update tokens.md>) | [Brokers 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) tell [Wallets 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to update the list
| 9 | [🤵🐌🎴 `Accepted@Issuer`](<../../../6 🅰️ APIs/55 🎴🅰️ Issuer/02 🤵🐌🎴 Accepted.md>) | [Brokers 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) tell [Issuers 🎴](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) of acceptance
| A | [🤗⏩🧑‍🦰 Prompt 🤔](<../../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Issuers 🎴](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) continue the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
||

<br/>

## FAQ

1. **Why the extra step to download the Token?**

    `Privacy` [Tokens 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) are not proxied via the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) to protect user's privacy.    
    * Instead, [Wallet 🧑‍🦰 apps](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) download the [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) directly from [Issuer 🎴 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>).
    * Accepted [Tokens 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) are stored locally, and only the path is sent to the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>).

    ---
    <br/>