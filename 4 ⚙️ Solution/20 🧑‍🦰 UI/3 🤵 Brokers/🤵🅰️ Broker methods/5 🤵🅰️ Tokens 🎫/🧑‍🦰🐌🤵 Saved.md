<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfTe327e788ccd54eefbe5f7e844 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L88 -->

# 🧑‍🦰🐌🤵 Saved @ Broker

> [Wallet 🧑‍🦰 apps](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>) inform [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) where the file with the [Token 🎫](<../../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) details was stored locally on the device.

> Part of the [🎴⏩🧑‍🦰 Offer Token @ Issuer](<../../../1 🧑‍🦰 Wallets/🧑‍🦰⏩ Wallet flows/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) flow:
> <br>• triggered by [`Save@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/4 🎫 Tokens/1 🤵🐌📣 Save.md>) message

<br/>

## Async Message 🐌

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.com
    Subject: Saved@Broker

Body:
    ChatID: <chat-uuid>
    TokenID: <token-uuid>
    Issuer: any-host.com
    Path: /storage/nlweb/tokens/<issuer>/<token-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|uuid | [Wallet 🧑‍🦰](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
||`To`|string| [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
||`Subject`|string|`Saved@Broker`
|Body  |`ChatID` |uuid  | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Save@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/4 🎫 Tokens/1 🤵🐌📣 Save.md>)
|      |`TokenID` |uuid  | [Token 🎫](<../../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) ID from [`Save@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/4 🎫 Tokens/1 🤵🐌📣 Save.md>)
|      |`Issuer`  |string| [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) from [`Save@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/4 🎫 Tokens/1 🤵🐌📣 Save.md>)
|      |`Path`    |string| Path to the local file
|