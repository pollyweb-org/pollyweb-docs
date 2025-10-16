# 🧑‍🦰🐌💼 Receive @ Consumer


> Part of the [💼⏩🧑‍🦰 Share Token @ Consumer](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in Prompts 🤔/🧑‍🦰👉💼 Share Token 🎫.md>) flow:
> <br/>• succeeds [`Share@Notifier`](<../../../20 🧑‍🦰 UI/2 📣 Notifiers/📣🅰️ Notifier methods/4 🎫 Tokens/2 🤵🐌📣 Share.md>)


* [Wallet 🧑‍🦰 apps](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>) send [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) to a [Consumer 💼 domain](<../💼🎭 Consumer role.md>).



<br/>

## Async Message 🐌

```yaml
Header:
    From: Anonymous
    To: any-consumer.dom
    Subject: Receive@Consumer
Body: 
    ChatID: <chat-uuid>
    Tokens: 
      - Issuer: any-issuer.dom
        TokenID: ANY-TOKEN-KEY
        Code: airlines.any-igo.dom/SSR/WCH:1 
        ...
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | `Anonymous`
| | `To`| string | [Consumer 💼](<../💼🎭 Consumer role.md>) from [`Share@Notifier`](<../../../20 🧑‍🦰 UI/2 📣 Notifiers/📣🅰️ Notifier methods/4 🎫 Tokens/2 🤵🐌📣 Share.md>)
| | `Subject`| string | `Receive@Consumer`
| Body | `ChatID` | string | [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Share@Notifier`](<../../../20 🧑‍🦰 UI/2 📣 Notifiers/📣🅰️ Notifier methods/4 🎫 Tokens/2 🤵🐌📣 Share.md>)
| | `Tokens`  | array | List of `Token` objects
| Token |  `Issuer` | string | [Issuer 🎴](<../../Issuers 🎴/🎴🎭 Issuer role.md>) from [`Save@Notifier`](<../../../20 🧑‍🦰 UI/2 📣 Notifiers/📣🅰️ Notifier methods/4 🎫 Tokens/1 🤵🐌📣 Save.md>)
| | `TokenID`| string | [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) ID from [`Save@Notifier`](<../../../20 🧑‍🦰 UI/2 📣 Notifiers/📣🅰️ Notifier methods/4 🎫 Tokens/1 🤵🐌📣 Save.md>)
| | ... | ... | Other [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) fields
|


## FAQ

1. **What's in the list of Tokens?**

    The list of [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) contains:
    * the content from the response of [`Issued@Issuer`](<../../Issuers 🎴/🎴🅰️ Issuer methods/🧑‍🦰🚀🎴 Issued.md>)
    * stored in local files during [`Saved@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🧑‍🦰🐌🤵 Saved.md>).


    ---
    <br/>