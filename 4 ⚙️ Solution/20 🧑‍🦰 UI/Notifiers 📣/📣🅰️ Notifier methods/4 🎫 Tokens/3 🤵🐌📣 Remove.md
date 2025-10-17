
# 🤵🐌📣 Revoked @ [Notifier](<../../📣👥 Notifier domain.md>)

> Used in [🧑‍🦰👉🤵 Remove token](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Tokens 🎫/💬🤵 Remove 🎫.md>).

<br/>

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Remove@Notifier
Body:
    WalletID: <wallet-id>
    Path: /storage/nlweb/tokens/<issuer>/<token-uuid>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵 domain](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) name
||`To`|string| [Notifier 📣 domain](<../../📣👥 Notifier domain.md>) name
||`Subject`|string|`Remove@Broker`
|Body  |`WalletID`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) ID from [`Onboard@Broker`](<../1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
||`Path`    |string| Path from [`Save@Notifier`](<1 🤵🐌📣 Save.md>)
|