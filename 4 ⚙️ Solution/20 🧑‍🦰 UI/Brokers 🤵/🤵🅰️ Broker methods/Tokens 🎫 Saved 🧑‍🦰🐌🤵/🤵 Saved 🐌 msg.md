<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfTe327e788ccd54eefbe5f7e844 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L88 -->

# 🧑‍🦰🐌🤵 Saved @ Broker

> Implemented by the [`Saved` 📃 script](<🤵 Saved 📃 handler.md>)

> Purpose:
* [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) 
    * inform [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) 
    * where the file with the [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) details 
    * was stored locally on the device.

> Part of the [`Save Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>):
* triggered by [`Save@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>) message

<br/>

## Async Message 🐌

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Saved@Broker

Body:
    Token: <token-uuid>
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
|Header|`From`|uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`To`|string| [Broker 🤵](<../../🤵🤲 Broker helper.md>) | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`Subject`|string|`Saved@Broker`
|Body  |`Token` |uuid  | [Broker 🤵](<../../🤵🤲 Broker helper.md>) key | [`Save@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)
|