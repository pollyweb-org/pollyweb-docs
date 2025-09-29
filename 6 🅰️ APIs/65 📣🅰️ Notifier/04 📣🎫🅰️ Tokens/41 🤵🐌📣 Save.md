<!-- #TODO -->


# 🤵🐌📣 Save @ Notifier

> Part of the [🧑‍🦰👉🎴 Offer Token @ Issuer](<../../../5 ⏩ Flows/60 🎴⏩ Issuers/01 🎴⏩🧑‍🦰 Offer token.md>) flow.

<br/>

```yaml
Header:
    From: any-broker.com
    To: any-notifier.com
    Subject: Save@Notifier
Body:
    ...

```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
||`To`|string| [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) name
||`Subject`|string|`Save@Notifier`
|Body  |`Token` |uuid  | 
