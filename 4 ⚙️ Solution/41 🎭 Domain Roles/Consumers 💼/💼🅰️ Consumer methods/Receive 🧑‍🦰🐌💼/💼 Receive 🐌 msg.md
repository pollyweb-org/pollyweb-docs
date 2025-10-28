# 🧑‍🦰🐌💼 Receive @ Consumer

> Implementations
* Implemented by the [`Receive` 📃 script](<💼 Receive 📃 handler.md>)

> Flow
* Part of the [`Share Token` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉💼 Share Token 🎫.md>) 
* Succeeds the [`Share@Notifier` 🅰️ method](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>)

> Purpose

* [Wallet 🧑‍🦰 apps](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) send [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) to a [Consumer 💼 domain](<../../💼🎭 Consumer role.md>).



<br/>

## Async Message 🐌

```yaml
Header:
    From: Anonymous
    To: any-consumer.dom
    Subject: Receive@Consumer

Body: 
    Hook: <hook-uuid>
    Tokens: 
      - Token: <token-uuid>
        ...
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | `Anonymous`
| | `To`| string | [Consumer 💼](<../../💼🎭 Consumer role.md>) from [`Share@Notifier`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>)
| | `Subject`| string | `Receive@Consumer`
| Body | `Hook` | uuid | `Hook` from [`Share@Notifier`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>)
| | `Tokens`  | array | List of `Token` objects
| Tokens |  `Token`| string | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) from [`Save@Notifier`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)
| | ... | ... | Other [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) fields
|



<br/>

## FAQ

1. **What's in the list of Tokens?**

    The list of [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) contains:
    * the content from the response of [`Issued@Issuer`](<../../../Issuers 🎴/🎴🅰️ Issuer methods/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 request.md>)
    * stored in local files during [`Saved@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>).


    ---
    <br/>