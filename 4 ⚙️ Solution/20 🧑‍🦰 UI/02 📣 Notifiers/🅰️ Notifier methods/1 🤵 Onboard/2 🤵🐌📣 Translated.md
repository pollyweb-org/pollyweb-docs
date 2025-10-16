<!-- Docs: https://quip.com/PCunAKUqSObO/-Notifier#temp:C:UKE27bcb1e6dd3e493f88b36b695 -->
<!-- Code: -->
<!-- Test: -->

# 🤵🐌📣 Translated @ Notifier

> Brokers domains call [Notifier 📣 domains](<../../📣 Notifier domain.md>) to re-render translated contented.


> Used by [🧑‍🦰👉🤵 Translate](<../../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/10 👉🤵 Set-up/12 🧑‍🦰👉🤵 Translate.md>) 

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.com
    To: any-notifier.com
    Subject: Translated@Notifier
Body:
    WalletID: <wallet-uuid>
    Language: en-us
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵 domain](<../../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) name
||`To`|string| [Notifier 📣](<../../📣 Notifier domain.md>) from [`Onboard@Broker`](<../../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/10 🤵🅰️ Wallets 🧑‍🦰/📣🚀🤵 Onboard.md>)
||`Subject`|string|`Translated@Notifier`
|Body  |`WalletID` |uuid  | [Wallet 🧑‍🦰](<../../../01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) ID from [`Translate@Broker`](<../../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/10 🤵🅰️ Wallets 🧑‍🦰/🧑‍🦰🐌🤵 Translate.md>)
|      |`Language` |enum  | ISO code from [`Translate@Broker`](<../../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/10 🤵🅰️ Wallets 🧑‍🦰/🧑‍🦰🐌🤵 Translate.md>)
|