<!-- Docs: https://quip.com/PCunAKUqSObO/-Notifier#temp:C:UKE27bcb1e6dd3e493f88b36b695 -->
<!-- Code: -->
<!-- Test: -->

# 🤵🐌📣 Translated @ Notifier

> Brokers domains call [Notifier 📣 domains](<../../📣👥 Notifier domain.md>) to re-render translated contented.


> Used by [🧑‍🦰👉🤵 Translate](<../../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in App 🏠/💬🤵 Translate.md>) 

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Translated@Notifier
Body:
    WalletID: <wallet-uuid>
    Language: en-us
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵 domain](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) name
||`To`|string| [Notifier 📣](<../../📣👥 Notifier domain.md>) from [`Onboard@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/📣🚀🤵 Onboard.md>)
||`Subject`|string|`Translated@Notifier`
|Body  |`WalletID` |uuid  | [Wallet 🧑‍🦰](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>) ID from [`Translate@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/🧑‍🦰🐌🤵 Translate.md>)
|      |`Language` |enum  | ISO code from [`Translate@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/🧑‍🦰🐌🤵 Translate.md>)
|