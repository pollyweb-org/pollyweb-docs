# 🤵🪣 Frontend @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Purpose

* [Itemized 🪣 dataset](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) that manages CQRS projections for [Notifier 📣 domains](<../../../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>)

> Data access
* [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) by the [`OnFrontendAltered` 🔔 handler](<../🪣🔔 on Altered/🤵 OnFrontendAltered 🔔 handler.md>) 
* [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) by the [`Frontend@Broker` 🅰️ method](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 📃 handler.md>)
<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Frontend
Key: Wallet
```

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
Wallet: <wallet-uuid>
PublicKey: ...public-key...
Chats: {...}
Binds: {...}
Tokens: {...}
```