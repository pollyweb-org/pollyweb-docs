# 🤵🐌🎴 Accepted @ Issuer


> Part of the [🧑‍🦰👉🎴 Save Token @ Issuer](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save Token.md>) flow.

* Tells an [Issuer 🎴 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) if a [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) was accepted or rejected.

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.com
    To: any-issuer.com
    Subject: Accepted@Issuer
Body:
    Token: <token-uuid>
    Result: Yes
```


|Object |Property |Type|Description
|-|-|-|-
|Header | `From`  | string  | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
|       | `To`    | string  | [Issuer 🎴 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) name
||`Subject`|string|`Token@Issuer` 
| Body  | `TokenID`| string | [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) ID from [`Offer@Broker`](<../15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/51 🎴🐌🤵 Offer.md>)
|| `Result`| enum | `Yes` `No` 
|

<br/>

## FAQ

1. **Why is the result for?**

    The result allows the [Issuer 🎴 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) to force the user to save the [Token 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>), as in the following example from the [Buy entry at a dance club 🤝 use case](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/12 🌐 Web: Buy entry 🎟️.md>).

    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Msgs/00 👥 Domain.md>) | [Prompt](<../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    |...
    | 🕺 Club       | ℹ️ Entry paid.
    | 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save entry? [Yes, No]  | > No
    | 🕺 Club       | ℹ️ You need to save the entry.
    | 🤵 [Broker](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 Save entry? [Yes, No]  | > Yes
    | 🕺 Club       | ✅ All set.
    |