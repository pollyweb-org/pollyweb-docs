# 🪣 Notifiers

> Contains [Notifier 📣 domains](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣👥 Notifier domain.md>)

## Schema

Here's the [Itemized 🛢 schema](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).

```yaml
# Notifiers.yaml
Key: Notifier
Children:
    Wallets: Wallets|Notifier
```

| Link | Table | Contains
|-|-|-
| Children | [`Wallets` 🪣](<🤵🪣 Wallets.md>) | [Wallet 🧑‍🦰 apps](<../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
|


## Example

Here's the [`GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET 🗺️ item.md>) result.

```yaml
# GET|Notifiers|any-notifier.dom
Notifier: any-notifier.dom
```
