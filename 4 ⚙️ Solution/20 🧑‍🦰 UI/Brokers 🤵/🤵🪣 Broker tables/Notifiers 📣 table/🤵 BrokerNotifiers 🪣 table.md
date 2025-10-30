# 🤵🪣 Notifiers @ Broker table

> Contains [Notifier 📣 domains](<../../../Notifiers 📣/📣👥 Notifier domain.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Notifiers.yaml
Table: Notifiers
Key: Notifier
Children:
    Wallets: { Wallets.Notifier: Notifiers.Notifier }
```

| Link | Table | Contains
|-|-|-
| Children | [`Wallets` 🪣](<../Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>) | [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
|

<br/>

## Example

Here's the [`GET` command](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) result.

```yaml
# GET|Notifiers|any-notifier.dom
Notifier: any-notifier.dom
```
