# 🤵🪣 Notifiers @ Broker table

> Implements the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Contains [Notifier 📣 domains](<../../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Notifiers.yaml
Prefix: Broker
Table: Notifiers
Key: Name
Children:
    Wallets: { Wallets.Notifier: Notifiers.Name }
```

| Link | Table | Contains
|-|-|-
| Children | [`Wallets` 🪣](<../Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>) | [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|

<br/>

## Example

Here's the [`GET` command](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) result.

```yaml
# GET|Notifiers|any-notifier.dom
Name: any-notifier.dom
```
