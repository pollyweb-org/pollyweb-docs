
# 🤵🐌📣 Revoked @ [Notifier](<../../📣👥 Notifier domain.md>)

> Used in [🧑‍🦰👉🤵 Remove token](<../../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in Tokens 🎫/🧑‍🦰💬🤵 Remove 🎫.md>).

<br/>

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Remove@Notifier
Body:
    Path: /storage/nlweb/tokens/<issuer>/<token-uuid>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵 domain](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) name
||`To`|string| [Notifier 📣 domain](<../../📣👥 Notifier domain.md>) name
||`Subject`|string|`Remove@Broker`
|Body  |`Path`    |string| Path from [`Save@Notifier`](<1 🤵🐌📣 Save.md>)
|