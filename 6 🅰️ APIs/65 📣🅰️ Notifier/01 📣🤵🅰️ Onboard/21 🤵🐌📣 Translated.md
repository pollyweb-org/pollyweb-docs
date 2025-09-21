<!-- Docs: https://quip.com/PCunAKUqSObO/-Notifier#temp:C:UKE27bcb1e6dd3e493f88b36b695 -->
<!-- Code: -->
<!-- Test: -->


# 🤵🐌📣 Translated @ Notifier

> Brokers domains call [Notifier 📣 domains](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) to re-render translated contented.


> Used by [🧑‍🦰👉🤵 Translate](<../../../5 ⏩ Flows/02 🧑‍🦰👉 Wallets/10 👉🤵 Set-up/12 🧑‍🦰👉🤵 Translate.md>) 

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
|Header|`From`|string | Broker domain name
||`To`|string| [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) name
||`Subject`|string|`Translated@Notifier`
|Body  |`WalletID` |UUID  | Wallet ID on the Broker domain
|      |`Language` |enum  | ISO language code
|