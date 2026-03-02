# 🤵🪣 Notifiers @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵/🤵 Broker 🤲 helper.md>)

> Contains [Notifier 📣 domains](<../../../../Notifiers 📣/📣/📣 Notifier 👥 domain.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

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
| Children | [`Wallets` 🪣](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) | [Wallet 🧑‍🦰 apps](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|Notifiers|any-notifier.dom
Name: any-notifier.dom
```
