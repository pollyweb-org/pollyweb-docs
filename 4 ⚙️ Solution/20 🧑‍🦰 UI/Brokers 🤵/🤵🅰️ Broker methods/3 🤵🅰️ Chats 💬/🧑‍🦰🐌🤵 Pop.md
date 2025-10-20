# 🧑‍🦰🐌🤵 Pop @ Broker

* Opens a new [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) 
    * with the [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>)
    * with a given context.

<br/>

## Chat

| [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| | | > Token 🎫 |
| | | > Broker 🤵 |
| 🤵 [Broker](<../../🤵🤲 Broker helper.md>) | ℹ️ Context: Token bla, bla
| 🤵 [Broker](<../../🤵🤲 Broker helper.md>) | 🤗 Hi! What do you need? <br/> - [ Remove ] Token <br/> - [ Something else ] 
|

<br/>

## Async Message 🐌

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Pop@Broker

Body:
    Reference: <reference-uuid>
    Context: TOKEN
    Key: <token-uuid>
```

| Object | Property | Type |Description
|-|-|-|-
| Header | `From`    | string | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|| `To`      | string | [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|| `Subject` | string | `Pop@Broker`
| Body | `Reference` | uuid | Reference for [`Converse@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)
|       | `Context`  | enum | `HOST` `ISSUER` `VAULT` `BIND` `TOKEN` 
|       | `Key` | uuid   | Optional index for the context
|

<br/>

## Handler

```yaml
# Get the Wallet 🧑‍🦰
- GET|Wallets|$.Msg.Header.From >> $wallet

# Verify the Message.
- VERIFY|$.Msg|$wallet.PublicKey

# Handle the context.
- CASE|$.Msg.Body.Context:
    TOKEN: TALK|PopToken
    VAULT: TALK|PopVault
    BIND : TALK|PopBind
```

|Talkers | Details
|-|-
| [`PopToken 🔆`](<../../🤵🔆 Broker locators/🤵🔆 Pop Token.md>) | Implements [🧑‍🦰💬🤵 Remove Token 🎫](<../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Tokens 🎫/💬🤵 Remove 🎫.md>)
| [`PopVault 🔆`](<../../🤵🔆 Broker locators/🤵🔆 Pop Vault.md>) | Implements [🧑‍🦰💬🤵 Unbind Vault](<../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Vaults 🗄️/💬🤵 Unbind 🗄️.md>)
|