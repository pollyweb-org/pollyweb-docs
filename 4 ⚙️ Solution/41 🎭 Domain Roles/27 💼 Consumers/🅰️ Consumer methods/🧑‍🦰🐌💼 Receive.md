# 🧑‍🦰🐌💼 Receive @ Consumer


> Part of the [💼⏩🧑‍🦰 Share Token @ Consumer](<../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token 🎫.md>) flow:
> <br/>• succeeds [`Share@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/4 🎫 Tokens/2 🤵🐌📣 Share.md>)


* [Wallet 🧑‍🦰 apps](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) send [Tokens 🎫](<../../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) to a [Consumer 💼 domain](<../$ 💼🎭 Consumer role.md>).



<br/>

## Async Message 🐌

```yaml
Header:
    From: Anonymous
    To: any-consumer.com
    Subject: Receive@Consumer
Body: 
    ChatID: <chat-uuid>
    Tokens: 
      - Issuer: any-issuer.com
        TokenID: ANY-TOKEN-KEY
        Code: airlines.any-igo.org/SSR/WCH:1 
        ...
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | `Anonymous`
| | `To`| string | [Consumer 💼](<../$ 💼🎭 Consumer role.md>) from [`Share@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/4 🎫 Tokens/2 🤵🐌📣 Share.md>)
| | `Subject`| string | `Receive@Consumer`
| Body | `ChatID` | string | [Chat 💬](<../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID from [`Share@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/4 🎫 Tokens/2 🤵🐌📣 Share.md>)
| | `Tokens`  | array | List of `Token` objects
| Token |  `Issuer` | string | [Issuer 🎴](<../../40 🎴 Issuers/$ 🎴🎭 Issuer role.md>) from [`Save@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/4 🎫 Tokens/1 🤵🐌📣 Save.md>)
| | `TokenID`| string | [Token 🎫](<../../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) ID from [`Save@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/4 🎫 Tokens/1 🤵🐌📣 Save.md>)
| | ... | ... | Other [Token 🎫](<../../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) fields
|


## FAQ

1. **What's in the list of Tokens?**

    The list of [Tokens 🎫](<../../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) contains:
    * the content from the response of [`Issued@Issuer`](<../../40 🎴 Issuers/55 🎴🅰️ Issuer/01 🧑‍🦰🚀🎴 Issued.md>)
    * stored in local files during [`Saved@Broker`](<../../../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/53 🧑‍🦰🐌🤵 Saved.md>).


    ---
    <br/>