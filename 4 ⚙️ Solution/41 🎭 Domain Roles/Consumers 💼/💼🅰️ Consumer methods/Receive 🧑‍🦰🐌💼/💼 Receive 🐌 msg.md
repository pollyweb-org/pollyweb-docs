# 🧑‍🦰🐌💼 Receive @ Consumer

> Implementations
* Implemented by the [`Receive` 📃 script](<💼 Receive 📃 handler.md>)

> Flow
* Part of the [`Share Token` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>) 
* Succeeds the [`Share@Notifier` 🅰️ method](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>)

> Purpose

* [Wallet 🧑‍🦰 apps](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) send [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) to a [Consumer 💼 domain](<../../💼🎭 Consumer role.md>).



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
        Key: token-1234
        # Properties from Save@Notifier
        Schema: .TOKEN
        Domain: any-issuer.dom
        Properties:
            Property1: Value1
            Property2: Value2
        Issued: 2024-09-21T12:34:00Z
        Starts: 2024-01-10T13:45:00.000Z
        Expires: 2028-12-10T13:45:00.000Z
        Signature: ABCMIQDALK2Fd...
        DKIM: pk1
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
| Header|`From`|domain| `Anonymous`
| |`To`|domain| [Consumer 💼](<../../💼🎭 Consumer role.md>) | [`Share@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>)
| | `Subject`| string | `Receive@Consumer`
| Body | `Hook` | uuid | [Issuer 🎴](<../../../Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) Hook | [`Share@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>)
| Tokens | `Token` | uuid | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) ID | [`Share@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>) | [`Status@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Status 💼🚀🤵/🤵 Status 🚀 request.md>)
|| `Key`| string | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) Key | [`Share@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>)
||...| ... | Properties | [`Save@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)
|



<br/>

## FAQ

1. **What's in the list of Tokens?**

    The list of [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) contains:
    * the `Key` from the [`Offer@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) request
    * plus the content from the response of [`Issued@Issuer`](<../../../Issuers 🎴/🎴🅰️ Issuer methods/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 request.md>)
    * stored in local files during [`Saved@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>).


    ---
    <br/>