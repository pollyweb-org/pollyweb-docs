
<!-- Docs: https://quip.com/zaYoA4kibXAP/-Broker-Wallets#temp:C:DQN0cc419509625497ea39fa08e9 -->
<!-- Source: https://github.com/jorgemjfonseca/domain-trust-framework/blob/143c4c876bdd0dd8b120bdfecf20ef6b268ad20f/python/roles/broker/BROKER_WALLETS.py#L76 -->


# 🧑‍🦰🐌🤵 Translate @ [Broker](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Part of the [`Set Language` 💬 chat](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Set Language 💬🤵/🧑‍🦰 Set Language ⏩ flow.md>)
*  Implemented by [`Language` 📃 handler](<🤵 Language 📃 handler.md>)

> Purpose
* The user requests the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) 
    * to change the language in the [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).

> Used in
* [🧑‍🦰👉🤵 Translate @ Wallet](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Set Language 💬🤵/🧑‍🦰 Set Language ⏩ flow.md>).

<br/>

## Async Message 🐌

```yaml
Header: 
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Language@Broker

Body:
    Language: en-us
```


|Object|Property|Type|Description|Origin
|-|-|-|-|-
|Header|`From`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`To`|domain| [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
||`Subject`| string | `Language@Broker`
|Body|`Language`| enum | ISO language code.
|