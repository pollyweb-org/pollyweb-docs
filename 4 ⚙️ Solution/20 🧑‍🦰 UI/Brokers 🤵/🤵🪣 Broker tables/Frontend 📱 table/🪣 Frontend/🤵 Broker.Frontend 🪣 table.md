# 🤵🪣 Frontend @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Purpose

* [Itemized 🪣 dataset](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) that manages CQRS projections for [Notifier 📣 domains](<../../../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>)



## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Frontend
Key: Wallet
```


## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
Wallet: <wallet-uuid>
PublicKey: ...public-key...
Chats: {...}
Binds: {...}
Tokens: {...}
```