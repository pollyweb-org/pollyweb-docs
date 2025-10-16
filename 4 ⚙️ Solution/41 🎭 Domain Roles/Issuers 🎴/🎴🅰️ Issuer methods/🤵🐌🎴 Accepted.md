# 🤵🐌🎴 Accepted @ Issuer


> Part of the [🧑‍🦰👉🎴 Save Token @ Issuer](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰⏩ Wallet flows/40 👉🎫 Tokens/🧑‍🦰👉🎴 Save token.md>) flow.

* Tells an [Issuer 🎴 domain](<../🎴🎭 Issuer role.md>) if a [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) was accepted or rejected.

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
|Header | `From`  | string  | [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) name
|       | `To`    | string  | [Issuer 🎴 domain](<../🎴🎭 Issuer role.md>) name
||`Subject`|string|`Token@Issuer` 
| Body  | `TokenID`| string | [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) ID from [`Offer@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🎴🐌🤵 Offer.md>)
|| `Result`| enum | `Yes` `No` 
|

<br/>

## FAQ

1. **Why is the result for?**

    The result allows the [Issuer 🎴 domain](<../🎴🎭 Issuer role.md>) to force the user to save the [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>), as in the following example from the [Buy entry at a dance club 🤝 use case](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/12 🌐 Web: Buy entry 🎟️.md>).

    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    |...
    | 🕺 Club       | ℹ️ Entry paid.
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Save entry? [Yes, No]  | > No
    | 🕺 Club       | ℹ️ You need to save the entry.
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Save entry? [Yes, No]  | > Yes
    | 🕺 Club       | ✅ All set.
    |