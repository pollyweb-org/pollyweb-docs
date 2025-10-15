
# 🤵🐌📣 Revoked @ [Notifier](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/$ 📣 Notifier domain.md>)

> Used in [🧑‍🦰👉🤵 Remove token](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/03 🧑‍🦰👉🤵 Remove token.md>).

<br/>

```yaml
Header:
    From: any-broker.com
    To: any-notifier.com
    Subject: Remove@Notifier
Body:
    Path: /storage/nlweb/tokens/<issuer>/<token-uuid>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) name
||`To`|string| [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/$ 📣 Notifier domain.md>) name
||`Subject`|string|`Remove@Broker`
|Body  |`Path`    |string| Path from [`Save@Notifier`](<41 🤵🐌📣 Save.md>)
|