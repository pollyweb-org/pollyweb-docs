
<!-- Docs: https://quip.com/zaYoA4kibXAP/-Broker-Wallets#temp:C:DQN0cc419509625497ea39fa08e9 -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/143c4c876bdd0dd8b120bdfecf20ef6b268ad20f/python/roles/broker/BROKER_WALLETS.py#L76 -->


# 🧑‍🦰🐌🤵 Translate @ [Broker](<../../🤵🤲 Broker helper.md>)

> The user requests the [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) to change the language in the [Wallet 🧑‍🦰 app](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>).

> Used in: [🧑‍🦰👉🤵 Translate @ Wallet](<../../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in App 🏠/🧑‍🦰💬🤵 Translate.md>).

<br/>

## Async Message 🐌

```yaml
Header: 
    From: <wallet-uuid>
    To: any-broker.com
    Subject: Translate@Broker

Body:
    Language: en-us
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | uuid | [Wallet 🧑‍🦰](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
||`To`| string | [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
||`Subject`| string | `Translate@Broker`
|Body|`Language`| enum | ISO language code.
|